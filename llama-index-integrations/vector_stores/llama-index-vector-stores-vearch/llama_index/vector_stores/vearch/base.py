import logging
import typing
import uuid
from typing import TYPE_CHECKING, Any, Iterable, List, Optional

import numpy as np

from llama_index.schema import BaseNode, MetadataMode, TextNode
from llama_index.vector_stores.types import (
    VectorStore,
    VectorStoreQuery,
    VectorStoreQueryResult,
)
from llama_index.vector_stores.utils import (
    legacy_metadata_dict_to_node,
    metadata_dict_to_node,
    node_to_metadata_dict,
)

logger = logging.getLogger(__name__)


class VearchVectorStore(VectorStore):
    """
    Vearch vector store:
        embeddings are stored within a Vearch table.
        when query, the index uses Vearch to query for the top
        k most similar nodes.

    Args:
        chroma_collection (chromadb.api.models.Collection.Collection):
            ChromaDB collection instance
    """

    flat_metadata: bool = True
    stores_text: bool = True
    _DEFAULT_TABLE_NAME = "llama_index_vearch"
    _DEFAULT_CLUSTER_DB_NAME = "llama_index_vearch_client_db"

    def __init__(
        self,
        path_or_url: Optional[str] = None,
        table_name: str = _DEFAULT_TABLE_NAME,
        db_name: str = _DEFAULT_CLUSTER_DB_NAME,
        **kwargs: Any,
    ) -> None:
        """
        Initialize vearch vector store
        """
        try:
            import vearch_cluster
        except ImportError:
            raise ValueError(
                "Could not import suitable python package."
                "Please install it with `pip install vearch_cluster."
            )

        if path_or_url is None:
            raise ValueError("Please input url of cluster")
        if not db_name:
            db_name = self._DEFAULT_CLUSTER_DB_NAME
            db_name += "_"
            db_name += str(uuid.uuid4()).split("-")[-1]
        self.using_db_name = db_name
        self.url = path_or_url
        self.vearch = vearch_cluster.VearchCluster(path_or_url)
        if not table_name:
            table_name = self._DEFAULT_TABLE_NAME
            table_name += "_"
            table_name += str(uuid.uuid4()).split("-")[-1]
        self.using_table_name = table_name

    @property
    def client(self) -> Any:
        """Get client."""
        return self.vearch

    def _get_matadata_field(self, metadatas: Optional[List[dict]] = None) -> None:
        field_list = []
        if metadatas:
            for key, value in metadatas[0].items():
                if isinstance(value, int):
                    field_list.append({"field": key, "type": "int"})
                    continue
                if isinstance(value, str):
                    field_list.append({"field": key, "type": "str"})
                    continue
                if isinstance(value, float):
                    field_list.append({"field": key, "type": "float"})
                    continue
                else:
                    raise ValueError("Please check data type,support int, str, float")
        self.field_list = field_list

    def _add_texts(
        self,
        ids: Iterable[str],
        texts: Iterable[str],
        metadatas: Optional[List[dict]] = None,
        embeddings: Optional[List[List[float]]] = None,
        **kwargs: Any,
    ) -> List[str]:
        """
        Returns:
            List of ids from adding the texts into the vectorstore.
        """
        if embeddings is None:
            raise ValueError("embeddings is None")
        self._get_matadata_field(metadatas)
    
        dbs_list = self.vearch.list_dbs()
        if self.using_db_name not in dbs_list:
            create_db_code = self.vearch.create_db(self.using_db_name)
            if not create_db_code:
                raise ValueError("create db failed!!!")
        space_list = self.vearch.list_spaces(self.using_db_name)
        if self.using_table_name not in space_list:
            create_space_code = self._create_space(len(embeddings[0]))
            if not create_space_code:
                raise ValueError("create space failed!!!")
        docid = []
        if embeddings is not None and metadatas is not None:
            meta_field_list = [i["field"] for i in self.field_list]
            for text, metadata, embed, id_d in zip(
                texts, metadatas, embeddings, ids
            ):
                profiles: typing.Dict[str, Any] = {}
                profiles["ref_doc_id"] = id_d
                profiles["text"] = text
                for f in meta_field_list:
                    profiles[f] = metadata[f]
                embed_np = np.array(embed)
                profiles["text_embedding"] = {
                    "feature": (embed_np / np.linalg.norm(embed_np)).tolist()
                }
                insert_res = self.vearch.insert_one(
                    self.using_db_name, self.using_table_name, profiles
                )
                if insert_res["status"] == 200:
                    docid.append(insert_res["_id"])
                    continue
                else:
                    retry_insert = self.vearch.insert_one(
                        self.using_db_name, self.using_table_name, profiles
                    )
                    docid.append(retry_insert["_id"])
                    continue
        return docid

    def _create_space(
        self,
        dim: int = 1024,
    ) -> int:
        """
        Create Cluster VectorStore space.

        Args:
            dim:dimension of vector.

        Return:
            code,0 failed for ,1 for success.
        """
        type_dict = {"int": "integer", "str": "string", "float": "float"}
        space_config = {
            "name": self.using_table_name,
            "partition_num": 1,
            "replica_num": 1,
            "engine": {
                "index_size": 1,
                "retrieval_type": "HNSW",
                "retrieval_param": {
                    "metric_type": "InnerProduct",
                    "nlinks": -1,
                    "efConstruction": -1,
                },
            },
        }
        tmp_proer = {
            "text": {"type": "string"},
            "text_embedding": {
                "type": "vector",
                "index": True,
                "dimension": dim,
                "store_type": "MemoryOnly",
            },
        }
        for item in self.field_list:
            tmp_proer[item["field"]] = {"type": type_dict[item["type"]]}
        space_config["properties"] = tmp_proer

        return self.vearch.create_space(self.using_db_name, space_config)

    def add(
        self,
        nodes: List[BaseNode],
        **add_kwargs: Any,
    ) -> List[str]:
        if not self.vearch:
            raise ValueError("Vearch Engine is not initialized")

        embeddings = []
        metadatas = []
        ids = []
        texts = []
        for node in nodes:
            embeddings.append(node.get_embedding())
            metadatas.append(
                node_to_metadata_dict(
                    node, remove_text=True, flat_metadata=self.flat_metadata
                )
            )
            ids.append(node.node_id)
            texts.append(node.get_content(metadata_mode=MetadataMode.NONE) or "")

        return self._add_texts(
            ids=ids,
            texts=texts,
            metadatas=metadatas,
            embeddings=embeddings,
        )

    def query(
        self,
        query: VectorStoreQuery,
        **kwargs: Any,
    ) -> VectorStoreQueryResult:
        """
        Query index for top k most similar nodes.
        Args:
            query : vector store query.
        Returns:
            VectorStoreQueryResult: Query results.
        """
        meta_filters = {}
        if query.filters is not None:
            for filter_ in query.filters.legacy_filters():
                meta_filters[filter_.key] = filter_.value
        if self.flag:
            meta_field_list = self.vearch.get_space(
                self.using_db_name, self.using_table_name
            )
            meta_field_list.remove("text_embedding")
        embed = query.query_embedding
        if embed is None:
            raise ValueError("query.query_embedding is None")
        k = query.similarity_top_k
        
        query_data = {
            "query": {
                "sum": [
                    {
                        "field": "text_embedding",
                        "feature": (embed / np.linalg.norm(embed)).tolist(),
                    }
                ],
            },
            "retrieval_param": {"metric_type": "InnerProduct", "efSearch": 64},
            "size": k,
            "fields": meta_field_list,
        }
        query_result = self.vearch.search(
            self.using_db_name, self.using_table_name, query_data
        )
        res = query_result["hits"]["hits"]
    
        nodes = []
        similarities = []
        ids = []
        for item in res:
            content = ""
            meta_data = {}
            node_id = ""
            score = item["_score"]
            item = item["_source"]
            for item_key in item:
                if item_key == "text":
                    content = item[item_key]
                    continue
                elif item_key == "_id":
                    node_id = item[item_key]
                    ids.append(node_id)
                    continue
                meta_data[item_key] = item[item_key]
            similarities.append(score)
            try:
                node = metadata_dict_to_node(meta_data)
                node.set_content(content)
            except Exception:
                metadata, node_info, relationships = legacy_metadata_dict_to_node(
                    meta_data
                )
                node = TextNode(
                    text=content,
                    id_=node_id,
                    metadata=metadata,
                    start_char_idx=node_info.get("start", None),
                    end_char_idx=node_info.get("end", None),
                    relationships=relationships,
                )
            nodes.append(node)
        return VectorStoreQueryResult(nodes=nodes, similarities=similarities, ids=ids)

    def _delete(
        self,
        ids: Optional[List[str]] = None,
        **kwargs: Any,
    ) -> None:
        """
        Delete the documents which have the specified ids.
        Args:
            ids: The ids of the embedding vectors.
            **kwargs: Other keyword arguments that subclasses might use.
        Returns:
            Optional[bool]: True if deletion is successful.
            False otherwise, None if not implemented.
        """
        if ids is None or len(ids) == 0:
            return 
        for _id in ids:
            query = {
                    "query": {
                        "filter": [{
                            "term": {
                                "ref_doc_id": [_id],
                                "operator": "and"   
                                }   
                            }]
                    },
                    "size": 10000,
                }
            self.vearch.delete_by_query(self,self.using_db_name, self.using_table_name, query)

    def delete(self, ref_doc_id: str, **delete_kwargs: Any) -> None:
        """Delete nodes using with ref_doc_id.
        Args:
            ref_doc_id (str): The doc_id of the document to delete.
        Returns:
            None
        """
        if len(ref_doc_id) == 0:
            return
        ids: List[str] = []
        ids.append(ref_doc_id)
        self._delete(ids)


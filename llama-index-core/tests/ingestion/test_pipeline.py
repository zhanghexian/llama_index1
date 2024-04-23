from multiprocessing import cpu_count

from llama_index.core.embeddings.mock_embed_model import MockEmbedding
from llama_index.core.extractors import KeywordExtractor
from llama_index.core.ingestion.pipeline import IngestionPipeline
from llama_index.core.llms.mock import MockLLM
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.readers import ReaderConfig, StringIterableReader
from llama_index.core.schema import Document
from llama_index.core.storage.docstore import SimpleDocumentStore


# clean up folders after tests
def teardown_function() -> None:
    import shutil

    shutil.rmtree("./test_pipeline", ignore_errors=True)


def test_build_pipeline() -> None:
    pipeline = IngestionPipeline(
        readers=[
            ReaderConfig(
                reader=StringIterableReader(),
                reader_kwargs={"texts": ["This is a test."]},
            )
        ],
        documents=[Document.example()],
        transformations=[
            SentenceSplitter(),
            KeywordExtractor(llm=MockLLM()),
            MockEmbedding(embed_dim=8),
        ],
    )

    assert len(pipeline.transformations) == 3


def test_run_pipeline() -> None:
    pipeline = IngestionPipeline(
        readers=[
            ReaderConfig(
                reader=StringIterableReader(),
                reader_kwargs={"texts": ["This is a test."]},
            )
        ],
        documents=[Document.example()],
        transformations=[
            SentenceSplitter(),
            KeywordExtractor(llm=MockLLM()),
        ],
    )

    nodes = pipeline.run()

    assert len(nodes) == 2
    assert len(nodes[0].metadata) > 0


def test_save_load_pipeline() -> None:
    documents = [
        Document(text="one", doc_id="1"),
        Document(text="two", doc_id="2"),
        Document(text="one", doc_id="1"),
    ]

    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=25, chunk_overlap=0),
        ],
        docstore=SimpleDocumentStore(),
    )

    nodes = pipeline.run(documents=documents)
    assert len(nodes) == 2
    assert pipeline.docstore is not None
    assert len(pipeline.docstore.docs) == 2

    # dedup will catch the last node
    nodes = pipeline.run(documents=[documents[-1]])
    assert len(nodes) == 0
    assert pipeline.docstore is not None
    assert len(pipeline.docstore.docs) == 2

    # test save/load
    pipeline.persist("./test_pipeline")

    pipeline2 = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=25, chunk_overlap=0),
        ],
    )

    pipeline2.load("./test_pipeline")

    # dedup will catch the last node
    nodes = pipeline.run(documents=[documents[-1]])
    assert len(nodes) == 0
    assert pipeline.docstore is not None
    assert len(pipeline.docstore.docs) == 2


def test_save_load_pipeline_without_docstore() -> None:
    documents = [
        Document(text="one", doc_id="1"),
        Document(text="two", doc_id="2"),
        Document(text="one", doc_id="1"),
    ]

    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=25, chunk_overlap=0),
        ],
    )

    nodes = pipeline.run(documents=documents)
    assert len(nodes) == 3
    assert pipeline.docstore is None

    # dedup will not catch the last node if the document store is not set
    nodes = pipeline.run(documents=[documents[-1]])
    assert len(nodes) == 1
    assert pipeline.docstore is None

    # test save/load
    pipeline.persist("./test_pipeline")

    pipeline2 = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=25, chunk_overlap=0),
        ],
    )

    pipeline2.load("./test_pipeline")

    # dedup will not catch the last node if the document store is not set
    nodes = pipeline.run(documents=[documents[-1]])
    assert len(nodes) == 1
    assert pipeline.docstore is None


def test_pipeline_update() -> None:
    document1 = Document.example()
    document1.id_ = "1"

    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=25, chunk_overlap=0),
        ],
        docstore=SimpleDocumentStore(),
    )

    nodes = pipeline.run(documents=[document1])
    assert len(nodes) == 19
    assert pipeline.docstore is not None
    assert len(pipeline.docstore.docs) == 1

    # adjust document content
    document1 = Document(text="test", doc_id="1")

    # run pipeline again
    nodes = pipeline.run(documents=[document1])

    assert len(nodes) == 1
    assert pipeline.docstore is not None
    assert len(pipeline.docstore.docs) == 1
    assert next(iter(pipeline.docstore.docs.values())).text == "test"  # type: ignore


def test_pipeline_dedup_duplicates_only() -> None:
    documents = [
        Document(text="one", doc_id="1"),
        Document(text="two", doc_id="2"),
        Document(text="three", doc_id="3"),
    ]

    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=25, chunk_overlap=0),
        ],
        docstore=SimpleDocumentStore(),
    )

    nodes = pipeline.run(documents=documents)
    assert len(nodes) == 3

    nodes = pipeline.run(documents=documents)
    assert len(nodes) == 0


def test_pipeline_parallel() -> None:
    document1 = Document.example()
    document1.id_ = "1"
    document2 = Document(text="One\n\n\nTwo\n\n\nThree.", doc_id="2")

    pipeline = IngestionPipeline(
        transformations=[
            SentenceSplitter(chunk_size=25, chunk_overlap=0),
        ],
        docstore=SimpleDocumentStore(),
    )

    num_workers = min(2, cpu_count())
    nodes = pipeline.run(documents=[document1, document2], num_workers=num_workers)
    assert len(nodes) == 20
    assert pipeline.docstore is not None
    assert len(pipeline.docstore.docs) == 2

# ChangeLog

## [2024-04-17]

### `llama-index-core` [0.10.30]

- Add intermediate outputs to QueryPipeline (#12683)
- Fix show progress causing results to be out of order (#12897)
- add OR filter condition support to simple vector store (#12823)
- improved custom agent init (#12824)
- fix pipeline load without docstore (#12808)
- Use async `_aprocess_actions` in `_arun_step_stream` (#12846)
- provide the exception to the StreamChatErrorEvent (#12879)
- fix bug in load and search tool spec (#12902)

### `llama-index-embeddings-azure-opena` [0.1.7]

- Expose azure_ad_token_provider argument to support token expiration (#12818)

### `llama-index-embeddings-cohere` [0.1.8]

- Add httpx_async_client option (#12896)

### `llama-index-embeddings-ipex-llm` [0.1.0]

- add ipex-llm embedding integration (#12740)

### `llama-index-embeddings-octoai` [0.1.0]

- add octoai embeddings (#12857)

### `llama-index-llms-azure-openai` [0.1.6]

- Expose azure_ad_token_provider argument to support token expiration (#12818)

### `llama-index-llms-ipex-llm` [0.1.2]

- add support for loading "low-bit format" model to IpexLLM integration (#12785)

### `llama-index-llms-mistralai` [0.1.11]

- support `open-mixtral-8x22b` (#12894)

### `llama-index-packs-agents-lats` [0.1.0]

- added LATS agent pack (#12735)

### `llama-index-readers-smart-pdf-loader` [0.1.4]

- Use passed in metadata for documents (#12844)

### `llama-index-readers-web` [0.1.9]

- added Firecrawl Web Loader (#12825)

### `llama-index-vector-stores-milvus` [0.1.10]

- use batch insertions into Milvus vector store (#12837)

### `llama-index-vector-stores-vearch` [0.1.0]

- add vearch to vector stores (#10972)

## [2024-04-13]

### `llama-index-core` [0.10.29]

- **BREAKING** Moved `PandasQueryEngine` and `PandasInstruction` parser to `llama-index-experimental` (#12419)
  - new install: `pip install -U llama-index-experimental`
  - new import: `from llama_index.experimental.query_engine import PandasQueryEngine`
- Fixed some core dependencies to make python3.12 work nicely (#12762)
- update async utils `run_jobs()` to include tqdm description (#12812)
- Refactor kvdocstore delete methods (#12681)

### `llama-index-llms-bedrock` [0.1.6]

- Support for Mistral Large from Bedrock (#12804)

### `llama-index-llms-openvino` [0.1.0]

- Added OpenVino LLMs (#12639)

### `llama-index-llms-predibase` [0.1.4]

- Update LlamaIndex-Predibase Integration to latest API (#12736)
- Enable choice of either Predibase-hosted or HuggingFace-hosted fine-tuned adapters in LlamaIndex-Predibase integration (#12789)

### `llama-index-output-parsers-guardrails` [0.1.3]

- Modernize GuardrailsOutputParser (#12676)

### `llama-index-packs-agents-coa` [0.1.0]

- Chain-of-Abstraction Agent Pack (#12757)

### `llama-index-packs-code-hierarchy` [0.1.3]

- Fixed issue with chunking multi-byte characters (#12715)

### `llama-index-packs-raft-dataset` [0.1.4]

- Fix bug in raft dataset generator - multiple system prompts (#12751)

### `llama-index-postprocessor-openvino-rerank` [0.1.2]

- Add openvino rerank support (#12688)

### `llama-index-readers-file` [0.1.18]

- convert to Path in docx reader if input path str (#12807)
- make pip check work for optional pdf packages (#12758)

### `llama-index-readers-s3` [0.1.7]

- wrong doc id when using default s3 endpoint in S3Reader (#12803)

### `llama-index-retrievers-bedrock` [0.1.0]

- Add Amazon Bedrock knowledge base integration as retriever (#12737)

### `llama-index-retrievers-mongodb-atlas-bm25-retriever` [0.1.3]

- Add mongodb atlas bm25 retriever (#12519)

### `llama-index-storage-chat-store-redis` [0.1.3]

- fix message serialization in redis chat store (#12802)

### `llama-index-vector-stores-astra-db` [0.1.6]

- Relax dependency version to accept astrapy `1.*` (#12792)

### `llama-index-vector-stores-couchbase` [0.1.0]

- Add support for Couchbase as a Vector Store (#12680)

### `llama-index-vector-stores-elasticsearch` [0.1.7]

- Fix elasticsearch hybrid rrf window_size (#12695)

### `llama-index-vector-stores-milvus` [0.1.8]

- Added support to retrieve metadata fields from milvus (#12626)

### `llama-index-vector-stores-redis` [0.2.0]

- Modernize redis vector store, use redisvl (#12386)

### `llama-index-vector-stores-qdrant` [0.2.0]

- refactor: Switch default Qdrant sparse encoder (#12512)

## [2024-04-09]

### `llama-index-core` [0.10.28]

- Support indented code block fences in markdown node parser (#12393)
- Pass in output parser to guideline evaluator (#12646)
- Added example of query pipeline + memory (#12654)
- Add missing node postprocessor in CondensePlusContextChatEngine async mode (#12663)
- Added `return_direct` option to tools /tool metadata (#12587)
- Add retry for batch eval runner (#12647)
- Thread-safe instrumentation (#12638)
- Coroutine-safe instrumentation Spans #12589
- Add in-memory loading for non-default filesystems in PDFReader (#12659)
- Remove redundant tokenizer call in sentence splitter (#12655)
- Add SynthesizeComponent import to shortcut imports (#12655)
- Improved truncation in SimpleSummarize (#12655)
- adding err handling in eval_utils default_parser for correctness (#12624)
- Add async_postprocess_nodes at RankGPT Postprocessor Nodes (#12620)
- Fix MarkdownNodeParser ref_doc_id (#12615)

### `llama-index-embeddings-openvino` [0.1.5]

- Added initial support for openvino embeddings (#12643)

### `llama-index-llms-anthropic` [0.1.9]

- add anthropic tool calling (#12591)

### `llama-index-llms-ipex-llm` [0.1.1]

- add ipex-llm integration (#12322)
- add more data types support to ipex-llm llm integration (#12635)

### `llama-index-llms-openllm` [0.1.4]

- Proper PrivateAttr usage in OpenLLM (#12655)

### `llama-index-multi-modal-llms-anthropic` [0.1.4]

- Bumped anthropic dep version (#12655)

### `llama-index-multi-modal-llms-gemini` [0.1.5]

- bump generativeai dep (#12645)

### `llama-index-packs-dense-x-retrieval` [0.1.4]

- Add streaming support for DenseXRetrievalPack (#12607)

### `llama-index-readers-mongodb` [0.1.4]

- Improve efficiency of MongoDB reader (#12664)

### `llama-index-readers-wikipedia` [0.1.4]

- Added multilingual support for the Wikipedia reader (#12616)

### `llama-index-storage-index-store-elasticsearch` [0.1.3]

- remove invalid chars from default collection name (#12672)

### `llama-index-vector-stores-milvus` [0.1.8]

- Added support to retrieve metadata fields from milvus (#12626)
- Bug fix - Similarity metric is always IP for MilvusVectorStore (#12611)

## [2024-04-04]

### `llama-index-agent-openai` [0.2.2]

- Update imports for message thread typing (#12437)

### `llama-index-core` [0.10.27]

- Fix for pydantic query engine outputs being blank (#12469)
- Add span_id attribute to Events (instrumentation) (#12417)
- Fix RedisDocstore node retrieval from docs property (#12324)
- Add node-postprocessors to retriever_tool (#12415)
- FLAREInstructQueryEngine : delegating retriever api if the query engine supports it (#12503)
- Make chat message to dict safer (#12526)
- fix check in batch eval runner for multi-kwargs (#12563)
- Fixes agent_react_multimodal_step.py bug with partial args (#12566)

### `llama-index-embeddings-clip` [0.1.5]

- Added support to load clip model from local file path (#12577)

### `llama-index-embeddings-cloudflar-workersai` [0.1.0]

- text embedding integration: Cloudflare Workers AI (#12446)

### `llama-index-embeddings-voyageai` [0.1.4]

- Fix pydantic issue in class definition (#12469)

### `llama-index-finetuning` [0.1.5]

- Small typo fix in QA generation prompt (#12470)

### `llama-index-graph-stores-falkordb` [0.1.3]

- Replace redis driver with FalkorDB driver (#12434)

### `llama-index-llms-anthropic` [0.1.8]

- Add ability to pass custom HTTP headers to Anthropic client (#12558)

### `llama-index-llms-cohere` [0.1.6]

- Add support for Cohere Command R+ model (#12581)

### `llama-index-llms-databricks` [0.1.0]

- Integrations with DataBricks LLM API (#12432)

### `llama-index-llms-watsonx` [0.1.6]

- Updated Watsonx foundation models (#12493)
- Updated base model name on watsonx integration #12491

### `lama-index-postprocessor-rankllm-rerank` [0.1.2]

- Add RankGPT support inside RankLLM (#12475)

### `llama-index-readers-microsoft-sharepoint` [0.1.7]

- Use recursive strategy by default for SharePoint (#12557)

### `llama-index-readers-web` [0.1.8]

- Readability web page reader fix playwright async api bug (#12520)

### `llama-index-vector-stores-kdbai` [0.1.5]

- small `to_list` fix (#12515)

### `llama-index-vector-stores-neptune` [0.1.0]

- Add support for Neptune Analytics as a Vector Store (#12423)

### `llama-index-vector-stores-postgres` [0.1.5]

- fix(postgres): numeric metadata filters (#12583)

## [2024-03-31]

### `llama-index-core` [0.10.26]

- pass proper query bundle in QueryFusionRetriever (#12387)
- Update llama_parse_json_element.py to fix error on lists (#12402)
- Add node postprocessors to retriever tool (#12415)
- Fix bug where user specified llm is not respected in fallback logic in element node parsers(#12403)
- log proper LLM response key for async callback manager events (#12421)
- Deduplicate the two built-in react system prompts; Also make it read from a Markdown file (#12307)
- fix bug in BatchEvalRunner for multi-evaluator eval_kwargs_lists (#12418)
- add the callback manager event for vector store index insert_nodes (#12443)
- fixes an issue with serializing chat messages into chat stores when they contain pydantic API objects (#12394)
- fixes an issue with slow memory.get() operation (caused by multiple calls to get_all()) (#12394)
- fixes an issue where an agent+tool message pair is cut from the memory (#12394)
- Added `FnNodeMapping` for object index (#12391)
- Make object mapping optional / hidden for object index (#12391)
- Make object index easier to create from existing vector db (#12391)
- When LLM failed to follow the react response template, tell it so #12300

### `llama-index-embeddings-cohere` [0.1.5]

- Bump cohere version to 5.1.1 (#12279)

### `llama-index-embeddings-itrex` [0.1.0]

- add Intel Extension for Transformers embedding model (#12410)

### `llama-index-graph-stores-neo4j` [0.1.4]

- make neo4j query insensitive (#12337)

### `llama-index-llms-cohere` [0.1.5]

- Bump cohere version to 5.1.1 (#12279)

### `llama-index-llms-ipex-llm` [0.1.0]

- add ipex-llm integration (#12322)

### `llama-index-llms-litellm` [0.1.4]

- Fix litellm ChatMessage role validation error (#12449)

### `llama-index-llms-openai` [0.1.14]

- Use `FunctionCallingLLM` base class in OpenAI (#12227)

### `llama-index-packs-self-rag` [0.1.4]

- Fix llama-index-core dep (#12374)

### `llama-index-postprocessor-cohere-rerank` [0.1.4]

- Bump cohere version to 5.1.1 (#12279)

### `llama-index-postprocessor-rankllm-rerank` [0.1.1]

- Added RankLLM rerank (#12296)
- RankLLM fixes (#12399)

### `llama-index-readers-papers` [0.1.4]

- Fixed bug with path names (#12366)

### `llama-index-vector-stores-analyticdb` [0.1.1]

- Add AnalyticDB VectorStore (#12230)

### `llama-index-vector-stores-kdbai` [0.1.4]

- Fixed typo in imports/readme (#12370)

### `llama-index-vector-stores-qdrant` [0.1.5]

- add `in` filter operator for qdrant (#12376)

## [2024-03-27]

### `llama-index-core` [0.10.25]

- Add score to NodeWithScore in KnowledgeGraphQueryEngine (#12326)
- Batch eval runner fixes (#12302)

### `llama-index-embeddings-cohere` [0.1.5]

- Added support for binary / quantized embeddings (#12321)

### `llama-index-llms-mistralai` [0.1.10]

- add support for custom endpoints to MistralAI (#12328)

### `llama-index-storage-kvstore-redis` [0.1.3]

- Fix RedisDocstore node retrieval from docs property (#12324)

## [2024-03-26]

### `llama-index-core` [0.10.24]

- pretty prints in `LlamaDebugHandler` (#12216)
- stricter interpreter constraints on pandas query engine (#12278)
- PandasQueryEngine can now execute 'pd.\*' functions (#12240)
- delete proper metadata in docstore delete function (#12276)
- improved openai agent parsing function hook (#12062)
- add raise_on_error flag for SimpleDirectoryReader (#12263)
- remove un-caught openai import in core (#12262)
- Fix download_llama_dataset and download_llama_pack (#12273)
- Implement EvalQueryEngineTool (#11679)
- Expand instrumenation Span coverage for AgentRunner (#12249)
- Adding concept of function calling agent/llm (mistral supported for now) (#12222, )

### `llama-index-embeddings-huggingface` [0.2.0]

- Use `sentence-transformers` as a backend (#12277)

### `llama-index-postprocessor-voyageai-rerank` [0.1.0]

- Added voyageai as a reranker (#12111)

### `llama-index-readers-gcs` [0.1.0]

- Added google cloud storage reader (#12259)

### `llama-index-readers-google` [0.2.1]

- Support for different drives (#12146)
- Remove unnecessary PyDrive dependency from Google Drive Reader (#12257)

### `llama-index-readers-readme` [0.1.0]

- added readme.com reader (#12246)

### `llama-index-packs-raft` [0.1.3]

- added pack for RAFT (#12275)

## [2024-03-23]

### `llama-index-core` [0.10.23]

- Added `(a)predict_and_call()` function to base LLM class + openai + mistralai (#12188)
- fixed bug with `wait()` in async agent streaming (#12187)

### `llama-index-embeddings-alephalpha` [0.1.0]

- Added alephalpha embeddings (#12149)

### `llama-index-llms-alephalpha` [0.1.0]

- Added alephalpha LLM (#12149)

### `llama-index-llms-openai` [0.1.7]

- fixed bug with `wait()` in async agent streaming (#12187)

### `llama-index-readers-docugami` [0.1.4]

- fixed import errors in docugami reader (#12154)

### `llama-index-readers-file` [0.1.12]

- fix PDFReader for remote fs (#12186)

## [2024-03-21]

### `llama-index-core` [0.10.22]

- Updated docs backend from sphinx to mkdocs, added ALL api reference, some light re-org, better search (#11301)
- Added async loading to `BaseReader` class (although its fake async for now) (#12156)
- Fix path implementation for non-local FS in `SimpleDirectoryReader` (#12141)
- add args/kwargs to spans, payloads for retrieval events, in instrumentation (#12147)
- [react agent] Upon exception, say so, so that Agent can correct itself (#12137)

### `llama-index-embeddings-together` [0.1.3]

- Added rate limit handling (#12127)

### `llama-index-graph-stores-neptune` [0.1.3]

- Add Amazon Neptune Support as Graph Store (#12097)

### `llama-index-llms-vllm` [0.1.7]

- fix VllmServer to work without CUDA-required vllm core (#12003)

### `llama-index-readers-s3` [0.1.4]

- Use S3FS in S3Reader (#12061)

### `llama-index-storage-docstore-postgres` [0.1.3]

- Added proper kvstore dep (#12157)

### `llama-index-storage-index-store-postgres` [0.1.3]

- Added proper kvstore dep (#12157)

### `llama-index-vector-stores-elasticsearch` [0.1.6]

- fix unclosed session in es add function #12135

### `llama-index-vector-stores-kdbai` [0.1.3]

- Add support for `KDBAIVectorStore` (#11967)

## [2024-03-20]

### `llama-index-core` [0.10.21]

- Lazy init for async elements StreamingAgentChatResponse (#12116)
- Fix streaming generators get bug by SynthesisEndEvent (#12092)
- CLIP embedding more models (#12063)

### `llama-index-packs-raptor` [0.1.3]

- Add `num_workers` to summary module (#)

### `llama-index-readers-telegram` [0.1.5]

- Fix datetime fields (#12112)
- Add ability to select time period of posts/messages (#12078)

### `llama-index-embeddings-openai` [0.1.7]

- Add api version/base api as optional for open ai embedding (#12091)

### `llama-index-networks` [0.2.1]

- Add node postprocessing to network retriever (#12027)
- Add privacy-safe networks demo (#12027)

### `llama-index-callbacks-langfuse` [0.1.3]

- Chore: bumps min version of langfuse dep (#12077)

### `llama-index-embeddings-google` [0.1.4]

- Chore: bumps google-generativeai dep (#12085)

### `llama-index-embeddings-gemini` [0.1.5]

- Chore: bumps google-generativeai dep (#12085)

### `llama-index-llms-gemini` [0.1.6]

- Chore: bumps google-generativeai dep (#12085)

### `llama-index-llms-palm` [0.1.4]

- Chore: bumps google-generativeai dep (#12085)

### `llama-index-multi-modal-llms-google` [0.1.4]

- Chore: bumps google-generativeai dep (#12085)

### `llama-index-vector-stores-google` [0.1.5]

- Chore: bumps google-generativeai dep (#12085)

### `llama-index-storage-kvstore-elasticsearch` [0.1.0]

- New integration (#12068)

### `llama-index-readers-google` [0.1.7]

- Fix - Google Drive Issue of not loading same name files (#12022)

### `llama-index-vector-stores-upstash` [0.1.3]

- Adding Metadata Filtering support for UpstashVectorStore (#12054)

### `llama-index-packs-raptor` [0.1.2]

- Fix: prevent RaptorPack infinite recursion (#12008)

### `llama-index-embeddings-huggingface-optimum` [0.1.4]

- Fix(OptimumEmbedding): removing token_type_ids causing ONNX validation issues

### `llama-index-llms-anthropic` [0.1.7]

- Fix: Anthropic LLM merge consecutive messages with same role (#12013)

### `llama-index-packs-diff-private-simple-dataset` [0.1.0]

- DiffPrivacy ICL Pack - OpenAI Completion LLMs (#11881)

### `llama-index-cli` [0.1.11]

- Remove llama_hub_url keyword from download_llama_dataset of command (#12038)

## [2024-03-14]

### `llama-index-core` [0.10.20]

- New `instrumentation` module for observability (#11831)
- Allow passing in LLM for `CitationQueryEngine` (#11914)
- Updated keyval docstore to allow changing suffix in addition to namespace (#11873)
- Add (some) async streaming support to query_engine #11949

### `llama-index-embeddings-dashscope` [0.1.3]

- Fixed embedding type for query texts (#11901)

### `llama-index-embeddings-premai` [0.1.3]

- Support for premai embeddings (#11954)

### `llama-index-networks` [0.2.0]

- Added support for network retrievers (#11800)

### `llama-index-llms-anthropic` [0.1.6]

- Added support for haiku (#11916)

### `llama-index-llms-mistralai` [0.1.6]

- Fixed import error for ChatMessage (#11902)

### `llama-index-llms-openai` [0.1.11]

- added gpt-35-turbo-0125 for AZURE_TURBO_MODELS (#11956)
- fixed error with nontype in logprobs (#11967)

### `llama-index-llms-premai` [0.1.4]

- Support for premai llm (#11954)

### `llama-index-llms-solar` [0.1.3]

- Support for solar as an LLM class (#11710)

### `llama-index-llms-vertex` [0.1.5]

- Add support for medlm in vertex (#11911)

### `llama-index-readers-goolge` [0.1.6]

- added README files and query string for google drive reader (#11724)

### `llama-index-readers-file` [0.1.11]

- Updated ImageReader to add `plain_text` option to trigger pytesseract (#11913)

### `llama-index-readers-pathway` [0.1.3]

- use pure requests to reduce deps, simplify code (#11924)

### `llama-index-retrievers-pathway` [0.1.3]

- use pure requests to reduce deps, simplify code (#11924)

### `llama-index-storage-docstore-mongodb` [0.1.3]

- Allow changing suffix for mongodb docstore (#11873)

### `llama-index-vector-stores-databricks` [0.1.1]

- Support for databricks vector search as a vector store (#10754)

### `llama-index-vector-stores-opensearch` [0.1.8]

- (re)implement proper delete (#11959)

### `llama-index-vector-stores-postgres` [0.1.4]

- Fixes for IN filters and OR text search (#11872, #11927)

## [2024-03-12]

### `llama-index-cli` [0.1.9]

- Removed chroma as a bundled dep to reduce `llama-index` deps

### `llama-index-core` [0.10.19]

- Introduce retries for rate limits in `OpenAI` llm class (#11867)
- Added table comments to SQL table schemas in `SQLDatabase` (#11774)
- Added `LogProb` type to `ChatResponse` object (#11795)
- Introduced `LabelledSimpleDataset` (#11805)
- Fixed insert `IndexNode` objects with unserializable objects (#11836)
- Fixed stream chat type error when writing response to history in `CondenseQuestionChatEngine` (#11856)
- Improve post-processing for json query engine (#11862)

### `llama-index-embeddings-cohere` [0.1.4]

- Fixed async kwarg error (#11822)

### `llama-index-embeddings-dashscope` [0.1.2]

- Fixed pydantic import (#11765)

### `llama-index-graph-stores-neo4j` [0.1.3]

- Properly close connection after verifying connectivity (#11821)

### `llama-index-llms-cohere` [0.1.3]

- Add support for new `command-r` model (#11852)

### `llama-index-llms-huggingface` [0.1.4]

- Fixed streaming decoding with special tokens (#11807)

### `llama-index-llms-mistralai` [0.1.5]

- Added support for latest and open models (#11792)

### `llama-index-tools-finance` [0.1.1]

- Fixed small bug when passing in the API get for stock news (#11772)

### `llama-index-vector-stores-chroma` [0.1.6]

- Slimmed down chroma deps (#11775)

### `llama-index-vector-stores-lancedb` [0.1.3]

- Fixes for deleting (#11825)

### `llama-index-vector-stores-postgres` [0.1.3]

- Support for nested metadata filters (#11778)

## [2024-03-07]

### `llama-index-callbacks-deepeval` [0.1.3]

- Update import path for callback handler (#11754)

### `llama-index-core` [0.10.18]

- Ensure `LoadAndSearchToolSpec` loads document objects (#11733)
- Fixed bug for no nodes in `QueryFusionRetriever` (#11759)
- Allow using different runtime kwargs for different evaluators in `BatchEvalRunner` (#11727)
- Fixed issues with fsspec + `SimpleDirectoryReader` (#11665)
- Remove `asyncio.run()` requirement from guideline evaluator (#11719)

### `llama-index-embeddings-voyageai` [0.1.3]

- Update voyage embeddings to use proper clients (#11721)

### `llama-index-indices-managed-vectara` [0.1.3]

- Fixed issues with vectara query engine in non-summary mode (#11668)

### `llama-index-llms-mymagic` [0.1.5]

- Add `return_output` option for json output with query and response (#11761)

### `llama-index-packs-code-hierarchy` [0.1.0]

- Added support for a `CodeHiearchyAgentPack` that allows for agentic traversal of a codebase (#10671)

### `llama-index-packs-cohere-citation-chat` [0.1.3]

- Added a new llama-pack for citations + chat with cohere (#11697)

### `llama-index-vector-stores-milvus` [0.1.6]

- Prevent forced `flush()` on document add (#11734)

### `llama-index-vector-stores-opensearch` [0.1.7]

- Small typo in metadata column name (#11751)

### `llama-index-vector-stores-tidbvector` [0.1.0]

- Initial support for TiDB vector store (#11635)

### `llama-index-vector-stores-weaviate` [0.1.4]

- Small fix for `int` fields in metadata filters (#11742)

## [2024-03-06]

New format! Going to try out reporting changes per package.

### `llama-index-cli` [0.1.8]

- Update mappings for `upgrade` command (#11699)

### `llama-index-core` [0.10.17]

- add `relative_score` and `dist_based_score` to `QueryFusionRetriever` (#11667)
- check for `none` in async agent queue (#11669)
- allow refine template for `BaseSQLTableQueryEngine` (#11378)
- update mappings for llama-packs (#11699)
- fixed index error for extracting rel texts in KG index (#11695)
- return proper response types from synthesizer when no nodes (#11701)
- Inherit metadata to summaries in DocumentSummaryIndex (#11671)
- Inherit callback manager in sql query engines (#11662)
- Fixed bug with agent streaming not being written to chat history (#11675)
- Fixed a small bug with `none` deltas when streaming a function call with an agent (#11713)

### `llama-index-multi-modal-llms-anthropic` [0.1.2]

- Added support for new multi-modal models `haiku` and `sonnet` (#11656)

### `llama-index-packs-finchat` [0.1.0]

- Added a new llama-pack for hierarchical agents + finance chat (#11387)

### `llama-index-readers-file` [0.1.8]

- Added support for checking if NLTK files are already downloaded (#11676)

### `llama-index-readers-json` [0.1.4]

- Use the metadata passed in when creating documents (#11626)

### `llama-index-vector-stores-astra-db` [0.1.4]

- Update wording in warning message (#11702)

### `llama-index-vector-stores-opensearch` [0.1.7]

- Avoid calling `nest_asyncio.apply()` in code to avoid confusing errors for users (#11707)

### `llama-index-vector-stores-qdrant` [0.1.4]

- Catch RPC errors (#11657)

## [0.10.16] - 2024-03-05

### New Features

- Anthropic support for new models (#11623, #11612)
- Easier creation of chat prompts (#11583)
- Added a raptor retriever llama-pack (#11527)
- Improve batch cohere embeddings through bedrock (#11572)
- Added support for vertex AI embeddings (#11561)

### Bug Fixes / Nits

- Ensure order in async embeddings generation (#11562)
- Fixed empty metadata for csv reader (#11563)
- Serializable fix for composable retrievers (#11617)
- Fixed milvus metadata filter support (#11566)
- FIxed pydantic import in clickhouse vector store (#11631)
- Fixed system prompts for gemini/vertext-gemini (#11511)

## [0.10.15] - 2024-03-01

### New Features

- Added FeishuWikiReader (#11491)
- Added videodb retriever integration (#11463)
- Added async to opensearch vector store (#11513)
- New LangFuse one-click callback handler (#11324)

### Bug Fixes / Nits

- Fixed deadlock issue with async chat streaming (#11548)
- Improved hidden file check in SimpleDirectoryReader (#11496)
- Fixed null values in document metadata when using SimpleDirectoryReader (#11501)
- Fix for sqlite utils in jsonalyze query engine (#11519)
- Added base url and timeout to ollama multimodal LLM (#11526)
- Updated duplicate handling in query fusion retriever (#11542)
- Fixed bug in kg indexx struct updating (#11475)

## [0.10.14] - 2024-02-28

### New Features

- Released llama-index-networks (#11413)
- Jina reranker (#11291)
- Added DuckDuckGo agent search tool (#11386)
- helper functions for chatml (#10272)
- added brave search tool for agents (#11468)
- Added Friendli LLM integration (#11384)
- metadata only queries for chromadb (#11328)

### Bug Fixes / Nits

- Fixed inheriting llm callback in synthesizers (#11404)
- Catch delete error in milvus (#11315)
- Fixed pinecone kwargs issue (#11422)
- Supabase metadata filtering fix (#11428)
- api base fix in gemini embeddings (#11393)
- fix elasticsearch vector store await (#11438)
- vllm server cuda fix (#11442)
- fix for passing LLM to context chat engine (#11444)
- set input types for cohere embeddings (#11288)
- default value for azure ad token (#10377)
- added back prompt mixin for react agent (#10610)
- fixed system roles for gemini (#11481)
- fixed mean agg pooling returning numpy float values (#11458)
- improved json path parsing for JSONQueryEngine (#9097)

## [0.10.13] - 2024-02-26

### New Features

- Added a llama-pack for KodaRetriever, for on-the-fly alpha tuning (#11311)
- Added support for `mistral-large` (#11398)
- Last token pooling mode for huggingface embeddings models like SFR-Embedding-Mistral (#11373)
- Added fsspec support to SimpleDirectoryReader (#11303)

### Bug Fixes / Nits

- Fixed an issue with context window + prompt helper (#11379)
- Moved OpenSearch vector store to BasePydanticVectorStore (#11400)
- Fixed function calling in fireworks LLM (#11363)
- Made cohere embedding types more automatic (#11288)
- Improve function calling in react agent (#11280)
- Fixed MockLLM imports (#11376)

## [0.10.12] - 2024-02-22

### New Features

- Added `llama-index-postprocessor-colbert-rerank` package (#11057)
- `MyMagicAI` LLM (#11263)
- `MariaTalk` LLM (#10925)
- Add retries to github reader (#10980)
- Added FireworksAI embedding and LLM modules (#10959)

### Bug Fixes / Nits

- Fixed string formatting in weaviate (#11294)
- Fixed off-by-one error in semantic splitter (#11295)
- Fixed `download_llama_pack` for multiple files (#11272)
- Removed `BUILD` files from packages (#11267)
- Loosened python version reqs for all packages (#11267)
- Fixed args issue with chromadb (#11104)

## [0.10.11] - 2024-02-21

### Bug Fixes / Nits

- Fixed multi-modal LLM for async acomplete (#11064)
- Fixed issue with llamaindex-cli imports (#11068)

## [0.10.10] - 2024-02-20

I'm still a bit wonky with our publishing process -- apologies. This is just a version
bump to ensure the changes that were supposed to happen in 0.10.9 actually
did get published. (AF)

## [0.10.9] - 2024-02-20

- add llama-index-cli dependency

## [0.10.7] - 2024-02-19

### New Features

- Added Self-Discover llamapack (#10951)

### Bug Fixes / Nits

- Fixed linting in CICD (#10945)
- Fixed using remote graph stores (#10971)
- Added missing LLM kwarg in NoText response synthesizer (#10971)
- Fixed openai import in rankgpt (#10971)
- Fixed resolving model name to string in openai embeddings (#10971)
- Off by one error in sentence window node parser (#10971)

## [0.10.6] - 2024-02-17

First, apologies for missing the changelog the last few versions. Trying to figure out the best process with 400+ packages.

At some point, each package will have a dedicated changelog.

But for now, onto the "master" changelog.

### New Features

- Added `NomicHFEmbedding` (#10762)
- Added `MinioReader` (#10744)

### Bug Fixes / Nits

- Various fixes for clickhouse vector store (#10799)
- Fix index name in neo4j vector store (#10749)
- Fixes to sagemaker embeddings (#10778)
- Fixed performance issues when splitting nodes (#10766)
- Fix non-float values in reranker + b25 (#10930)
- OpenAI-agent should be a dep of openai program (#10930)
- Add missing shortcut imports for query pipeline components (#10930)
- Fix NLTK and tiktoken not being bundled properly with core (#10930)
- Add back `llama_index.core.__version__` (#10930)

## [0.10.3] - 2024-02-13

### Bug Fixes / Nits

- Fixed passing in LLM to `as_chat_engine` (#10605)
- Fixed system prompt formatting for anthropic (#10603)
- Fixed elasticsearch vector store error on `__version__` (#10656)
- Fixed import on openai pydantic program (#10657)
- Added client back to opensearch vector store exports (#10660)
- Fixed bug in SimpleDirectoryReader not using file loaders properly (#10655)
- Added lazy LLM initialization to RankGPT (#10648)
- Fixed bedrock embedding `from_credentials` passing ing the model name (#10640)
- Added back recent changes to TelegramReader (#10625)

## [0.10.0, 0.10.1] - 2024-02-12

### Breaking Changes

- Several changes are introduced. See the [full blog post](https://blog.llamaindex.ai/llamaindex-v0-10-838e735948f8) for complete details.

## [0.9.48] - 2024-02-12

### Bug Fixes / Nits

- Add back deprecated API for BedrockEmbdding (#10581)

## [0.9.47] - 2024-02-11

Last patch before v0.10!

### New Features

- add conditional links to query pipeline (#10520)
- refactor conditional links + add to cookbook (#10544)
- agent + query pipeline cleanups (#10563)

### Bug Fixes / Nits

- Add sleep to fix lag in chat stream (#10339)
- OllamaMultiModal kwargs (#10541)
- Update Ingestion Pipeline to handle empty documents (#10543)
- Fixing minor spelling error (#10516)
- fix elasticsearch async check (#10549)
- Docs/update slack demo colab (#10534)
- Adding the possibility to use the IN operator for PGVectorStore (#10547)
- fix agent reset (#10562)
- Fix MD duplicated Node id from multiple docs (#10564)

## [0.9.46] - 2024-02-08

### New Features

- Update pooling strategy for embedding models (#10536)
- Add Multimodal Video RAG example (#10530)
- Add SECURITY.md (#10531)
- Move agent module guide up one-level (#10519)

### Bug Fixes / Nits

- Deeplake fixes (#10529)
- Add Cohere section for llamaindex (#10523)
- Fix md element (#10510)

## [0.9.45.post1] - 2024-02-07

### New Features

- Upgraded deeplake vector database to use BasePydanticVectorStore (#10504)

### Bug Fixes / Nits

- Fix MD parser for inconsistency tables (#10488)
- Fix ImportError for pypdf in MetadataExtractionSEC.ipynb (#10491)

## [0.9.45] - 2024-02-07

### New Features

- Refactor: add AgentRunner.from_llm method (#10452)
- Support custom prompt formatting for non-chat LLMS (#10466)
- Bump cryptography from 41.0.7 to 42.0.0 (#10467)
- Add persist and load method for Colbert Index (#10477)
- Allow custom agent to take in user inputs (#10450)

### Bug Fixes / Nits

- remove exporter from arize-phoenix global callback handler (#10465)
- Fixing Dashscope qwen llm bug (#10471)
- Fix: calling AWS Bedrock models (#10443)
- Update Azure AI Search (fka Azure Cognitive Search) vector store integration to latest client SDK 11.4.0 stable + updating jupyter notebook sample (#10416)
- fix some imports (#10485)

## [0.9.44] - 2024-02-05

### New Features

- ollama vision cookbook (#10438)
- Support Gemini "transport" configuration (#10457)
- Add Upstash Vector (#10451)

## [0.9.43] - 2024-02-03

### New Features

- Add multi-modal ollama (#10434)

### Bug Fixes / Nits

- update base class for astradb (#10435)

## [0.9.42.post1] - 2024-02-02

### New Features

- Add Async support for Base nodes parser (#10418)

## [0.9.42] - 2024-02-02

### New Features

- Add support for `gpt-3.5-turbo-0125` (#10412)
- Added `create-llama` support to rag cli (#10405)

### Bug Fixes / Nits

- Fixed minor bugs in lance-db vector store (#10404)
- Fixed streaming bug in ollama (#10407)

## [0.9.41] - 2024-02-01

### New Features

- Nomic Embedding (#10388)
- Dashvector support sparse vector (#10386)
- Table QA with MarkDownParser and Benchmarking (#10382)
- Simple web page reader (#10395)

### Bug Fixes / Nits

- fix full node content in KeywordExtractor (#10398)

## [0.9.40] - 2024-01-30

### New Features

- Improve and fix bugs for MarkdownElementNodeParser (#10340)
- Fixed and improve Perplexity support for new models (#10319)
- Ensure system_prompt is passed to Perplexity LLM (#10326)
- Extended BaseRetrievalEvaluator to include an optional PostProcessor (#10321)

## [0.9.39] - 2024-01-26

### New Features

- Support for new GPT Turbo Models (#10291)
- Support Multiple docs for Sentence Transformer Fine tuning(#10297)

### Bug Fixes / Nits

- Marvin imports fixed (#9864)

## [0.9.38] - 2024-01-25

### New Features

- Support for new OpenAI v3 embedding models (#10279)

### Bug Fixes / Nits

- Extra checks on sparse embeddings for qdrant (#10275)

## [0.9.37] - 2024-01-24

### New Features

- Added a RAG CLI utility (#10193)
- Added a textai vector store (#10240)
- Added a Postgresql based docstore and index store (#10233)
- specify tool spec in tool specs (#10263)

### Bug Fixes / Nits

- Fixed serialization error in ollama chat (#10230)
- Added missing fields to `SentenceTransformerRerank` (#10225)
- Fixed title extraction (#10209, #10226)
- nit: make chainable output parser more exposed in library/docs (#10262)
- :bug: summary index not carrying over excluded metadata keys (#10259)

## [0.9.36] - 2024-01-23

### New Features

- Added support for `SageMakerEmbedding` (#10207)

### Bug Fixes / Nits

- Fix duplicated `file_id` on openai assistant (#10223)
- Fix circular dependencies for programs (#10222)
- Run `TitleExtractor` on groups of nodes from the same parent document (#10209)
- Improve vectara auto-retrieval (#10195)

## [0.9.35] - 2024-01-22

### New Features

- `beautifulsoup4` dependency to new optional extra `html` (#10156)
- make `BaseNode.hash` an `@property` (#10163)
- Neutrino (#10150)
- feat: JSONalyze Query Engine (#10067)
- [wip] add custom hybrid retriever notebook (#10164)
- add from_collection method to ChromaVectorStore class (#10167)
- CLI experiment v0: ask (#10168)
- make react agent prompts more editable (#10154)
- Add agent query pipeline (#10180)

### Bug Fixes / Nits

- Update supabase vecs metadata filter function to support multiple fields (#10133)
- Bugfix/code improvement for LanceDB integration (#10144)
- `beautifulsoup4` optional dependency (#10156)
- Fix qdrant aquery hybrid search (#10159)
- make hash a @property (#10163)
- fix: bug on poetry install of llama-index[postgres] (#10171)
- [doc] update jaguar vector store documentation (#10179)
- Remove use of not-launched finish_message (#10188)
- Updates to Lantern vector stores docs (#10192)
- fix typo in multi_document_agents.ipynb (#10196)

## [0.9.34] - 2024-01-19

### New Features

- Added SageMakerEndpointLLM (#10140)
- Added support for Qdrant filters (#10136)

### Bug Fixes / Nits

- Update bedrock utils for Claude 2:1 (#10139)
- BugFix: deadlocks using multiprocessing (#10125)

## [0.9.33] - 2024-01-17

### New Features

- Added RankGPT as a postprocessor (#10054)
- Ensure backwards compatibility with new Pinecone client version bifucation (#9995)
- Recursive retriever all the things (#10019)

### Bug Fixes / Nits

- BugFix: When using markdown element parser on a table containing comma (#9926)
- extend auto-retrieval notebook (#10065)
- Updated the Attribute name in llm_generators (#10070)
- jaguar vector store add text_tag to add_kwargs in add() (#10057)

## [0.9.32] - 2024-01-16

### New Features

- added query-time row retrieval + fix nits with query pipeline over structured data (#10061)
- ReActive Agents w/ Context + updated stale link (#10058)

## [0.9.31] - 2024-01-15

### New Features

- Added selectors and routers to query pipeline (#9979)
- Added sparse-only search to qdrant vector store (#10041)
- Added Tonic evaluators (#10000)
- Adding async support to firestore docstore (#9983)
- Implement mongodb docstore `put_all` method (#10014)

### Bug Fixes / Nits

- Properly truncate sql results based on `max_string_length` (#10015)
- Fixed `node.resolve_image()` for base64 strings (#10026)
- Fixed cohere system prompt role (#10020)
- Remove redundant token counting operation in SentenceSplitter (#10053)

## [0.9.30] - 2024-01-11

### New Features

- Implements a Node Parser using embeddings for Semantic Splitting (#9988)
- Add Anyscale Embedding model support (#9470)

### Bug Fixes / Nits

- nit: fix pandas get prompt (#10001)
- Fix: Token counting bug (#9912)
- Bump jinja2 from 3.1.2 to 3.1.3 (#9997)
- Fix corner case for qdrant hybrid search (#9993)
- Bugfix: sphinx generation errors (#9944)
- Fix: `language` used before assignment in `CodeSplitter` (#9987)
- fix inconsistent name "text_parser" in section "Use a Text Splitter… (#9980)
- :bug: fixing batch size (#9982)
- add auto-async execution to query pipelines (#9967)
- :bug: fixing init (#9977)
- Parallel Loading with SimpleDirectoryReader (#9965)
- do not force delete an index in milvus (#9974)

## [0.9.29] - 2024-01-10

### New Features

- Added support for together.ai models (#9962)
- Added support for batch redis/firestore kvstores, async firestore kvstore (#9827)
- Parallelize `IngestionPipeline.run()` (#9920)
- Added new query pipeline components: function, argpack, kwargpack (#9952)

### Bug Fixes / Nits

- Updated optional langchain imports to avoid warnings (#9964)
- Raise an error if empty nodes are embedded (#9953)

## [0.9.28] - 2024-01-09

### New Features

- Added support for Nvidia TenorRT LLM (#9842)
- Allow `tool_choice` to be set during agent construction (#9924)
- Added streaming support for `QueryPipeline` (#9919)

### Bug Fixes / Nits

- Set consistent doc-ids for llama-index readers (#9923, #9916)
- Remove unneeded model inputs for HuggingFaceEmbedding (#9922)
- Propagate `tool_choice` flag to downstream APIs (#9901)
- Add `chat_store_key` to chat memory `from_defaults()` (#9928)

## [0.9.27] - 2024-01-08

### New Features

- add query pipeline (#9908)
- Feature: Azure Multi Modal (fixes: #9471) (#9843)
- add postgres docker (#9906)
- Vectara auto_retriever (#9865)
- Redis Chat Store support (#9880)
- move more classes to core (#9871)

### Bug Fixes / Nits / Smaller Features

- Propagate `tool_choice` flag to downstream APIs (#9901)
- filter out negative indexes from faiss query (#9907)
- added NE filter for qdrant payloads (#9897)
- Fix incorrect id assignment in MyScale query result (#9900)
- Qdrant Text Match Filter (#9895)
- Fusion top k for hybrid search (#9894)
- Fix (#9867) sync_to_async to avoid blocking during asynchronous calls (#9869)
- A single node passed into compute_scores returns as a float (#9866)
- Remove extra linting steps (#9878)
- add vectara links (#9886)

## [0.9.26] - 2024-01-05

### New Features

- Added a `BaseChatStore` and `SimpleChatStore` abstraction for dedicated chat memory storage (#9863)
- Enable custom `tree_sitter` parser to be passed into `CodeSplitter` (#9845)
- Created a `BaseAutoRetriever` base class, to allow other retrievers to extend to auto modes (#9846)
- Added support for Nvidia Triton LLM (#9488)
- Added `DeepEval` one-click observability (#9801)

### Bug Fixes / Nits

- Updated the guidance integration to work with the latest version (#9830)
- Made text storage optional for doctores/ingestion pipeline (#9847)
- Added missing `sphinx-automodapi` dependency for docs (#9852)
- Return actual node ids in weaviate query results (#9854)
- Added prompt formatting to LangChainLLM (#9844)

## [0.9.25] - 2024-01-03

### New Features

- Added concurrancy limits for dataset generation (#9779)
- New `deepeval` one-click observability handler (#9801)
- Added jaguar vector store (#9754)
- Add beta multimodal ReAct agent (#9807)

### Bug Fixes / Nits

- Changed default batch size for OpenAI embeddings to 100 (#9805)
- Use batch size properly for qdrant upserts (#9814)
- `_verify_source_safety` uses AST, not regexes, for proper safety checks (#9789)
- use provided LLM in element node parsers (#9776)
- updated legacy vectordb loading function to be more robust (#9773)
- Use provided http client in AzureOpenAI (#9772)

## [0.9.24] - 2023-12-30

### New Features

- Add reranker for BEIR evaluation (#9743)
- Add Pathway integration. (#9719)
- custom agents implementation + notebook (#9746)

### Bug Fixes / Nits

- fix beam search for vllm: add missing parameter (#9741)
- Fix alpha for hrbrid search (#9742)
- fix token counter (#9744)
- BM25 tokenizer lowercase (#9745)

## [0.9.23] - 2023-12-28

### Bug Fixes / Nits

- docs: fixes qdrant_hybrid.ipynb typos (#9729)
- make llm completion program more general (#9731)
- Refactor MM Vector store and Index for empty collection (#9717)
- Adding IF statement to check for Schema using "Select" (#9712)
- allow skipping module loading in `download_module` and `download_llama_pack` (#9734)

## [0.9.22] - 2023-12-26

### New Features

- Added `.iter_data()` method to `SimpleDirectoryReader` (#9658)
- Added async support to `Ollama` LLM (#9689)
- Expanding pinecone filter support for `in` and `not in` (#9683)

### Bug Fixes / Nits

- Improve BM25Retriever performance (#9675)
- Improved qdrant hybrid search error handling (#9707)
- Fixed `None` handling in `ChromaVectorStore` (#9697)
- Fixed postgres schema creation if not existing (#9712)

## [0.9.21] - 2023-12-23

### New Features

- Added zilliz cloud as a managed index (#9605)

### Bug Fixes / Nits

- Bedrock client and LLM fixes (#9671, #9646)

## [0.9.20] - 2023-12-21

### New Features

- Added `insert_batch_size` to limit number of embeddings held in memory when creating an index, defaults to 2048 (#9630)
- Improve auto-retrieval (#9647)
- Configurable Node ID Generating Function (#9574)
- Introduced action input parser (#9575)
- qdrant sparse vector support (#9644)
- Introduced upserts and delete in ingestion pipeline (#9643)
- Add Zilliz Cloud Pipeline as a Managed Index (#9605)
- Add support for Google Gemini models via VertexAI (#9624)
- support allowing additional metadata filters on autoretriever (#9662)

### Bug Fixes / Nits

- Fix pip install commands in LM Format Enforcer notebooks (#9648)
- Fixing some more links and documentations (#9633)
- some bedrock nits and fixes (#9646)

## [0.9.19] - 2023-12-20

### New Features

- new llama datasets `LabelledEvaluatorDataset` & `LabelledPairwiseEvaluatorDataset` (#9531)

## [0.9.18] - 2023-12-20

### New Features

- multi-doc auto-retrieval guide (#9631)

### Bug Fixes / Nits

- fix(vllm): make Vllm's 'complete' method behave the same as other LLM class (#9634)
- FIx Doc links and other documentation issue (#9632)

## [0.9.17] - 2023-12-19

### New Features

- [example] adding user feedback (#9601)
- FEATURE: Cohere ReRank Relevancy Metric for Retrieval Eval (#9495)

### Bug Fixes / Nits

- Fix Gemini Chat Mode (#9599)
- Fixed `types-protobuf` from being a primary dependency (#9595)
- Adding an optional auth token to the TextEmbeddingInference class (#9606)
- fix: out of index get latest tool call (#9608)
- fix(azure_openai.py): add missing return to subclass override (#9598)
- fix mix up b/w 'formatted' and 'format' params for ollama api call (#9594)

## [0.9.16] - 2023-12-18

### New Features

- agent refactor: step-wise execution (#9584)
- Add OpenRouter, with Mixtral demo (#9464)
- Add hybrid search to neo4j vector store (#9530)
- Add support for auth service accounts for Google Semantic Retriever (#9545)

### Bug Fixes / Nits

- Fixed missing `default=None` for `LLM.system_prompt` (#9504)
- Fix #9580 : Incorporate metadata properly (#9582)
- Integrations: Gradient[Embeddings,LLM] - sdk-upgrade (#9528)
- Add mixtral 8x7b model to anyscale available models (#9573)
- Gemini Model Checks (#9563)
- Update OpenAI fine-tuning with latest changes (#9564)
- fix/Reintroduce `WHERE` filter to the Sparse Query for PgVectorStore (#9529)
- Update Ollama API to ollama v0.1.16 (#9558)
- ollama: strip invalid `formatted` option (#9555)
- add a device in optimum push #9541 (#9554)
- Title vs content difference for Gemini Embedding (#9547)
- fix pydantic fields to float (#9542)

## [0.9.15] - 2023-12-13

### New Features

- Added full support for Google Gemini text+vision models (#9452)
- Added new Google Semantic Retriever (#9440)
- added `from_existing()` method + async support to OpenAI assistants (#9367)

### Bug Fixes / Nits

- Fixed huggingface LLM system prompt and messages to prompt (#9463)
- Fixed ollama additional kwargs usage (#9455)

## [0.9.14] - 2023-12-11

### New Features

- Add MistralAI LLM (#9444)
- Add MistralAI Embeddings (#9441)
- Add `Ollama` Embedding class (#9341)
- Add `FlagEmbeddingReranker` for reranking (#9285)
- feat: PgVectorStore support advanced metadata filtering (#9377)
- Added `sql_only` parameter to SQL query engines to avoid executing SQL (#9422)

### Bug Fixes / Nits

- Feat/PgVector Support custom hnsw.ef_search and ivfflat.probes (#9420)
- fix F1 score definition, update copyright year (#9424)
- Change more than one image input for Replicate Multi-modal models from error to warning (#9360)
- Removed GPT-Licensed `aiostream` dependency (#9403)
- Fix result of BedrockEmbedding with Cohere model (#9396)
- Only capture valid tool names in react agent (#9412)
- Fixed `top_k` being multiplied by 10 in azure cosmos (#9438)
- Fixed hybrid search for OpenSearch (#9430)

### Breaking Changes

- Updated the base `LLM` interface to match `LLMPredictor` (#9388)
- Deprecated `LLMPredictor` (#9388)

## [0.9.13] - 2023-12-06

### New Features

- Added batch prediction support for `LabelledRagDataset` (#9332)

### Bug Fixes / Nits

- Fixed save and load for faiss vector store (#9330)

## [0.9.12] - 2023-12-05

### New Features

- Added an option `reuse_client` to openai/azure to help with async timeouts. Set to `False` to see improvements (#9301)
- Added support for `vLLM` llm (#9257)
- Add support for python 3.12 (#9304)
- Support for `claude-2.1` model name (#9275)

### Bug Fixes / Nits

- Fix embedding format for bedrock cohere embeddings (#9265)
- Use `delete_kwargs` for filtering in weaviate vector store (#9300)
- Fixed automatic qdrant client construction (#9267)

## [0.9.11] - 2023-12-03

### New Features

- Make `reference_contexts` optional in `LabelledRagDataset` (#9266)
- Re-organize `download` module (#9253)
- Added document management to ingestion pipeline (#9135)
- Add docs for `LabelledRagDataset` (#9228)
- Add submission template notebook and other doc updates for `LabelledRagDataset` (#9273)

### Bug Fixes / Nits

- Convert numpy to list for `InstructorEmbedding` (#9255)

## [0.9.10] - 2023-11-30

### New Features

- Advanced Metadata filter for vector stores (#9216)
- Amazon Bedrock Embeddings New models (#9222)
- Added PromptLayer callback integration (#9190)
- Reuse file ids for `OpenAIAssistant` (#9125)

### Breaking Changes / Deprecations

- Deprecate ExactMatchFilter (#9216)

## [0.9.9] - 2023-11-29

### New Features

- Add new abstractions for `LlamaDataset`'s (#9165)
- Add metadata filtering and MMR mode support for `AstraDBVectorStore` (#9193)
- Allowing newest `scikit-learn` versions (#9213)

### Breaking Changes / Deprecations

- Added `LocalAI` demo and began deprecation cycle (#9151)
- Deprecate `QueryResponseDataset` and `DatasetGenerator` of `evaluation` module (#9165)

### Bug Fixes / Nits

- Fix bug in `download_utils.py` with pointing to wrong repo (#9215)
- Use `azure_deployment` kwarg in `AzureOpenAILLM` (#9174)
- Fix similarity score return for `AstraDBVectorStore` Integration (#9193)

## [0.9.8] - 2023-11-26

### New Features

- Add `persist` and `persist_from_dir` methods to `ObjectIndex` that are able to support it (#9064)
- Added async metadata extraction + pipeline support (#9121)
- Added back support for start/end char idx in nodes (#9143)

### Bug Fixes / Nits

- Fix for some kwargs not being set properly in global service context (#9137)
- Small fix for `memory.get()` when system/prefix messages are large (#9149)
- Minor fixes for global service context (#9137)

## [0.9.7] - 2023-11-24

### New Features

- Add support for `PGVectoRsStore` (#9087)
- Enforcing `requests>=2.31` for security, while unpinning `urllib3` (#9108)

### Bug Fixes / Nits

- Increased default memory token limit for context chat engine (#9123)
- Added system prompt to `CondensePlusContextChatEngine` that gets prepended to the `context_prompt` (#9123)
- Fixed bug in `CondensePlusContextChatEngine` not using chat history properly (#9129)

## [0.9.6] - 2023-11-22

### New Features

- Added `default_headers` argument to openai LLMs (#9090)
- Added support for `download_llama_pack()` and LlamaPack integrations
- Added support for `llamaindex-cli` command line tool

### Bug Fixed / Nits

- store normalize as bool for huggingface embedding (#9089)

## [0.9.5] - 2023-11-21

### Bug Fixes / Nits

- Fixed bug with AzureOpenAI logic for inferring if stream chunk is a tool call (#9018)

### New Features

- `FastEmbed` embeddings provider (#9043)
- More precise testing of `OpenAILike` (#9026)
- Added callback manager to each retriever (#8871)
- Ability to bypass `max_tokens` inference with `OpenAILike` (#9032)

### Bug Fixes / Nits

- Fixed bug in formatting chat prompt templates when estimating chunk sizes (#9025)
- Sandboxed Pandas execution, remediate CVE-2023-39662 (#8890)
- Restored `mypy` for Python 3.8 (#9031)
- Loosened `dataclasses-json` version range,
  and removes unnecessary `jinja2` extra from `pandas` (#9042)

## [0.9.4] - 2023-11-19

### New Features

- Added `CondensePlusContextChatEngine` (#8949)

### Smaller Features / Bug Fixes / Nits

- Fixed bug with `OpenAIAgent` inserting errors into chat history (#9000)
- Fixed various bugs with LiteLLM and the new OpenAI client (#9003)
- Added context window attribute to perplexity llm (#9012)
- Add `node_parser` attribute back to service context (#9013)
- Refactor MM retriever classes (#8998)
- Fix TextNode instantiation on SupabaseVectorIndexDemo (#8994)

## [0.9.3] - 2023-11-17

### New Features

- Add perplexity LLM integration (#8734)

### Bug Fixes / Nits

- Fix token counting for new openai client (#8981)
- Fix small pydantic bug in postgres vector db (#8962)
- Fixed `chunk_overlap` and `doc_id` bugs in `HierarchicalNodeParser` (#8983)

## [0.9.2] - 2023-11-16

### New Features

- Added new notebook guide for Multi-Modal Rag Evaluation (#8945)
- Added `MultiModalRelevancyEvaluator`, and `MultiModalFaithfulnessEvaluator` (#8945)

## [0.9.1] - 2023-11-15

### New Features

- Added Cohere Reranker fine-tuning (#8859)
- Support for custom httpx client in `AzureOpenAI` LLM (#8920)

### Bug Fixes / Nits

- Fixed issue with `set_global_service_context` not propagating settings (#8940)
- Fixed issue with building index with Google Palm embeddings (#8936)
- Fixed small issue with parsing ImageDocuments/Nodes that have no text (#8938)
- Fixed issue with large data inserts in Astra DB (#8937)
- Optimize `QueryEngineTool` for agents (#8933)

## [0.9.0] - 2023-11-15

### New Features / Breaking Changes / Deprecations

- New `IngestionPipeline` concept for ingesting and transforming data
- Data ingestion and transforms are now automatically cached
- Updated interface for node parsing/text splitting/metadata extraction modules
- Changes to the default tokenizer, as well as customizing the tokenizer
- Packaging/Installation changes with PyPi (reduced bloat, new install options)
- More predictable and consistent import paths
- Plus, in beta: MultiModal RAG Modules for handling text and images!
- Find more details at: `https://medium.com/@llama_index/719f03282945`

## [0.8.69.post1] - 2023-11-13

### Bug Fixes / Nits

- Increase max weaivate delete size to max of 10,000 (#8887)
- Final pickling remnant fix (#8902)

## [0.8.69] - 2023-11-13

### Bug Fixes / Nits

- Fixed bug in loading pickled objects (#8880)
- Fix `custom_path` vs `custom_dir` in `download_loader` (#8865)

## [0.8.68] - 2023-11-11

### New Features

- openai assistant agent + advanced retrieval cookbook (#8863)
- add retrieval API benchmark (#8850)
- Add JinaEmbedding class (#8704)

### Bug Fixes / Nits

- Improved default timeouts/retries for OpenAI (#8819)
- Add back key validation for OpenAI (#8819)
- Disable automatic LLM/Embedding model downloads, give informative error (#8819)
- fix openai assistant tool creation + retrieval notebook (#8862)
- Quick fix Replicate MultiModal example (#8861)
- fix: paths treated as hidden (#8860)
- fix Replicate multi-modal LLM + notebook (#8854)
- Feature/citation metadata (#8722)
- Fix ImageNode type from NodeWithScore for SimpleMultiModalQueryEngine (#8844)

## [0.8.67] - 2023-11-10

### New Features

- Advanced Multi Modal Retrieval Example and docs (#8822, #8823)

### Bug Fixes / Nits

- Fix retriever node postprocessors for `CitationQueryEngine` (#8818)
- Fix `cannot pickle 'builtins.CoreBPE' object` in most scenarios (#8835)

## [0.8.66] - 2023-11-09

### New Features

- Support parallel function calling with new OpenAI client in `OpenAIPydanticProgram` (#8793)

### Bug Fixes / Nits

- Fix bug in pydantic programs with new OpenAI client (#8793)
- Fixed bug with un-listable fsspec objects (#8795)

## [0.8.65] - 2023-11-08

### New Features

- `OpenAIAgent` parallel function calling (#8738)

### New Features

- Properly supporting Hugging Face recommended model (#8784)

### Bug Fixes / Nits

- Fixed missing import for `embeddings.__all__` (#8779)

### Breaking Changes / Deprecations

- Use `tool_choice` over `function_call` and `tool` over `functions` in `OpenAI(LLM)` (#8738)
- Deprecate `to_openai_function` in favor of `to_openai_tool` (#8738)

## [0.8.64] - 2023-11-06

### New Features

- `OpenAIAgent` parallel function calling (#8738)
- Add AI assistant agent (#8735)
- OpenAI GPT4v Abstraction (#8719)
- Add support for `Lantern` VectorStore (#8714)

### Bug Fixes / Nits

- Fix returning zero nodes in elastic search vector store (#8746)
- Add try/except for `SimpleDirectoryReader` loop to avoid crashing on a single document (#8744)
- Fix for `deployment_name` in async embeddings (#8748)

## [0.8.63] - 2023-11-05

### New Features

- added native sync and async client support for the lasted `openai` client package (#8712)
- added support for `AzureOpenAIEmbedding` (#8712)

### Bug Fixes / Nits

- Fixed errors about "no host supplied" with `download_loader` (#8723)

### Breaking Changes

- `OpenAIEmbedding` no longer supports azure, moved into the `AzureOpenAIEmbedding` class (#8712)

## [0.8.62.post1] - 2023-11-05

### Breaking Changes

- add new devday models (#8713)
- moved `max_docs` parameter from constructor to `lazy_load_data()` for `SimpleMongoReader` (#8686)

## [0.8.61] - 2023-11-05

### New Features

- [experimental] Hyperparameter tuner (#8687)

### Bug Fixes / Nits

- Fix typo error in CohereAIModelName class: cohere light models was missing v3 (#8684)
- Update deeplake.py (#8683)

## [0.8.60] - 2023-11-04

### New Features

- prompt optimization guide (#8659)
- VoyageEmbedding (#8634)
- Multilingual support for `YoutubeTranscriptReader` (#8673)
- emotion prompt guide (#8674)

### Bug Fixes / Nits

- Adds mistral 7b instruct v0.1 to available anyscale models (#8652)
- Make pgvector's setup (extension, schema, and table creation) optional (#8656)
- Allow init of stores_text variable for Pinecone vector store (#8633)
- fix: azure ad support (#8667)
- Fix nltk bug in multi-threaded environments (#8668)
- Fix google colab link in cohereai notebook (#8677)
- passing max_tokens to the `Cohere` llm (#8672)

## [0.8.59] - 2023-11-02

- Deepmemory support (#8625)
- Add CohereAI embeddings (#8650)
- Add Azure AD (Microsoft Entra ID) support (#8667)

## [0.8.58] - 2023-11-02

### New Features

- Add `lm-format-enforcer` integration for structured output (#8601)
- Google Vertex Support (#8626)

## [0.8.57] - 2023-10-31

### New Features

- Add `VoyageAIEmbedding` integration (#8634)
- Add fine-tuning evaluator notebooks (#8596)
- Add `SingleStoreDB` integration (#7991)
- Add support for ChromaDB PersistentClient (#8582)
- Add DataStax Astra DB support (#8609)

### Bug Fixes / Nits

- Update dataType in Weaviate (#8608)
- In Knowledge Graph Index with hybrid retriever_mode,
  - return the nodes found by keyword search when 'No Relationship found'
- Fix exceed context length error in chat engines (#8530)
- Retrieve actual content of all the triplets from KG (#8579)
- Return the nodes found by Keywords when no relationship is found by embeddings in hybrid retriever_mode in `KnowledgeGraphIndex` (#8575)
- Optimize content of retriever tool and minor bug fix (#8588)

## [0.8.56] - 2023-10-30

### New Features

- Add Amazon `BedrockEmbedding` (#8550)
- Moves `HuggingFaceEmbedding` to center on `Pooling` enum for pooling (#8467)
- Add IBM WatsonX LLM support (#8587)

### Bug Fixes / Nits

- [Bug] Patch Clarifai classes (#8529)
- fix retries for bedrock llm (#8528)
- Fix : VectorStore’s QueryResult always returns saved Node as TextNode (#8521)
- Added default file_metadata to get basic metadata that many postprocessors use, for SimpleDirectoryReader (#8486)
- Handle metadata with None values in chromadb (#8584)

## [0.8.55] - 2023-10-29

### New Features

- allow prompts to take in functions with `function_mappings` (#8548)
- add advanced prompt + "prompt engineering for RAG" notebook (#8555)
- Leverage Replicate API for serving LLaVa modal (#8539)

### Bug Fixes / Nits

- Update pull request template with google colab support inclusion (#8525)

## [0.8.54] - 2023-10-28

### New Features

- notebook showing how to fine-tune llama2 on structured outputs (#8540)
  - added GradientAIFineTuningHandler
  - added pydantic_program_mode to ServiceContext
- Initialize MultiModal Retrieval using LlamaIndex (#8507)

### Bug Fixes / Nits

- Add missing import to `ChatEngine` usage pattern `.md` doc (#8518)
- :bug: fixed async add (#8531)
- fix: add the needed CondenseQuestionChatEngine import in the usage_pa… (#8518)
- Add import LongLLMLinguaPostprocessor for LongLLMLingua.ipynb (#8519)

## [0.8.53] - 2023-10-27

### New Features

- Docs refactor (#8500)
  An overhaul of the docs organization. Major changes
  - Added a big new "understanding" section
  - Added a big new "optimizing" section
  - Overhauled Getting Started content
  - Categorized and moved module guides to a single section

## [0.8.52] - 2023-10-26

### New Features

- Add longllmlingua (#8485)
- Add google colab support for notebooks (#7560)

### Bug Fixes / Nits

- Adapt Cassandra VectorStore constructor DB connection through cassio.init (#8255)
- Allow configuration of service context and storage context in managed index (#8487)

## [0.8.51.post1] - 2023-10-25

### New Features

- Add Llava MultiModal QA examples for Tesla 10k RAG (#8271)
- fix bug streaming on react chat agent not working as expected (#8459)

### Bug Fixes / Nits

- patch: add selected result to response metadata for router query engines, fix bug (#8483)
- add Jina AI embeddings notebook + huggingface embedding fix (#8478)
- add `is_chat_model` to replicate (#8469)
- Brought back `toml-sort` to `pre-commit` (#8267)
- Added `LocationConstraint` for local `test_s3_kvstore` (#8263)

## [0.8.50] - 2023-10-24

### New Features

- Expose prompts in different modules (query engines, synthesizers, and more) (#8275)

## [0.8.49] - 2023-10-23

### New Features

- New LLM integrations
  - Support for Hugging Face Inference API's `conversational`, `text_generation`,
    and `feature_extraction` endpoints via `huggingface_hub[inference]` (#8098)
  - Add Amazon Bedrock LLMs (#8223)
  - Add AI21 Labs LLMs (#8233)
  - Add OpenAILike LLM class for OpenAI-compatible api servers (#7973)
- New / updated vector store integrations
  - Add DashVector (#7772)
  - Add Tencent VectorDB (#8173)
  - Add option for custom Postgres schema on PGVectorStore instead of only allowing public schema (#8080)
- Add Gradient fine tuning engine (#8208)
- docs(FAQ): frequently asked questions (#8249)

### Bug Fixes / Nits

- Fix inconsistencies with `ReActAgent.stream_chat` (#8147)
- Deprecate some functions for GuardrailsOutputParser (#8016)
- Simplify dependencies (#8236)
- Bug fixes for LiteLLM (#7885)
- Update for Predibase LLM (#8211)

## [0.8.48] - 2023-10-20

### New Features

- Add `DELETE` for MyScale vector store (#8159)
- Add SQL Retriever (#8197)
- add semantic kernel document format (#8226)
- Improve MyScale Hybrid Search and Add `DELETE` for MyScale vector store (#8159)

### Bug Fixes / Nits

- Fixed additional kwargs in ReActAgent.from_tools() (#8206)
- Fixed missing spaces in prompt templates (#8190)
- Remove auto-download of llama2-13B on exception (#8225)

## [0.8.47] - 2023-10-19

### New Features

- add response synthesis to text-to-SQL (#8196)
- Added support for `LLMRailsEmbedding` (#8169)
- Inferring MPS device with PyTorch (#8195)
- Consolidated query/text prepending (#8189)

## [0.8.46] - 2023-10-18

### New Features

- Add fine-tuning router support + embedding selector (#8174)
- add more document converters (#8156)

### Bug Fixes / Nits

- Add normalization to huggingface embeddings (#8145)
- Improve MyScale Hybrid Search (#8159)
- Fixed duplicate `FORMAT_STR` being inside prompt (#8171)
- Added: support for output_kwargs={'max_colwidth': xx} for PandasQueryEngine (#8110)
- Minor fix in the description for an argument in cohere llm (#8163)
- Fix Firestore client info (#8166)

## [0.8.45] - 2023-10-13

### New Features

- Added support for fine-tuning cross encoders (#7705)
- Added `QueryFusionRetriever` for merging multiple retrievers + query augmentation (#8100)
- Added `nb-clean` to `pre-commit` to minimize PR diffs (#8108)
- Support for `TextEmbeddingInference` embeddings (#8122)

### Bug Fixes / Nits

- Improved the `BM25Retriever` interface to accept `BaseNode` objects (#8096)
- Fixed bug with `BM25Retriever` tokenizer not working as expected (#8096)
- Brought mypy to pass in Python 3.8 (#8107)
- `ReActAgent` adding missing `super().__init__` call (#8125)

## [0.8.44] - 2023-10-12

### New Features

- add pgvector sql query engine (#8087)
- Added HoneyHive one-click observability (#7944)
- Add support for both SQLAlchemy V1 and V2 (#8060)

## [0.8.43.post1] - 2023-10-11

### New Features

- Moves `codespell` to `pre-commit` (#8040)
- Added `prettier` for autoformatting extensions besides `.py` (#8072)

### Bug Fixes / Nits

- Fixed forgotten f-str in `HuggingFaceLLM` (#8075)
- Relaxed numpy/panadas reqs

## [0.8.43] - 2023-10-10

### New Features

- Added support for `GradientEmbedding` embed models (#8050)

### Bug Fixes / Nits

- added `messages_to_prompt` kwarg to `HuggingFaceLLM` (#8054)
- improved selection and sql parsing for open-source models (#8054)
- fixed bug when agents hallucinate too many kwargs for a tool (#8054)
- improved prompts and debugging for selection+question generation (#8056)

## [0.8.42] - 2023-10-10

### New Features

- `LocalAI` more intuitive module-level var names (#8028)
- Enable `codespell` for markdown docs (#7972)
- add unstructured table element node parser (#8036)
- Add: Async upserting for Qdrant vector store (#7968)
- Add cohere llm (#8023)

### Bug Fixes / Nits

- Parse multi-line outputs in react agent answers (#8029)
- Add properly named kwargs to keyword `as_retriever` calls (#8011)
- Updating Reference to RAGAS LlamaIndex Integration (#8035)
- Vectara bugfix (#8032)
- Fix: ChromaVectorStore can attempt to add in excess of chromadb batch… (#8019)
- Fix get_content method in Mbox reader (#8012)
- Apply kwarg filters in WeaviateVectorStore (#8017)
- Avoid ZeroDivisionError (#8027)
- `LocalAI` intuitive module-level var names (#8028)
- zep/fix: imports & typing (#8030)
- refactor: use `str.join` (#8020)
- use proper metadata str for node parsing (#7987)

## [0.8.41] - 2023-10-07

### New Features

- You.com retriever (#8024)
- Pull fields from mongodb into metadata with `metadata_names` argument (#8001)
- Simplified `LocalAI.__init__` preserving the same behaviors (#7982)

### Bug Fixes / Nits

- Use longest metadata string for metadata aware text splitting (#7987)
- Handle lists of strings in mongodb reader (#8002)
- Removes `OpenAI.class_type` as it was dead code (#7983)
- Fixing `HuggingFaceLLM.device_map` type hint (#7989)

## [0.8.40] - 2023-10-05

### New Features

- Added support for `Clarifai` LLM (#7967)
- Add support for function fine-tuning (#7971)

### Breaking Changes

- Update document summary index (#7815)
  - change default retrieval mode to embedding
  - embed summaries into vector store by default at indexing time (instead of calculating embedding on the fly)
  - support configuring top k in llm retriever

## [0.8.39] - 2023-10-03

### New Features

- Added support for pydantic object outputs with query engines (#7893)
- `ClarifaiEmbedding` class added for embedding support (#7940)
- Markdown node parser, flat file reader and simple file node parser (#7863)
- Added support for mongdb atlas `$vectorSearch` (#7866)

### Bug Fixes / Nits

- Adds support for using message metadata in discord reader (#7906)
- Fix `LocalAI` chat capability without `max_tokens` (#7942)
- Added `codespell` for automated checking (#7941)
- `ruff` modernization and autofixes (#7889)
- Implement own SQLDatabase class (#7929)
- Update LlamaCPP context_params property (#7945)
- fix duplicate embedding (#7949)
- Adds `codespell` tool for enforcing good spelling (#7941)
- Supporting `mypy` local usage with `venv` (#7952)
- Vectara - minor update (#7954)
- Avoiding `pydantic` reinstalls in CI (#7956)
- move tree_sitter_languages into data_requirements.txt (#7955)
- Add `cache_okay` param to `PGVectorStore` to help suppress TSVector warnings (#7950)

## [0.8.38] - 2023-10-02

### New Features

- Updated `KeywordNodePostprocessor` to use spacy to support more languages (#7894)
- `LocalAI` supporting global or per-query `/chat/completions` vs `/completions` (#7921)
- Added notebook on using REBEL + Wikipedia filtering for knowledge graphs (#7919)
- Added support for `ElasticsearchEmbedding` (#7914)

## [0.8.37] - 2023-09-30

### New Features

- Supporting `LocalAI` LLMs (#7913)
- Validations protecting against misconfigured chunk sizes (#7917)

### Bug Fixes / Nits

- Simplify NL SQL response to SQL parsing, with expanded NL SQL prompt (#7868)
- Improve vector store retrieval speed for vectordb integrations (#7876)
- Added replacing {{ and }}, and fixed JSON parsing recursion (#7888)
- Nice-ified JSON decoding error (#7891)
- Nice-ified SQL error from LLM not providing SQL (#7900)
- Nice-ified `ImportError` for `HuggingFaceLLM` (#7904)
- eval fixes: fix dataset response generation, add score to evaluators (#7915)

## [0.8.36] - 2023-09-27

### New Features

- add "build RAG from scratch notebook" - OSS/local (#7864)

### Bug Fixes / Nits

- Fix elasticsearch hybrid scoring (#7852)
- Replace `get_color_mapping` and `print_text` Langchain dependency with internal implementation (#7845)
- Fix async streaming with azure (#7856)
- Avoid `NotImplementedError()` in sub question generator (#7855)
- Patch predibase initialization (#7859)
- Bumped min langchain version and changed prompt imports from langchain (#7862)

## [0.8.35] - 2023-09-27

### Bug Fixes / Nits

- Fix dropping textnodes in recursive retriever (#7840)
- share callback_manager between agent and its llm when callback_manager is None (#7844)
- fix pandas query engine (#7847)

## [0.8.34] - 2023-09-26

### New Features

- Added `Konko` LLM support (#7775)
- Add before/after context sentence (#7821)
- EverlyAI integration with LlamaIndex through OpenAI library (#7820)
- add Arize Phoenix tracer to global handlers (#7835)

### Bug Fixes / Nits

- Normalize scores returned from ElasticSearch vector store (#7792)
- Fixed `refresh_ref_docs()` bug with order of operations (#7664)
- Delay postgresql connection for `PGVectorStore` until actually needed (#7793)
- Fix KeyError in delete method of `SimpleVectorStore` related to metadata filters (#7829)
- Fix KeyError in delete method of `SimpleVectorStore` related to metadata filters (#7831)
- Addressing PyYAML import error (#7784)
- ElasticsearchStore: Update User-Agent + Add example docker compose (#7832)
- `StorageContext.persist` supporting `Path` (#7783)
- Update ollama.py (#7839)
- fix bug for self.\_session_pool (#7834)

## [0.8.33] - 2023-09-25

### New Features

- add pairwise evaluator + benchmark auto-merging retriever (#7810)

### Bug Fixes / Nits

- Minor cleanup in embedding class (#7813)
- Misc updates to `OpenAIEmbedding` (#7811)

## [0.8.32] - 2023-09-24

### New Features

- Added native support for `HuggingFaceEmbedding`, `InstructorEmbedding`, and `OptimumEmbedding` (#7795)
- Added metadata filtering and hybrid search to MyScale vector store (#7780)
- Allowing custom text field name for Milvus (#7790)
- Add support for `vector_store_query_mode` to `VectorIndexAutoRetriever` (#7797)

### Bug Fixes / Nits

- Update `LanceDBVectorStore` to handle score and distance (#7754)
- Pass LLM to `memory_cls` in `CondenseQuestionChatEngine` (#7785)

## [0.8.31] - 2023-09-22

### New Features

- add pydantic metadata extractor (#7778)
- Allow users to set the embedding dimensions in azure cognitive vector store (#7734)
- Add semantic similarity evaluator (#7770)

### Bug Fixes / Nits

- 📝docs: Update Chatbot Tutorial and Notebook (#7767)
- Fixed response synthesizers with empty nodes (#7773)
- Fix `NotImplementedError` in auto vector retriever (#7764)
- Multiple kwargs values in "KnowledgeGraphQueryEngine" bug-fix (#7763)
- Allow setting azure cognitive search dimensionality (#7734)
- Pass service context to index for dataset generator (#7748)
- Fix output parsers for selector templates (#7774)
- Update Chatbot_SEC.ipynb (#7711)
- linter/typechecker-friendly improvements to cassandra test (#7771)
- Expose debug option of `PgVectorStore` (#7776)
- llms/openai: fix Azure OpenAI by considering `prompt_filter_results` field (#7755)

## [0.8.30] - 2023-09-21

### New Features

- Add support for `gpt-3.5-turbo-instruct` (#7729)
- Add support for `TimescaleVectorStore` (#7727)
- Added `LongContextReorder` for lost-in-the-middle issues (#7719)
- Add retrieval evals (#7738)

### Bug Fixes / Nits

- Added node post-processors to async context chat engine (#7731)
- Added unique index name for postgres tsv column (#7741)

## [0.8.29.post1] - 2023-09-18

### Bug Fixes / Nits

- Fix langchain import error for embeddings (#7714)

## [0.8.29] - 2023-09-18

### New Features

- Added metadata filtering to the base simple vector store (#7564)
- add low-level router guide (#7708)
- Add CustomQueryEngine class (#7703)

### Bug Fixes / Nits

- Fix context window metadata in lite-llm (#7696)

## [0.8.28] - 2023-09-16

### New Features

- Add CorrectnessEvaluator (#7661)
- Added support for `Ollama` LLMs (#7635)
- Added `HWPReader` (#7672)
- Simplified portkey LLM interface (#7669)
- Added async operation support to `ElasticsearchStore` vector store (#7613)
- Added support for `LiteLLM` (#7600)
- Added batch evaluation runner (#7692)

### Bug Fixes / Nits

- Avoid `NotImplementedError` for async langchain embeddings (#7668)
- Imrpoved reliability of LLM selectors (#7678)
- Fixed `query_wrapper_prompt` and `system_prompt` for output parsers and completion models (#7678)
- Fixed node attribute inheritance in citation query engine (#7675)

### Breaking Changes

- Refactor and update `BaseEvaluator` interface to be more consistent (#7661)
  - Use `evaluate` function for generic input
  - Use `evaluate_response` function with `Response` objects from llama index query engine
- Update existing evaluators with more explicit naming
  - `ResponseEvaluator` -> `FaithfulnessEvaluator`
  - `QueryResponseEvaluator` -> `RelevancyEvaluator`
  - old names are kept as class aliases for backwards compatibility

## [0.8.27] - 2023-09-14

### New Features

- add low-level tutorial section (#7673)

### Bug Fixes / Nits

- default delta should be a dict (#7665)
- better query wrapper logic on LLMPredictor (#7667)

## [0.8.26] - 2023-09-12

### New Features

- add non-linear embedding adapter (#7658)
- Add "finetune + RAG" evaluation to knowledge fine-tuning notebook (#7643)

### Bug Fixes / Nits

- Fixed chunk-overlap for sentence splitter (#7590)

## [0.8.25] - 2023-09-12

### New Features

- Added `AGENT_STEP` callback event type (#7652)

### Bug Fixes / Nits

- Allowed `simple` mode to work with `as_chat_engine()` (#7637)
- Fixed index error in azure streaming (#7646)
- Removed `pdb` from llama-cpp (#7651)

## [0.8.24] - 2023-09-11

## New Features

- guide: fine-tuning to memorize knowledge (#7626)
- added ability to customize prompt template for eval modules (#7626)

### Bug Fixes

- Properly detect `llama-cpp-python` version for loading the default GGML or GGUF `llama2-chat-13b` model (#7616)
- Pass in `summary_template` properly with `RetrieverQueryEngine.from_args()` (#7621)
- Fix span types in wandb callback (#7631)

## [0.8.23] - 2023-09-09

### Bug Fixes

- Make sure context and system prompt is included in prompt for first chat for llama2 (#7597)
- Avoid negative chunk size error in refine process (#7607)
- Fix relationships for small documents in hierarchical node parser (#7611)
- Update Anyscale Endpoints integration with full streaming and async support (#7602)
- Better support of passing credentials as LLM constructor args in `OpenAI`, `AzureOpenAI`, and `Anyscale` (#7602)

### Breaking Changes

- Update milvus vector store to support filters and dynamic schemas (#7286)
  - See the [updated notebook](https://docs.llamaindex.ai/en/stable/examples/vector_stores/MilvusIndexDemo.html) for usage
- Added NLTK to core dependencies to support the default sentence splitter (#7606)

## [0.8.22] - 2023-09-07

### New Features

- Added support for ElasticSearch Vector Store (#7543)

### Bug Fixes / Nits

- Fixed small `_index` bug in `ElasticSearchReader` (#7570)
- Fixed bug with prompt helper settings in global service contexts (#7576)
- Remove newlines from openai embeddings again (#7588)
- Fixed small bug with setting `query_wrapper_prompt` in the service context (#7585)

### Breaking/Deprecated API Changes

- Clean up vector store interface to use `BaseNode` instead of `NodeWithEmbedding`
  - For majority of users, this is a no-op change
  - For users directly operating with the `VectorStore` abstraction and manually constructing `NodeWithEmbedding` objects, this is a minor breaking change. Use `TextNode` with `embedding` set directly, instead of `NodeWithEmbedding`.

## [0.8.21] - 2023-09-06

### New Features

- add embedding adapter fine-tuning engine + guide (#7565)
- Added support for Azure Cognitive Search vector store (#7469)
- Support delete in supabase (#6951)
- Added support for Espilla vector store (#7539)
- Added support for AnyScale LLM (#7497)

### Bug Fixes / Nits

- Default to user-configurable top-k in `VectorIndexAutoRetriever` (#7556)
- Catch validation errors for structured responses (#7523)
- Fix streaming refine template (#7561)

## [0.8.20] - 2023-09-04

### New Features

- Added Portkey LLM integration (#7508)
- Support postgres/pgvector hybrid search (#7501)
- upgrade recursive retriever node reference notebook (#7537)

## [0.8.19] - 2023-09-03

### New Features

- replace list index with summary index (#7478)
- rename list index to summary index part 2 (#7531)

## [0.8.18] - 2023-09-03

### New Features

- add agent finetuning guide (#7526)

## [0.8.17] - 2023-09-02

### New Features

- Make (some) loaders serializable (#7498)
- add node references to recursive retrieval (#7522)

### Bug Fixes / Nits

- Raise informative error when metadata is too large during splitting (#7513)
- Allow langchain splitter in simple node parser (#7517)

## [0.8.16] - 2023-09-01

### Bug Fixes / Nits

- fix link to Marvin notebook in docs (#7504)
- Ensure metadata is not `None` in `SimpleWebPageReader` (#7499)
- Fixed KGIndex visualization (#7493)
- Improved empty response in KG Index (#7493)

## [0.8.15] - 2023-08-31

### New Features

- Added support for `MarvinEntityExtractor` metadata extractor (#7438)
- Added a url_metadata callback to SimpleWebPageReader (#7445)
- Expanded callback logging events (#7472)

### Bug Fixes / Nits

- Only convert newlines to spaces for text 001 embedding models in OpenAI (#7484)
- Fix `KnowledgeGraphRagRetriever` for non-nebula indexes (#7488)
- Support defined embedding dimension in `PGVectorStore` (#7491)
- Greatly improved similarity calculation speed for the base vector store (#7494)

## [0.8.14] - 2023-08-30

### New Features

- feat: non-kg heterogeneous graph support in Graph RAG (#7459)
- rag guide (#7480)

### Bug Fixes / Nits

- Improve openai fine-tuned model parsing (#7474)
- doing some code de-duplication (#7468)
- support both str and templates for query_wrapper_prompt in HF LLMs (#7473)

## [0.8.13] - 2023-08-29

### New Features

- Add embedding finetuning (#7452)
- Added support for RunGPT LLM (#7401)
- Integration guide and notebook with DeepEval (#7425)
- Added `VectorIndex` and `VectaraRetriever` as a managed index (#7440)
- Added support for `to_tool_list` to detect and use async functions (#7282)

## [0.8.12] - 2023-08-28

### New Features

- add openai finetuning class (#7442)
- Service Context to/from dict (#7395)
- add finetuning guide (#7429)

### Smaller Features / Nits / Bug Fixes

- Add example how to run FalkorDB docker (#7441)
- Update root.md to use get_response_synthesizer expected type. (#7437)
- Bugfix MonsterAPI Pydantic version v2/v1 support. Doc Update (#7432)

## [0.8.11.post3] - 2023-08-27

### New Features

- AutoMergingRetriever (#7420)

## [0.8.10.post1] - 2023-08-25

### New Features

- Added support for `MonsterLLM` using MonsterAPI (#7343)
- Support comments fields in NebulaGraphStore and int type VID (#7402)
- Added configurable endpoint for DynamoDB (#6777)
- Add structured answer filtering for Refine response synthesizer (#7317)

### Bug Fixes / Nits

- Use `utf-8` for json file reader (#7390)
- Fix entity extractor initialization (#7407)

## [0.8.9] - 2023-08-24

### New Features

- Added support for FalkorDB/RedisGraph graph store (#7346)
- Added directed sub-graph RAG (#7378)
- Added support for `BM25Retriever` (#7342)

### Bug Fixes / Nits

- Added `max_tokens` to `Xinference` LLM (#7372)
- Support cache dir creation in multithreaded apps (#7365)
- Ensure temperature is a float for openai (#7382)
- Remove duplicate subjects in knowledge graph retriever (#7378)
- Added support for both pydantic v1 and v2 to allow other apps to move forward (#7394)

### Breaking/Deprecated API Changes

- Refactor prompt template (#7319)
  - Use `BasePromptTemplate` for generic typing
  - Use `PromptTemplate`, `ChatPromptTemplate`, `SelectorPromptTemplate` as core implementations
  - Use `LangchainPromptTemplate` for compatibility with Langchain prompt templates
  - Fully replace specific prompt classes (e.g. `SummaryPrompt`) with generic `BasePromptTemplate` for typing in codebase.
  - Keep `Prompt` as an alias for `PromptTemplate` for backwards compatibility.
  - BREAKING CHANGE: remove support for `Prompt.from_langchain_prompt`, please use `template=LangchainPromptTemplate(lc_template)` instead.

## [0.8.8] - 2023-08-23

### New Features

- `OpenAIFineTuningHandler` for collecting LLM inputs/outputs for OpenAI fine tuning (#7367)

### Bug Fixes / Nits

- Add support for `claude-instant-1.2` (#7369)

## [0.8.7] - 2023-08-22

### New Features

- Support fine-tuned OpenAI models (#7364)
- Added support for Cassandra vector store (#6784)
- Support pydantic fields in tool functions (#7348)

### Bug Fixes / Nits

- Fix infinite looping with forced function call in `OpenAIAgent` (#7363)

## [0.8.6] - 2023-08-22

### New Features

- auto vs. recursive retriever notebook (#7353)
- Reader and Vector Store for BagelDB with example notebooks (#7311)

### Bug Fixes / Nits

- Use service context for intermediate index in retry source query engine (#7341)
- temp fix for prompt helper + chat models (#7350)
- Properly skip unit-tests when packages not installed (#7351)

## [0.8.5.post2] - 2023-08-20

### New Features

- Added FireStore docstore/index store support (#7305)
- add recursive agent notebook (#7330)

### Bug Fixes / Nits

- Fix Azure pydantic error (#7329)
- fix callback trace ids (make them a context var) (#7331)

## [0.8.5.post1] - 2023-08-18

### New Features

- Awadb Vector Store (#7291)

### Bug Fixes / Nits

- Fix bug in OpenAI llm temperature type

## [0.8.5] - 2023-08-18

### New Features

- Expose a system prompt/query wrapper prompt in the service context for open-source LLMs (#6647)
- Changed default MyScale index format to `MSTG` (#7288)
- Added tracing to chat engines/agents (#7304)
- move LLM and embeddings to pydantic (#7289)

### Bug Fixes / Nits

- Fix sentence splitter bug (#7303)
- Fix sentence splitter infinite loop (#7295)

## [0.8.4] - 2023-08-17

### Bug Fixes / Nits

- Improve SQL Query parsing (#7283)
- Fix loading embed_model from global service context (#7284)
- Limit langchain version until we migrate to pydantic v2 (#7297)

## [0.8.3] - 2023-08-16

### New Features

- Added Knowledge Graph RAG Retriever (#7204)

### Bug Fixes / Nits

- accept `api_key` kwarg in OpenAI LLM class constructor (#7263)
- Fix to create separate queue instances for separate instances of `StreamingAgentChatResponse` (#7264)

## [0.8.2.post1] - 2023-08-14

### New Features

- Added support for Rockset as a vector store (#7111)

### Bug Fixes

- Fixed bug in service context definition that could disable LLM (#7261)

## [0.8.2] - 2023-08-14

### New Features

- Enable the LLM or embedding model to be disabled by setting to `None` in the service context (#7255)
- Resolve nearly any huggingface embedding model using the `embed_model="local:<model_name>"` syntax (#7255)
- Async tool-calling support (#7239)

### Bug Fixes / Nits

- Updated supabase kwargs for add and query (#7103)
- Small tweak to default prompts to allow for more general purpose queries (#7254)
- Make callback manager optional for `CustomLLM` + docs update (#7257)

## [0.8.1] - 2023-08-13

### New Features

- feat: add node_postprocessors to ContextChatEngine (#7232)
- add ensemble query engine tutorial (#7247)

### Smaller Features

- Allow EMPTY keys for Fastchat/local OpenAI API endpoints (#7224)

## [0.8.0] - 2023-08-11

### New Features

- Added "LLAMA_INDEX_CACHE_DIR" to control cached files (#7233)
- Default to pydantic selectors when possible (#7154, #7223)
- Remove the need for langchain wrappers on `embed_model` in the service context (#7157)
- Metadata extractors take an `LLM` object now, in addition to `LLMPredictor` (#7202)
- Added local mode + fallback to llama.cpp + llama2 (#7200)
- Added local fallback for embeddings to `BAAI/bge-small-en` (#7200)
- Added `SentenceWindowNodeParser` + `MetadataReplacementPostProcessor` (#7211)

### Breaking Changes

- Change default LLM to gpt-3.5-turbo from text-davinci-003 (#7223)
- Change prompts for compact/refine/tree_summarize to work better with gpt-3.5-turbo (#7150, #7179, #7223)
- Increase default LLM temperature to 0.1 (#7180)

## [0.7.24.post1] - 2023-08-11

### Other Changes

- Reverted #7223 changes to defaults (#7235)

## [0.7.24] - 2023-08-10

### New Features

- Default to pydantic selectors when possible (#7154, #7223)
- Remove the need for langchain wrappers on `embed_model` in the service context (#7157)
- Metadata extractors take an `LLM` object now, in addition to `LLMPredictor` (#7202)
- Added local mode + fallback to llama.cpp + llama2 (#7200)
- Added local fallback for embeddings to `BAAI/bge-small-en` (#7200)
- Added `SentenceWindowNodeParser` + `MetadataReplacementPostProcessor` (#7211)

### Breaking Changes

- Change default LLM to gpt-3.5-turbo from text-davinci-003 (#7223)
- Change prompts for compact/refine/tree_summarize to work better with gpt-3.5-turbo (#7150, #7179, #7223)
- Increase default LLM temperature to 0.1 (#7180)

### Other Changes

- docs: Improvements to Mendable Search (#7220)
- Refactor openai agent (#7077)

### Bug Fixes / Nits

- Use `1 - cosine_distance` for pgvector/postgres vector db (#7217)
- fix metadata formatting and extraction (#7216)
- fix(readers): Fix non-ASCII JSON Reader bug (#7086)
- Chore: change PgVectorStore variable name from `sim` to `distance` for clarity (#7226)

## [0.7.23] - 2023-08-10

### Bug Fixes / Nits

- Fixed metadata formatting with custom tempalates and inheritance (#7216)

## [0.7.23] - 2023-08-10

### New Features

- Add "one click observability" page to docs (#7183)
- Added Xorbits inference for local deployments (#7151)
- Added Zep vector store integration (#7203)
- feat/zep vectorstore (#7203)

### Bug Fixes / Nits

- Update the default `EntityExtractor` model (#7209)
- Make `ChatMemoryBuffer` pickleable (#7205)
- Refactored `BaseOpenAIAgent` (#7077)

## [0.7.22] - 2023-08-08

### New Features

- add ensemble retriever notebook (#7190)
- DOCS: added local llama2 notebook (#7146)

### Bug Fixes / Nits

- Fix for `AttributeError: 'OpenAIAgent' object has no attribute 'callback_manager'` by calling super constructor within `BaseOpenAIAgent`
- Remove backticks from nebula queries (#7192)

## [0.7.21] - 2023-08-07

### New Features

- Added an `EntityExtractor` for metadata extraction (#7163)

## [0.7.20] - 2023-08-06

### New Features

- add router module docs (#7171)
- add retriever router (#7166)

### New Features

- Added a `RouterRetriever` for routing queries to specific retrievers (#7166)

### Bug Fixes / Nits

- Fix for issue where having multiple concurrent streamed responses from `OpenAIAgent` would result in interleaving of tokens across each response stream. (#7164)
- fix llms callbacks issue (args[0] error) (#7165)

## [0.7.19] - 2023-08-04

### New Features

- Added metadata filtering to weaviate (#7130)
- Added token counting (and all callbacks) to agents and streaming (#7122)

## [0.7.18] - 2023-08-03

### New Features

- Added `to/from_string` and `to/from_dict` methods to memory objects (#7128)
- Include columns comments from db tables in table info for SQL queries (#7124)
- Add Neo4j support (#7122)

### Bug Fixes / Nits

- Added `Azure AD` validation support to the `AzureOpenAI` class (#7127)
- add `flush=True` when printing agent/chat engine response stream (#7129)
- Added `Azure AD` support to the `AzureOpenAI` class (#7127)
- Update LLM question generator prompt to mention JSON markdown (#7105)
- Fixed `astream_chat` in chat engines (#7139)

## [0.7.17] - 2023-08-02

### New Features

- Update `ReActAgent` to support memory modules (minor breaking change since the constructor takes `memory` instead of `chat_history`, but the main `from_tools` method remains backward compatible.) (#7116)
- Update `ReActAgent` to support streaming (#7119)
- Added Neo4j graph store and query engine integrations (#7122)
- add object streaming (#7117)

## [0.7.16] - 2023-07-30

### New Features

- Chat source nodes (#7078)

## [0.7.15] - 2023-07-29

### Bug Fixes / Nits

- anthropic api key customization (#7082)
- Fix broken link to API reference in Contributor Docs (#7080)
- Update vector store docs (#7076)
- Update comment (#7073)

## [0.7.14] - 2023-07-28

### New Features

- Added HotpotQADistractor benchmark evaluator (#7034)
- Add metadata filter and delete support for LanceDB (#7048)
- Use MetadataFilters in opensearch (#7005)
- Added support for `KuzuGraphStore` (#6970)
- Added `kg_triplet_extract_fn` to customize how KGs are built (#7068)

### Bug Fixes / Nits

- Fix string formatting in context chat engine (#7050)
- Fixed tracing for async events (#7052)
- Less strict triplet extraction for KGs (#7059)
- Add configurable limit to KG data retrieved (#7059)
- Nebula connection improvements (#7059)
- Bug fix in building source nodes for agent response (#7067)

## [0.7.13] - 2023-07-26

### New Features

- Support function calling api for AzureOpenAI (#7041)

### Bug Fixes / Nits

- tune prompt to get rid of KeyError in SubQ engine (#7039)
- Fix validation of Azure OpenAI keys (#7042)

## [0.7.12] - 2023-07-25

### New Features

- Added `kwargs` to `ComposableGraph` for the underlying query engines (#6990)
- Validate openai key on init (#6940)
- Added async embeddings and async RetrieverQueryEngine (#6587)
- Added async `aquery` and `async_add` to PGVectorStore (#7031)
- Added `.source_nodes` attribute to chat engine and agent responses (#7029)
- Added `OpenInferenceCallback` for storing generation data in OpenInference format (#6998)

### Bug Fixes / Nits

- Fix achat memory initialization for data agents (#7000)
- Add `print_response_stream()` to agengt/chat engine response class (#7018)

### Bug Fixes / Nits

- Fix achat memory initialization for data agents (#7000)
- Add `print_response_stream()` to agengt/chat engine response class (#7018)

## [v0.7.11.post1] - 2023-07-20

### New Features

- Default to pydantic question generation when possible for sub-question query engine (#6979)

### Bug Fixes / Nits

- Fix returned order of messages in large chat memory (#6979)

## [v0.7.11] - 2023-07-19

### New Features

- Added a `SentenceTransformerRerank` node post-processor for fast local re-ranking (#6934)
- Add numpy support for evaluating queries in pandas query engine (#6935)
- Add metadata filtering support for Postgres Vector Storage integration (#6968)
- Proper llama2 support for agents and query engines (#6969)

### Bug Fixes / Nits

- Added `model_name` to LLMMetadata (#6911)
- Fallback to retriever service context in query engines (#6911)
- Fixed `as_chat_engine()` ValueError with extra kwargs (#6971

## [v0.7.10.post1] - 2023-07-18

### New Features

- Add support for Replicate LLM (vicuna & llama 2!)

### Bug Fixes / Nits

- fix streaming for condense chat engine (#6958)

## [v0.7.10] - 2023-07-17

### New Features

- Add support for chroma v0.4.0 (#6937)
- Log embedding vectors to callback manager (#6962)

### Bug Fixes / Nits

- add more robust embedding timeouts (#6779)
- improved connection session management on postgres vector store (#6843)

## [v0.7.9] - 2023-07-15

### New Features

- specify `embed_model="local"` to use default local embbeddings in the service context (#6806)
- Add async `acall` endpoint to `BasePydanticProgram` (defaults to sync version). Implement for `OpenAIPydanticProgram`

### Bug Fixes / Nits

- fix null metadata for searching existing vector dbs (#6912)
- add module guide docs for `SimpleDirectoryReader` (#6916)
- make sure `CondenseQuestionChatEngine` streaming chat endpoints work even if not explicitly setting `streaming=True` in the underlying query engine.

## [v0.7.8] - 2023-07-13

### New Features

- Added embedding speed benchmark (#6876)
- Added BEIR retrieval benchmark (#6825)

### Bug Fixes / Nits

- remove toctrees from deprecated_terms (#6895)
- Relax typing dependencies (#6879)
- docs: modification to evaluation notebook (#6840)
- raise error if the model does not support functions (#6896)
- fix(bench embeddings): bug not taking into account string length (#6899)x

## [v0.7.7] - 2023-07-13

### New Features

- Improved milvus consistency support and output fields support (#6452)
- Added support for knowledge graph querying w/ cypyer+nebula (#6642)
- Added `Document.example()` to create documents for fast prototyping (#6739)
- Replace react chat engine to use native reactive agent (#6870)

### Bug Fixes / Nits

- chore: added a help message to makefile (#6861)

### Bug Fixes / Nits

- Fixed support for using SQLTableSchema context_str attribute (#6891)

## [v0.7.6] - 2023-07-12

### New Features

- Added sources to agent/chat engine responses (#6854)
- Added basic chat buffer memory to agents / chat engines (#6857)
- Adding load and search tool (#6871)
- Add simple agent benchmark (#6869)
- add agent docs (#6866)
- add react agent (#6865)

### Breaking/Deprecated API Changes

- Replace react chat engine with native react agent (#6870)
- Set default chat mode to "best": use openai agent when possible, otherwise use react agent (#6870)

### Bug Fixes / Nits

- Fixed support for legacy vector store metadata (#6867)
- fix chroma notebook in docs (#6872)
- update LC embeddings docs (#6868)

## [v0.7.5] - 2023-07-11

### New Features

- Add `Anthropic` LLM implementation (#6855)

### Bug Fixes / Nits

- Fix indexing error in `SentenceEmbeddingOptimizer` (#6850)
- fix doc for custom embedding model (#6851)
- fix(silent error): Add validation to `SimpleDirectoryReader` (#6819)
- Fix link in docs (#6833)
- Fixes Azure gpt-35-turbo model not recognized (#6828)
- Update Chatbot_SEC.ipynb (#6808)
- Rename leftover original name to LlamaIndex (#6792)
- patch nested traces of the same type (#6791)

## [v0.7.4] - 2023-07-08

### New Features

- `MetadataExtractor` - Documnent Metadata Augmentation via LLM-based feature extractors (#6764)

### Bug Fixes / Nits

- fixed passing in query bundle to node postprocessors (#6780)
- fixed error in callback manager with nested traces (#6791)

## [v0.7.3] - 2023-07-07

### New Features

- Sub question query engine returns source nodes of sub questions in the callback manager (#6745)
- trulens integration (#6741)
- Add sources to subquestion engine (#6745)

### Bug Fixes / Nits

- Added/Fixed streaming support to simple and condense chat engines (#6717)
- fixed `response_mode="no_text"` response synthesizer (#6755)
- fixed error setting `num_output` and `context_window` in service context (#6766)
- Fix missing as_query_engine() in tutorial (#6747)
- Fixed variable sql_query_engine in the notebook (#6778)
- fix required function fields (#6761)
- Remove usage of stop token in Prompt, SQL gen (#6782)

## [v0.7.2] - 2023-07-06

### New Features

- Support Azure OpenAI (#6718)
- Support prefix messages (e.g. system prompt) in chat engine and OpenAI agent (#6723)
- Added `CBEventType.SUB_QUESTIONS` event type for tracking sub question queries/responses (#6716)

### Bug Fixes / Nits

- Fix HF LLM output error (#6737)
- Add system message support for langchain message templates (#6743)
- Fixed applying node-postprocessors (#6749)
- Add missing `CustomLLM` import under `llama_index.llms` (#6752)
- fix(typo): `get_transformer_tokenizer_fn` (#6729)
- feat(formatting): `black[jupyter]` (#6732)
- fix(test): `test_optimizer_chinese` (#6730)

## [v0.7.1] - 2023-07-05

### New Features

- Streaming support for OpenAI agents (#6694)
- add recursive retriever + notebook example (#6682)

## [v0.7.0] - 2023-07-04

### New Features

- Index creation progress bars (#6583)

### Bug Fixes/ Nits

- Improved chat refine template (#6645)

### Breaking/Deprecated API Changes

- Change `BaseOpenAIAgent` to use `llama_index.llms.OpenAI`. Adjust `chat_history` to use `List[ChatMessage]]` as type.
- Remove (previously deprecated) `llama_index.langchain_helpers.chain_wrapper` module.
- Remove (previously deprecated) `llama_index.token_counter.token_counter` module. See [migration guide](/how_to/callbacks/token_counting_migration.html) for more details on new callback based token counting.
- Remove `ChatGPTLLMPredictor` and `HuggingFaceLLMPredictor`. See [migration guide](/how_to/customization/llms_migration_guide.html) for more details on replacements.
- Remove support for setting `cache` via `LLMPredictor` constructor.
- Update `BaseChatEngine` interface:
  - adjust `chat_history` to use `List[ChatMessage]]` as type
  - expose `chat_history` state as a property
  - support overriding `chat_history` in `chat` and `achat` endpoints
- Remove deprecated arguments for `PromptHelper`: `max_input_size`, `embedding_limit`, `max_chunk_overlap`
- Update all notebooks to use native openai integration (#6696)

## [v0.6.38] - 2023-07-02

### New Features

- add optional tqdm progress during index creation (#6583)
- Added async support for "compact" and "refine" response modes (#6590)
- [feature]add transformer tokenize functionalities for optimizer (chinese) (#6659)
- Add simple benchmark for vector store (#6670)
- Introduce `llama_index.llms` module, with new `LLM` interface, and `OpenAI`, `HuggingFaceLLM`, `LangChainLLM` implementations. (#6615)
- Evaporate pydantic program (#6666)

### Bug Fixes / Nits

- Improve metadata/node storage and retrieval for RedisVectorStore (#6678)
- Fixed node vs. document filtering in vector stores (#6677)
- add context retrieval agent notebook link to docs (#6660)
- Allow null values for the 'image' property in the ImageNode class and se… (#6661)
- Fix broken links in docs (#6669)
- update milvus to store node content (#6667)

## [v0.6.37] - 2023-06-30

### New Features

- add context augmented openai agent (#6655)

## [v0.6.36] - 2023-06-29

### New Features

- Redis support for index stores and docstores (#6575)
- DuckDB + SQL query engine notebook (#6628)
- add notebook showcasing deplot data loader (#6638)

### Bug Fixes / Nits

- More robust JSON parsing from LLM for `SelectionOutputParser` (#6610)
- bring our loaders back in line with llama-hub (#6630)
- Remove usage of SQLStructStoreIndex in notebooks (#6585)
- MD reader: remove html tags and leave linebreaks alone (#6618)
- bump min langchain version to latest version (#6632)
- Fix metadata column name in postgres vector store (#6622)
- Postgres metadata fixes (#6626, #6634)
- fixed links to dataloaders in contribution.md (#6636)
- fix: typo in docs in creating custom_llm huggingface example (#6639)
- Updated SelectionOutputParser to handle JSON objects and arrays (#6610)
- Fixed docstring argument typo (#6652)

## [v0.6.35] - 2023-06-28

- refactor structured output + pydantic programs (#6604)

### Bug Fixes / Nits

- Fix serialization for OpenSearch vector stores (#6612)
- patch docs relationships (#6606)
- Bug fix for ignoring directories while parsing git repo (#4196)
- updated Chroma notebook (#6572)
- Backport old node name (#6614)
- Add the ability to change chroma implementation (#6601)

## [v0.6.34] - 2023-06-26

### Patch Update (v0.6.34.post1)

- Patch imports for Document obj for backwards compatibility (#6597)

### New Features

- New `TextNode`/`Document` object classes based on pydantic (#6586)
- `TextNode`/`Document` objects support metadata customization (metadata templates, exclude metadata from LLM or embeddings) (#6586)
- Nodes no longer require flat metadata dictionaries, unless the vector store you use requires it (#6586)

### Bug Fixes / Nits

- use `NLTK_DATA` env var to control NLTK download location (#6579)
- [discord] save author as metadata in group_conversations.py (#6592)
- bs4 -> beautifulsoup4 in requirements (#6582)
- negate euclidean distance (#6564)
- add df output parser notebook link to docs (#6581)

### Breaking/Deprecated API Changes

- `Node` has been renamed to `TextNode` and is imported from `llama_index.schema` (#6586)
- `TextNode` and `Document` must be instantiated with kwargs: `Document(text=text)` (#6586)
- `TextNode` (fka `Node`) has a `id_` or `node_id` property, rather than `doc_id` (#6586)
- `TextNode` and `Document` have a metadata property, which replaces the extra_info property (#6586)
- `TextNode` no longer has a `node_info` property (start/end indexes are accessed directly with `start/end_char_idx` attributes) (#6586)

## [v0.6.33] - 2023-06-25

### New Features

- Add typesense vector store (#6561)
- add df output parser (#6576)

### Bug Fixes / Nits

- Track langchain dependency via bridge module. (#6573)

## [v0.6.32] - 2023-06-23

### New Features

- add object index (#6548)
- add SQL Schema Node Mapping + SQLTableRetrieverQueryEngine + obj index fixes (#6569)
- sql refactor (NLSQLTableQueryEngine) (#6529)

### Bug Fixes / Nits

- Update vector_stores.md (#6562)
- Minor `BaseResponseBuilder` interface cleanup (#6557)
- Refactor TreeSummarize (#6550)

## [v0.6.31] - 2023-06-22

### Bug Fixes / Nits

- properly convert weaviate distance to score (#6545)
- refactor tree summarize and fix bug to not truncate context (#6550)
- fix custom KG retrieval notebook nits (#6551)

## [v0.6.30] - 2023-06-21

### New Features

- multi-selector support in router query engine (#6518)
- pydantic selector support in router query engine using OpenAI function calling API (#6518)
- streaming response support in `CondenseQuestionChatEngine` and `SimpleChatEngine` (#6524)
- metadata filtering support in `QdrantVectorStore` (#6476)
- add `PGVectorStore` to support postgres with pgvector (#6190)

### Bug Fixes / Nits

- better error handling in the mbox reader (#6248)
- Fix blank similarity score when using weaviate (#6512)
- fix for sorted nodes in `PrevNextNodePostprocessor` (#6048)

### Breaking/Deprecated API Changes

- Refactor PandasQueryEngine to take in df directly, deprecate PandasIndex (#6527)

## [v0.6.29] - 2023-06-20

### New Features

- query planning tool with OpenAI Function API (#6520)
- docs: example of kg+vector index (#6497)
- Set context window sizes for Cohere and AI21(J2 model) (#6485)

### Bug Fixes / Nits

- add default input size for Cohere and AI21 (#6485)
- docs: replace comma with colon in dict object (#6439)
- extra space in prompt and error message update (#6443)
- [Issue 6417] Fix prompt_templates docs page (#6499)
- Rip out monkey patch and update model to context window mapping (#6490)

## [v0.6.28] - 2023-06-19

### New Features

- New OpenAI Agent + Query Engine Cookbook (#6496)
- allow recursive data extraction (pydantic program) (#6503)

### Bug Fixes / Nits

- update mongo interface (#6501)
- fixes that we forgot to include for openai pydantic program (#6503) (#6504)
- Fix github pics in Airbyte notebook (#6493)

## [v0.6.27] - 2023-06-16

### New Features

- Add node doc_id filtering to weaviate (#6467)
- New `TokenCountingCallback` to customize and track embedding, prompt, and completion token usage (#6440)
- OpenAI Retrieval Function Agent (#6491)

### Breaking/Deprecated API Changes

- Deprecated current token tracking (llm predictor and embed model will no longer track tokens in the future, please use the `TokenCountingCallback` (#6440)
- Add maximal marginal relevance to the Simple Vector Store, which can be enabled as a query mode (#6446)

### Bug Fixes / Nits

- `as_chat_engine` properly inherits the current service context (#6470)
- Use namespace when deleting from pinecone (#6475)
- Fix paths when using fsspec on windows (#3778)
- Fix for using custom file readers in `SimpleDirectoryReader` (#6477)
- Edit MMR Notebook (#6486)
- FLARE fixes (#6484)

## [v0.6.26] - 2023-06-14

### New Features

- Add OpenAIAgent and tutorial notebook for "build your own agent" (#6461)
- Add OpenAIPydanticProgram (#6462)

### Bug Fixes / Nits

- Fix citation engine import (#6456)

## [v0.6.25] - 2023-06-13

### New Features

- Added FLARE query engine (#6419).

## [v0.6.24] - 2023-06-12

### New Features

- Added better support for vector store with existing data (e.g. allow configurable text key) for Pinecone and Weaviate. (#6393)
- Support batched upsert for Pineone (#6393)
- Added initial [guidance](https://github.com/microsoft/guidance/) integration. Added `GuidancePydanticProgram` for generic structured output generation and `GuidanceQuestionGenerator` for generating sub-questions in `SubQuestionQueryEngine` (#6246).

## [v0.6.23] - 2023-06-11

### Bug Fixes / Nits

- Remove hardcoded chunk size for citation query engine (#6408)
- Mongo demo improvements (#6406)
- Fix notebook (#6418)
- Cleanup RetryQuery notebook (#6381)

## [v0.6.22] - 2023-06-10

### New Features

- Added `SQLJoinQueryEngine` (generalization of `SQLAutoVectorQueryEngine`) (#6265)
- Added support for graph stores under the hood, and initial support for Nebula KG. More docs coming soon! (#2581)
- Added guideline evaluator to allow llm to provide feedback based on user guidelines (#4664)
- Added support for MongoDB Vector stores to enable Atlas knnbeta search (#6379)
- Added new CitationQueryEngine for inline citations of sources in response text (#6239)

### Bug Fixes

- Fixed bug with `delete_ref_doc` not removing all metadata from the docstore (#6192)
- FIxed bug with loading existing QDrantVectorStore (#6230)

### Miscellaneous

- Added changelog officially to github repo (#6191)

## [v0.6.21] - 2023-06-06

### New Features

- SimpleDirectoryReader has new `filename_as_id` flag to automatically set the doc_id (useful for `refresh_ref_docs()`)
- DocArray vector store integration
- Tair vector store integration
- Weights and Biases callback handler for tracing and versioning indexes
- Can initialize indexes directly from a vector store: `index = VectorStoreIndex.from_vector_store(vector_store=vector_store)`

### Bug Fixes

- Fixed multimodal notebook
- Updated/fixed the SQL tutorial in the docs

### Miscellaneous

- Minor docs updates
- Added github pull-requset templates
- Added github issue-forms

## [v0.6.20] - 2023-06-04

### New Features

- Added new JSONQueryEngine that uses JSON schema to deliver more accurate JSON query answers
- Metadata support for redis vector-store
- Added Supabase vector store integration

### Bug Fixes

- Fixed typo in text-to-sql prompt

### Breaking/Deprecated API Changes

- Removed GPT prefix from indexes (old imports/names are still supported though)

### Miscellaneous

- Major docs updates, brought important modules to the top level

## [v0.6.19] - 2023-06-02

### New Features

- Added agent tool abstraction for llama-hub data loaders

### Miscellaneous

- Minor doc updates

## [v0.6.18] - 2023-06-02

### Miscellaneous

- Added `Discover LlamaIndex` video series to the tutorials docs section
- Minor docs updates

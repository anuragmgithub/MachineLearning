## Short description  
DataCopilot is an end-to-end Supply Chain Intelligence Assistant that answers natural language   questions about shipments, inventory, suppliers, invoices, and exceptions by combining structured   data (MySQL / Snowflake) and unstructured documents (invoices, emails, PDFs). It   demonstrates LLMs, embeddings, RAG, and agentic automation (SQL/ETL agent + docs agent). Build,   evaluate, and deploy a production-style pipeline.  

### Why this use case?

Supply chains generate a mix of structured time-series data (orders, inventory, shipments) and   unstructured artifacts (purchase orders, invoices, email threads). This mix makes the domain ideal  for learning:  

retrieval-augmented generation (RAG) to ground LLM answers,combining SQL queries with retrieved  docs,building agents that can run safe SQL / ETL actions, production concerns: index refresh, observability, and safe response filtering.  

- An API (/ask) and a small web UI (Streamlit/React) where users can ask natural language queries about supply chain data.  
- RAG pipeline that retrieves relevant docs & table rows and uses an LLM to produce grounded answers with citations.  
- An Agent that can safely execute read-only SQL queries or call pre-approved ETL tasks when requested by the user.  
- A scheduled ingestion & reindexing pipeline (Airflow) that fetches new documents and re-embeds them.  
- Dockerized deployment with basic monitoring and an evaluation suite.  

---

## Tech stack:
-LLMs & embeddings: OpenAI (or Llama 3 locally) + text-embedding-3-large or sentence-transformers fallback
- RAG framework: LangChain or LlamaIndex
- Vector DB: FAISS (local) for dev; Pinecone or Qdrant for production
- Backend: FastAPI
- Frontend: Streamlit (fast), optionally React later
- Orchestration: Apache Airflow (DAG for ETL + reindexing)
- Storage / Warehouse: MySQL (source), Snowflake (analytics)
- Containerization: Docker, docker-compose; k8s manifests optional
- Testing: pytest
- Observability: simple logging, LangChain callbacks or LangFuse/Weights & Biases (optional)

```
datacopilot-supplychain/
├── README.md
├── docker-compose.yml
├── .env.example
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── services/
│   │   ├── embeddings.py
│   │   ├── vectorstore.py
│   │   ├── retriever.py
│   │   └── agent.py
│   ├── db/
│   │   └── mysql_client.py
│   └── config.py
├── scripts/
│   ├── etl_to_snowflake.py
│   ├── ingest_docs.py
│   └── pdf_to_text.py
├── infra/
│   └── airflow/dags/etl_index_dag.py
├── data/
│   ├── docs/
│   └── raw/
├── frontend/
│   └── streamlit_app.py
├── tests/
├── examples/
│   └── sample_queries.md
└── docs/
    └── design.md
```
---

## High-level architecture

- Data sources: MySQL (orders, inventory, shipments), file store (PDF invoices, PO emails), Snowflake for analytics.  

- ETL: scripts/etl_to_snowflake.py moves/cleans sources into Snowflake; scripts/ingest_docs.py extracts text from PDFs and chunks them.  

- Embeddings & Indexing: chunked text + metadata → embeddings → vector DB. Structured rows can also be converted into short textual passages and indexed for retrieval.  

- Query path: user input → embedding → retrieve top-k docs/rows → assemble prompt (context + SQL results if agent runs) → LLM → answer + citations.  

- Agent: when question needs a table scan, agent may run a read-only SQL query (via a safe SQL agent), fetch results, include them in context, and generate the final answer. Agent decisions are logged and visible to the user. 

Deliverables checklist (MVP)

 Repo with skeleton and docs

 Sample data & ingestion scripts

 Embeddings + FAISS index with metadata

 FastAPI /ask endpoint with RAG pipeline

 Streamlit UI + example queries

 SQL agent (read-only) and safe runner

 Airflow DAG to refresh index weekly

 Evaluation script & basic logs

 Docker compose files

Helpful resources & libs to read

LangChain docs (retrieval chains, agents)

OpenAI or Hugging Face embeddings models docs

FAISS quickstart

Airflow DAG best practices

Streamlit quickstart
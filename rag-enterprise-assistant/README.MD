rag-enterprise-assistant/
├── ingestion/
│   ├── __init__.py
│   ├── loaders.py
│   ├── chunkers.py
│   ├── prepare_chunks.py
│   ├── embedder.py
│   └── build_index.py
│
├── retrieval/
│   ├── __init__.py
│   ├── faiss_store.py
│   ├── retriever.py        (later)
│   ├── reranker.py         (later)
│   └── test_search.py
│
├── llm/
│   ├── __init__.py
│   ├── prompts.py          (later)
│   └── answer_generator.py (later)
│
├── api/
│   ├── __init__.py
│   └── app.py              (later)
│
├── eval/
│   └── evaluation.py       (later)
│
├── config/
│   └── settings.py         (later)
│
├── data/
│   ├── docs/
│   │   ├── rbi/
│   │   │   └── rbi_kyc_master_direction.pdf
│   │   └── annual_reports/
│   └── faiss/
│       ├── banking_docs.index
│       └── banking_docs.meta
│
├── logs/
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md

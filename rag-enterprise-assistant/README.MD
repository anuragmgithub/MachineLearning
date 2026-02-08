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


# RAG Enterprise Assistant

A Retrieval-Augmented Generation (RAG) project for enterprise document QA.  
This project ingests PDFs, processes them into embeddings, builds a FAISS index for retrieval, and uses an LLM to answer user queries based   on relevant chunks.  

---

## Architecture   

+----------------+  
| PDF Documents  |  
+----------------+  
        |  
        v  
+----------------+  
| Text Cleaning  |  
+----------------+  
        |  
        v   
+----------------+  
| Text Chunking  |  
+----------------+  
        |  
        v  
+----------------+  
| Embeddings     |  
+----------------+  
        |  
        v  
+----------------+  
| FAISS Index    |  
+----------------+  
        |  
        v   
+----------------+  
| Retriever      |   
+----------------+   
        |   
        v   
+----------------+   
| LLM            |   
+----------------+  
        |  
        v  
+----------------+   
| Answer Output  |  
+----------------+  

## Install PyTorch CPU version (for Sentence Transformers) 

```
python -m pip install torch==2.3.1+cpu torchvision==0.14.1+cpu torchaudio==2.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

```

### Run the ingestion script:
```
python -m ingestion.run_ingestion
```


# RAG Enterprise Assistant

## Project Structure

```
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
│   ├── retriever.py                (later)
│   ├── reranker.py                 (later)
│   └── test_search.py
│
├── llm/
│   ├── __init__.py
│   ├── prompts.py                  (later)
│   └── answer_generator.py         (later)
│
├── api/
│   ├── __init__.py
│   └── app.py                      (later)
│
├── eval/
│   └── evaluation.py               (later)
│
├── config/
│   └── settings.py                 (later)
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
├── .env
├── .gitignore
├── requirements.txt
└── README.md


## Overview

A Retrieval-Augmented Generation (RAG) project for enterprise document QA. This project ingests PDFs, processes them into embeddings, builds a FAISS index for retrieval, and uses an LLM to answer user queries based on relevant chunks.

---

## Architecture

```
PDF Documents
     ↓
Text Cleaning
     ↓
Text Chunking
     ↓
Embeddings
     ↓
FAISS Index
     ↓
Retriever
     ↓
LLM
     ↓
Answer Output
```

---

## Setup & Installation

### Prerequisites

- Python 3.10+
- PyTorch (CPU or GPU)

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install PyTorch (CPU version for Sentence Transformers)

```bash
python -m pip install torch==2.3.1+cpu torchvision==0.14.1+cpu torchaudio==2.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
```

---

## Usage

### Run the Ingestion Script

```bash
python -m ingestion.run_ingestion
```

---

## Project Components

| Module | Purpose | Status |
|--------|---------|--------|
| **ingestion** | PDF parsing, text cleaning, chunking, embeddings | Active |
| **retrieval** | FAISS indexing and search | Active |
| **llm** | LLM integration for answer generation | In Progress |
| **api** | REST API endpoints | Planned |
| **eval** | Evaluation metrics | Planned |
| **config** | Configuration management | Planned |

---

## Data

- **docs/**: Source PDF documents
  - `rbi/`: RBI guideline documents
  - `annual_reports/`: Bank annual reports
- **faiss/**: Pre-built FAISS indices and metadata

---

## Configuration

Create a `.env` file in the project root with required environment variables.

---

## Requirements

See [requirements.txt](requirements.txt) for all dependencies.

---

## License

This project is provided as-is for educational and enterprise use.


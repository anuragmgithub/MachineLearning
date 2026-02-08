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

### Key Models Used

| Component | Model | Details |
|-----------|-------|---------|
| **Embedding** | `all-MiniLM-L6-v2` (Sentence Transformers) | 384-dimensional dense embeddings for semantic search |
| **LLM** | OpenAI `gpt-3.5-turbo` | Context-aware answer generation with configurable temperature |
| **Vector Store** | FAISS (IndexFlatL2) | In-memory similarity search using L2 distance metrics |

### Core Concepts

- **Retrieval-Augmented Generation (RAG)**: Combines document retrieval with LLM generation for accurate, contextual answers
- **Dense Vector Embeddings**: Semantic representations of text for similarity-based retrieval
- **Vector Similarity Search**: Efficient document ranking using L2 distance in FAISS
- **In-memory Vector Index**: Fast semantic search on enterprise-scale document collections
- **Context-aware Prompting**: System prompts with domain expertise (financial domain) for specialized responses
- **Chunk-based Processing**: Document segmentation for optimal context window and relevance

---

## Technology Stack

| Category | Technology | Purpose |
|----------|-----------|---------|
| **LLM Provider** | OpenAI API | GPT-based answer generation |
| **RAG Framework** | LangChain | Orchestration of retrieval & generation pipelines |
| **Text Embeddings** | Sentence Transformers | Dense vector representations for semantic search |
| **Vector DB** | FAISS (CPU) | Scalable similarity search and indexing |
| **PDF Processing** | PyPDF | Document parsing and text extraction |
| **API Framework** | FastAPI | High-performance REST API endpoints |
| **Data Validation** | Pydantic | Type-safe configuration and schema validation |
| **Configuration** | python-dotenv | Secure environment variable management |

---

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

## How It Works

### 1. **Ingestion Pipeline**
   - **PDF Loading**: Documents are read from `data/docs/` using PyPDF
   - **Text Cleaning**: Remove noise, normalize whitespace, clean special characters
   - **Chunking**: Split documents into semantic chunks (optimal size for embedding & context window)
   - **Embedding Generation**: Convert text chunks to 384-dimensional vectors using `all-MiniLM-L6-v2`
   - **Index Building**: Store embeddings in FAISS with L2 distance metric

### 2. **Retrieval Pipeline**
   - **Query Embedding**: Convert user query to 384-dimensional vector using the same embedding model
   - **Semantic Search**: Find top-K most similar chunks using FAISS (L2 distance)
   - **Reranking** (optional): Re-score retrieved chunks for relevance

### 3. **Answer Generation**
   - **Context Assembly**: Combine retrieved chunks as context
   - **Prompt Engineering**: System prompt provides domain expertise (financial documents)
   - **LLM Inference**: Send context + query to GPT-3.5-turbo with `temperature=0.2` for consistency
   - **Answer Output**: Return concise, context-grounded responses

---

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

### Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
EMBEDDER_MODEL=all-MiniLM-L6-v2
LLM_MODEL=gpt-3.5-turbo
FAISS_INDEX_PATH=data/faiss/banking_docs.index
FAISS_META_PATH=data/faiss/banking_docs.meta
```

### Model Parameters

#### Embedding Model (all-MiniLM-L6-v2)
- **Dimensions**: 384
- **Inference Speed**: Fast (suitable for real-time applications)
- **Strengths**: Good balance of semantic understanding and efficiency
- **Use Case**: Domain-agnostic semantic search

#### LLM (GPT-3.5-turbo)
- **Temperature**: 0.2 (low = deterministic, focused answers)
- **Max Tokens**: 500 (configurable per request)
- **System Prompt**: Financial domain expert
- **Context Window**: ~4K tokens (sufficient for retrieved context + query)

#### FAISS Index
- **Metric**: L2 Distance (Euclidean distance)
- **Type**: IndexFlatL2 (exact search, no approximation)
- **Scalability**: CPU-based, suitable for up to ~1M documents

---

---

## Requirements

See [requirements.txt](requirements.txt) for all dependencies.

---

## License

This project is provided as-is for educational and enterprise use.


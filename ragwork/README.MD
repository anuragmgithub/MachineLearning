## What is RAG?
RAG = Retrieval-Augmented Generation.  
It’s a paradigm that combines:  
- Retrieval: Fetching relevant knowledge from external sources (databases, documents, web, APIs).
- Generation: Using a generative model (like GPT, LLaMA, or Falcon) to produce context-aware responses using retrieved knowledge.  

Why it matters:  
- Traditional LLMs can hallucinate because they rely only on internal parameters.  
- RAG reduces hallucination by grounding responses in actual data.  
- Used in knowledge-intensive tasks like customer support, coding assistants, research, and enterprise knowledge bots.    

RAG system has 3 main layers:  
A. Knowledge Base / Index  
Stores documents, embeddings, or metadata for retrieval.
Types:
- Vector Databases: FAISS, Pinecone, Weaviate, Milvus, ChromaDB  
- Traditional DBs: PostgreSQL, Elasticsearch (if text search is enough)  
Key tasks:  
- Document ingestion  
- Embedding generation  
- Indexing for fast retrieval  

B. Retrieval Layer    
Retrieves top-K relevant documents for a query.  
Techniques:  
- Dense retrieval: Use embeddings + cosine similarity (BERT, OpenAI Embeddings)  
- Sparse retrieval: Keyword-based (BM25)  

C. Generation Layer  
LLM generates output using retrieved context.  
Methods:
- RAG-Sequence: Feed context + query to LLM at once  
- RAG-Token: LLM retrieves knowledge dynamically during token generation  

Production considerations:  
Prompt engineering / templates  
Handling long context (memory-efficient attention, chunking)  
Context ranking and filtering  

D. Orchestration Layer  
Glue everything together.
Components:  
Query processing  
Retrieval  
Generation  
Logging & monitoring (important for production)  
Tools:  
LangChain, LlamaIndex (frameworks that abstract orchestration)  


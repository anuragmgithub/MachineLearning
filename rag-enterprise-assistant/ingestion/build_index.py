# ingestion/build_index.py

import faiss
import numpy as np
from ingestion.embedder import Embedder

def build_faiss_index(chunks, embedding_dim=384, index_path="data/faiss_index.index"):
    """
    Build a FAISS vector index from text chunks.

    Args:
        chunks (list): List of TextChunk objects with `.text` attribute.
        embedding_dim (int): Dimension of the embeddings (default: 384 for MiniLM).
        index_path (str): Path to save the FAISS index.

    Returns:
        index: FAISS index object
    """
    print("Initializing embedder...")
    embedder = Embedder()

    print("Creating embeddings for all chunks...")
    embeddings = [embedder.embed(chunk.text) for chunk in chunks]

    # Convert to numpy array of type float32 (FAISS requirement)
    embeddings_np = np.array(embeddings, dtype=np.float32)

    print(f"Building FAISS index with {len(chunks)} vectors of dimension {embedding_dim}...")
    index = faiss.IndexFlatL2(embedding_dim)  # L2 distance
    index.add(embeddings_np)

    print(f"Total vectors in index: {index.ntotal}")

    # Save index
    faiss.write_index(index, index_path)
    print(f" FAISS index saved to {index_path}")

    return index

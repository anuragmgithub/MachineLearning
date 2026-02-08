# ingestion/retriever.py

import faiss
import numpy as np
from ingestion.embedder import Embedder

class Retriever:
    def __init__(self, index_path="data/faiss_index.index"):
        print(f"⚡ Loading FAISS index from {index_path}...")
        self.index = faiss.read_index(index_path)
        self.embedder = Embedder()

    def retrieve(self, query, top_k=5):
        """
        Return top-k most similar chunks to the query
        """
        query_embedding = self.embedder.embed(query).astype(np.float32)
        query_embedding = np.expand_dims(query_embedding, axis=0)
        distances, indices = self.index.search(query_embedding, top_k)
        return indices[0], distances[0]

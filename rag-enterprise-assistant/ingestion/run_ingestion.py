# ingestion/run_ingestion.py

import os
from dotenv import load_dotenv
import openai

from ingestion.pdf_loader import load_pdfs
from ingestion.text_cleaner import clean_text
from ingestion.chunker import chunk_text
from ingestion.schema import TextChunk
from ingestion.build_index import build_faiss_index
from retrieval.retriever import Retriever
from llm.llm import LLM  # Your LLM wrapper class

# Path to PDFs
PDF_DIR = "data/docs"

def run():
    # -----------------------------
    #  Load environment variables
    # -----------------------------
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env")
    openai.api_key = api_key

    # -----------------------------
    # Load, clean, and chunk PDFs
    # -----------------------------
    raw_docs = load_pdfs(PDF_DIR)
    all_chunks = []

    for doc in raw_docs:
        cleaned_text = clean_text(doc.text)
        chunks = chunk_text(cleaned_text)

        for idx, chunk in enumerate(chunks):
            all_chunks.append(
                TextChunk(
                    source=doc.source,
                    chunk_id=idx,
                    text=chunk
                )
            )

    print(f" Total chunks created: {len(all_chunks)}")
    print("🔹 Sample chunk:\n", all_chunks[0].text[:500], "...")  # print first 500 chars

    # -----------------------------
    # Build FAISS index
    # -----------------------------
    build_faiss_index(all_chunks)
    print(" FAISS index built successfully!")

    # -----------------------------
    # Retrieve relevant chunks for a query
    # -----------------------------
    retriever = Retriever()
    query = "What are the RBI Basel III capital requirements?"
    results, distances = retriever.retrieve(query, top_k=3)

    print("\n🔹 Top retrieved chunks:")
    for i, r in enumerate(results, 1):
        print(f"{i}. {r.text[:200]}...")  # print first 200 chars

    # -----------------------------
    # Generate answer using LLM
    # -----------------------------
    llm = LLM(api_key=api_key)  # Initialize your LLM wrapper with API key
    answer = llm.generate_answer(query, results)

    print("\n🔹 Final Answer from LLM:\n", answer)


if __name__ == "__main__":
    run()

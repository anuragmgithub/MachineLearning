# ingestion/run_ingestion.py

from ingestion.pdf_loader import load_pdfs
from ingestion.text_cleaner import clean_text
from ingestion.chunker import chunk_text
from ingestion.schema import TextChunk
from ingestion.build_index import build_faiss_index
from ingestion.retriever import Retriever
from ingestion.llm import LLM
import os

PDF_DIR = "data/docs"

def run():
    #  Load, clean, and chunk PDFs
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

    print(f"Total chunks created: {len(all_chunks)}")
    print(" Sample chunk:\n", all_chunks[0])

    # Build FAISS index
    build_faiss_index(all_chunks)

    # Retrieve relevant chunks for a query
    retriever = Retriever()
    query = "What are the RBI Basel III capital requirements?"
    results, distances = retriever.retrieve(query, top_k=3)
    print("\nTop retrieved chunks:")
    for r in results:
        print("-", r.text[:200], "...")  # Print first 200 chars

    # Generate answer using LLM
    api_key = os.environ.get("OPENAI_API_KEY")  # Set your API key in environment
    llm = LLM(api_key)
    answer = llm.generate_answer(query, results)
    print("\n🔹 Final Answer from LLM:\n", answer)


if __name__ == "__main__":
    run()

from ingestion.pdf_loader import load_pdfs
from ingestion.text_cleaner import clean_text
from ingestion.chunker import chunk_text
from ingestion.schema import TextChunk
from ingestion.build_index import build_faiss_index

PDF_DIR = "data/docs"

def run():
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

    build_faiss_index(all_chunks)

if __name__ == "__main__":
    run()

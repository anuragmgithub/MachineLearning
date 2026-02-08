from pathlib import Path
from pypdf import PdfReader
from ingestion.schema import RawDocument

def is_garbage(text: str) -> bool:
    if not text:
        return True

    alpha_ratio = sum(c.isalpha() for c in text) / max(len(text), 1)

    # If less than 50% alphabetic characters → garbage
    return alpha_ratio < 0.5


def load_pdfs(pdf_dir: str) -> list[RawDocument]:
    documents = []

    for pdf_path in Path(pdf_dir).glob("*.pdf"):
        reader = PdfReader(pdf_path)

        for page_no, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if not page_text:
                continue

            if is_garbage(page_text):
                continue

            documents.append(
                RawDocument(
                    source=f"{pdf_path.name}::page_{page_no + 1}",
                    text=page_text
                )
            )

    return documents

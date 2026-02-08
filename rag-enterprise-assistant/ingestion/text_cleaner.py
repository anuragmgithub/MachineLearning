import re
import unicodedata

def clean_text(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", errors="ignore").decode()

    # Remove URLs, emails, phone numbers
    text = re.sub(r"http\S+|www\.\S+", " ", text)
    text = re.sub(r"\S+@\S+", " ", text)
    text = re.sub(r"\+?\d[\d\s\-]{7,}\d", " ", text)

    # Remove repeated punctuation
    text = re.sub(r"_+", " ", text)

    text = text.replace("\n", " ")
    text = re.sub(r"\s+", " ", text)

    return text.strip()

from transformers import pipeline
from config.config import MODEL_NAME

# Load the Hugging Face summarization model
summarizer = pipeline("summarization", model=MODEL_NAME)

def summarize_text(text, max_length=130, min_length=30):
    """
    Summarizes the input text using a pre-trained Hugging Face model.
    """
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

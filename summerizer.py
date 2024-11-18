print("Starting Summarizer...")

from transformers import pipeline

# Initialize the summarization pipeline
try:
    summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    print("Summarizer model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    summarizer = None

def summarize_paragraph(paragraph, max_length=100, min_length=25):
    """
    Summarize a given paragraph using a pre-trained model.

    Parameters:
    paragraph (str): The input text to summarize.
    max_length (int): Maximum length of the summary.
    min_length (int): Minimum length of the summary.

    Returns:
    str: The summarized text or an error message.
    """
    if not summarizer:
        return "Summarizer pipeline is not initialized. Please check your setup."
    
    try:
        # Adjust max_length dynamically if paragraph is short
        words_count = len(paragraph.split())
        adjusted_max_length = min(max_length, max(50, words_count // 2))
        
        summary = summarizer(paragraph, max_length=adjusted_max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error during summarization: {e}"

# Input paragraph
paragraph = """
Artificial Intelligence (AI) has been transforming industries across the globe. 
It allows machines to perform tasks that typically require human intelligence, such as decision-making, 
language understanding, and visual perception. AI is widely used in applications like healthcare, finance, 
education, and entertainment. With advancements in machine learning, AI systems are becoming more capable 
and versatile, helping businesses optimize operations and improve user experiences.
"""

# Generate summary
if paragraph.strip():
    summary = summarize_paragraph(paragraph)
    print("\nOriginal Paragraph:")
    print(paragraph.strip())
    print("\nSummarized Text:")
    print(summary)
else:
    print("No input paragraph provided. Please enter a valid text.")

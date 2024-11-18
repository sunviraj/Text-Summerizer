print("hello")

from transformers import pipeline

# Initialize the summarization pipeline
summarizer = pipeline("summarization")

def summarize_paragraph(paragraph, max_length=100, min_length=25):
    """
    Summarize a given paragraph using a pre-trained model.

    Parameters:
    paragraph (str): The input text to summarize.
    max_length (int): Maximum length of the summary.
    min_length (int): Minimum length of the summary.

    Returns:
    str: The summarized text.
    """
    try:
        summary = summarizer(paragraph, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"Error: {e}"

# Input paragraph
paragraph = """
Artificial Intelligence (AI) has been transforming industries across the globe. 
It allows machines to perform tasks that typically require human intelligence, such as decision-making, 
language understanding, and visual perception. AI is widely used in applications like healthcare, finance, 
education, and entertainment. With advancements in machine learning, AI systems are becoming more capable 
and versatile, helping businesses optimize operations and improve user experiences.
"""

# Generate summary
summary = summarize_paragraph(paragraph)
print("Original Paragraph:")
print(paragraph)
print("\nSummarized Text:")
print(summary)
Text Summarizer

A Python-based text summarization tool that uses a pre-trained model from the Hugging Face transformers library to generate concise summaries of input paragraphs.

Features

	•	Summarizes input paragraphs efficiently.
	•	Dynamically adjusts summary length based on the input.
	•	Utilizes the sshleifer/distilbart-cnn-12-6 model for high-quality summarization.
	•	Handles errors gracefully and provides helpful output messages.

Requirements

Before running the script, ensure you have the following installed:
	•	Python 3.7 or later
	•	Required Python libraries:
	•	transformers
	•	torch (optional for GPU acceleration)

To install the required libraries, run:
pip install transformers torch

Usage

	1.	Clone this repository: git clone https://github.com/<your-username>/<repo-name>.git
	2.	Navigate to the project directory: cd <repo-name>
	3.	Run the script: python3 summerizer.py
	4.	The script will:
	•	Display the original paragraph.
	•	Print the summarized text.

Code Overview

The main script (summerizer.py) contains:
	•	A summarize_paragraph function that takes a paragraph and returns its summarized version.
	•	Dynamic adjustment of max_length for improved summarization of shorter texts.
	•	Error handling for smoother execution.

Example Input: 
Artificial Intelligence (AI) has been transforming industries across the globe. 
It allows machines to perform tasks that typically require human intelligence, such as decision-making, 
language understanding, and visual perception. AI is widely used in applications like healthcare, finance, 
education, and entertainment. With advancements in machine learning, AI systems are becoming more capable 
and versatile, helping businesses optimize operations and improve user experiences.

Example Output:
Artificial Intelligence (AI) has been transforming industries across the globe. 
It allows machines to perform tasks that typically require human intelligence, such as decision-making and visual perception. 
AI is widely used in applications like healthcare, finance, and entertainment.





Future Enhancements

	•	Add support for batch summarization of multiple paragraphs.
	•	Enable GPU acceleration for faster processing.
	•	Integrate additional summarization models for customizable output styles.

Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

License

This project is licensed under the MIT License. See the LICENSE file for details.

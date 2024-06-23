# Import necessary libraries
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")

# Create a pipeline for sentiment analysis
nlp_pipeline = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# Example texts for analysis
texts = [
    "I love using Hugging Face models!",
    "This movie was terrible.",
    "The weather today is nice.",
    "I am feeling neutral about this.",
    "The product exceeded my expectations."
    "I love my life"
]

# Perform sentiment analysis for each text
for text in texts:
    print(f"Text: {text}")
    result = nlp_pipeline(text)
    print(f"Sentiment: {result}\n")

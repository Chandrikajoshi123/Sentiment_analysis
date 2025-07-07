import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from PIL import Image
import base64

# Define the available models
models = {
    "ROBERTA": "Abubakari/finetuned-Sentiment-classfication-ROBERTA-model",
    "BERT": "Abubakari/finetuned-Sentiment-classfication-BERT-model",
    "DISTILBERT": "Abubakari/finetuned-Sentiment-classfication-DISTILBERT-model"
}

# Select the model to use
model_name = "ROBERTA"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(models[model_name])
model = AutoModelForSequenceClassification.from_pretrained(models[model_name])

# Tokenize the input text
inputs = tokenizer("This is an example sentence.", return_tensors="pt")

# Make a forward pass
outputs = model(**inputs)

# ✅ Now safe to use 'outputs'
confidence_level = np.max(outputs.logits.detach().numpy())
predicted_class = outputs.logits.argmax().item()
score = outputs.logits.softmax(dim=1)[0][predicted_class].item()

print(f"Predicted class: {predicted_class}, Score: {score:.3f}")

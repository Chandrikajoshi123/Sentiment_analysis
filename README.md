# Sentiment Analysis API

![image](https://github.com/user-attachments/assets/e6b965b3-7bbd-4509-86fa-6f55745d90bb)


## Overview
This project builds a sentiment classifier on Amazon product reviews and serves it as a FastAPI Rest API.

## Tech Stack
- Python
- Scikit-learn (Naive Bayes Classifier)
- FastAPI( Rest API)
- Docker (containerization)

## Features
- Post/Predict -Accepts review text and return sentiment (Positive/negative/neutral)

## Project Structure
- `notebooks/` :Model training code
- `app/` : FastAPI app saved model
- `Dockerfile/` : Container for deployment

## Example request
```bash
curl -x Post http://localhost:8000/predict/ -H "Content-Type: application/json" -d '{"text": This product is amazing!}'

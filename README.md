# Sentiment Analysis API



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
```
## Results
- Macro ROC-AUC: 0.86
- Model: TF-IDF + Logistic Regression (class_weight=balanced)
- confusion matrix:

![image](https://github.com/user-attachments/assets/e12b3bd4-7039-450a-88a4-e59153033821)

## Challenges
- Dataset highly imbalanced ( Positive reviews dominated)
- Addressed via class weights

## Future Improvements
- Apply oversampling(SMOTE)
- Tray transformer model (DistilBERT/BERT)


  

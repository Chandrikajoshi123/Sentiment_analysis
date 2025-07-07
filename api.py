import joblib
model = joblib.load('../app/sentiment_model.pkl')
print(model)
from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
model_name=('sentiment_model.pkl')

app=FastAPI(
  title='Sentiment Analysis API',
  description='API for sentiment analysis',
  version='1.0'
 )

class ReviewText(BaseModel):
    text:str

@app.get("/")
def read_root():
     return {"message":"Welcome to the sentiment Analysis API. Use Post for sentimdent predictons"}

@app.post("/predict")
def predict_sentiment(data: ReviewText):
    review = data.text
    pred = model.predict([review])[0]
    proba = model.predict_proba([review])[0]
    return {
        "predicted_sentiment": pred,
        "confidence_scores": {
            "negative": round(float(proba[model.classes_ == 'negative'][0]), 3),
            "neutral": round(float(proba[model.classes_ == 'neutral'][0]), 3),
            "positive": round(float(proba[model.classes_ == 'positive'][0]), 3)
        }
    }
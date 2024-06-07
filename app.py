from fastapi import FastAPI, Request
from transformers import DistilBertForSequenceClassification, DistilBertTokenizer
import torch

app = FastAPI()

model_path = "./saved_model"
model = DistilBertForSequenceClassification.from_pretrained(model_path)
tokenizer = DistilBertTokenizer.from_pretrained(model_path)

@app.post("/predict")
async def predict(request: Request):
    request_data = await request.json()
    text = request_data.get("text")
    
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding='max_length', max_length=512)
    outputs = model(**inputs)
    predictions = torch.softmax(outputs.logits, dim=-1).tolist()[0]

    sentiment = "positive" if predictions[1] > predictions[0] else "negative"
    confidence = max(predictions)
    
    return {"sentiment": sentiment, "confidence": confidence}

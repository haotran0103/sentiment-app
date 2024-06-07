def predict_sentiment(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding='max_length', max_length=512)
    outputs = model(**inputs)
    predictions = outputs.logits.argmax(-1).item()
    return predictions

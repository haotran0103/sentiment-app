from src.textSentiments.components.model import get_model_and_tokenizer
from src.textSentiments.components.predict import predict_sentiment

def predict_pipeline(model_name: str, text: str):
    model, tokenizer = get_model_and_tokenizer(model_name)
    return predict_sentiment(text, model, tokenizer)

# Dùng để thử nghiệm và nghiên cứu mô hình
from src.textSentiments.components.data_loader import load_and_preprocess_data
from src.textSentiments.components.model import get_model_and_tokenizer, train_model

def run_experiments():
    dataset = load_and_preprocess_data("imdb")
    model, tokenizer = get_model_and_tokenizer("bert-base-uncased")
    train_model(model, tokenizer, dataset, epochs=3, learning_rate=2e-5)

if __name__ == "__main__":
    run_experiments()

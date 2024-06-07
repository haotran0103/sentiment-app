from src.textSentiments.components.data_loader import load_and_preprocess_data
from src.textSentiments.components.model import get_model_and_tokenizer, train_model
from src.textSentiments.config.configuration import get_config

def train_pipeline(config_path: str):
    config = get_config(config_path)
    dataset_name = config['dataset_name']
    model_name = config['model_name']
    epochs = config['epochs']
    learning_rate = config['learning_rate']

    dataset = load_and_preprocess_data(dataset_name)
    model, tokenizer = get_model_and_tokenizer(model_name)
    train_model(model, tokenizer, dataset, epochs, learning_rate)

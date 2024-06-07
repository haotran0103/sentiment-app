from src.textSentiments.utils.common import read_yaml

def get_config(config_path: str):
    return read_yaml(config_path)

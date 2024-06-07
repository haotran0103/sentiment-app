from dataclasses import dataclass

@dataclass
class DataConfig:
    dataset_name: str
    model_name: str
    epochs: int
    learning_rate: float

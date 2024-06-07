from datasets import load_dataset

def load_and_preprocess_data(dataset_name: str):
    dataset = load_dataset(dataset_name)
    # Thực hiện tiền xử lý dữ liệu tại đây
    return dataset

from transformers import BertForSequenceClassification, BertTokenizer, Trainer, TrainingArguments

def get_model_and_tokenizer(model_name: str):
    model = BertForSequenceClassification.from_pretrained(model_name, num_labels=2)
    tokenizer = BertTokenizer.from_pretrained(model_name)
    return model, tokenizer

def train_model(model, tokenizer, dataset, epochs: int, learning_rate: float):
    # Chuẩn bị dữ liệu cho huấn luyện
    train_dataset = dataset['train'].map(
        lambda e: tokenizer(e['text'], truncation=True, padding='max_length'),
        batched=True
    )
    eval_dataset = dataset['test'].map(
        lambda e: tokenizer(e['text'], truncation=True, padding='max_length'),
        batched=True
    )

    # Thiết lập huấn luyện
    training_args = TrainingArguments(
        output_dir='./results',
        num_train_epochs=epochs,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset,
    )

    # Huấn luyện mô hình
    trainer.train()

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import pandas as pd
import torch

def main(): #egitim
    print("CUDA is available:", torch.cuda.is_available())

    df = pd.read_csv("genisletilmis_mesaj_veriseti_50k.csv")

    df['Birim'] = df['Birim'].astype('category')
    df['label'] = df['Birim'].cat.codes

    dataset = Dataset.from_pandas(df[['Mesaj', 'label']].rename(columns={'Mesaj': 'text'}))

    model_name = "distilbert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    def tokenize_function(example):
        return tokenizer(example["text"], padding="max_length", truncation=True, max_length=128)

    tokenized_dataset = dataset.map(tokenize_function, batched=True)

    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(df['Birim'].unique()))

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="no",
        learning_rate=5e-5,
        per_device_train_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_dir='./logs',
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
    )

    trainer.train()

    model.save_pretrained("./results")
    tokenizer.save_pretrained("./results")

if __name__ == "__main__":
    main()

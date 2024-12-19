from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import pandas as pd
import torch

def main():
    # Veri setini yükleme
    df = pd.read_csv("genisletilmis_mesaj_veriseti_50k.csv")

    # Label'ları kategorik numaralara çevirme
    df['Birim'] = df['Birim'].astype('category')
    df['label'] = df['Birim'].cat.codes

    # Dataset formatına dönüştürme
    dataset = Dataset.from_pandas(df[['Mesaj', 'label']].rename(columns={'Mesaj': 'text'}))

    # Tokenizer yükleme
    model_name = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    # Tokenize fonksiyonu
    def tokenize_function(example):
        return tokenizer(example["text"], padding="max_length", truncation=True)

    # Dataset'i tokenize etme
    tokenized_dataset = dataset.map(tokenize_function, batched=True)

    # Modeli yükleme
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=len(df['Birim'].unique()))

    # Eğitim ayarları
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=4,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_dir='./logs',
    )

    # Trainer oluşturma
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        eval_dataset=tokenized_dataset,
    )

    # Modeli eğitme
    trainer.train()

    # Tahmin yapma fonksiyonu
    def predict_message(message):
        # Mesajı tokenize et
        inputs = tokenizer(message, return_tensors="pt", padding=True, truncation=True, max_length=512)
        # Model tahmini
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class = torch.argmax(logits, dim=1).item()
        # Kategori adını getir
        label_map = dict(enumerate(df['Birim'].cat.categories))
        return label_map[predicted_class]

    # Örnek tahminler
    messages = [
        "Kargom nerede öğrenmek istiyorum.",
        "Teknik destek alabilir miyim?",
        "Fatura detaylarımı göremiyorum.",
    ]

    for msg in messages:
        print(f"Mesaj: '{msg}' -> Tahmin Edilen Birim: {predict_message(msg)}")

if __name__ == "__main__":
    main()

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd

# Etiketleri yüklemek için CSV dosyasını tekrar okuyun
df = pd.read_csv("genisletilmis_mesaj_veriseti_50k.csv")
df['Birim'] = df['Birim'].astype('category')

def predict(text):
    # Modeli ve tokenizer'ı yükleyin
    model_name = "./results"  # Eğitilmiş modelin çıktısının yolu
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)

    # Modeli değerlendirme moduna ayarlayın
    model.eval()

    # Girdi metinlerini tokenize edin
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Modeli kullanarak tahminler alın
    with torch.no_grad():
        outputs = model(**inputs)
        predictions = torch.argmax(outputs.logits, dim=-1)

    # Sonuçları yorumlayın
    labels = df['Birim'].cat.categories
    predicted_label = labels[predictions.item()]
    return predicted_label

if __name__ == "__main__":
    # Konsoldan kullanıcı girdisi alın
    user_input = input("Sınıflandırmak istediğiniz metni girin: ")
    prediction = predict(user_input)
    print(f"Tahmin edilen etiket: {prediction}")

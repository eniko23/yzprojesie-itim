import pandas as pd

# Veri setini yükleyin
df = pd.read_csv("benzersiz_veri_seti.csv")

# Tekrarlanan satırları kontrol edin
duplicates = df[df.duplicated()]
print("Tekrarlanan satır sayısı:", len(duplicates))

# Tekrarlanan satırları çıkarın
df_cleaned = df.drop_duplicates()
print("Temizlenmiş veri seti boyutu:", df_cleaned.shape)

# Temizlenmiş veri setini kaydedin (istenirse)
df_cleaned.to_csv("temizlenmis_mesaj_veriseti.csv", index=False)

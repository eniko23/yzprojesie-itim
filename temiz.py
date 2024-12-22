import pandas as pd

df = pd.read_csv("benzersiz_veri_seti.csv")

duplicates = df[df.duplicated()]
print("Tekrarlanan satır sayısı:", len(duplicates))

df_cleaned = df.drop_duplicates()
print("Temizlenmiş veri seti boyutu:", df_cleaned.shape)

df_cleaned.to_csv("temizlenmis_mesaj_veriseti.csv", index=False)

import csv
import random

templates = {
    "IT": [
        "{personel} bugün {action} ile ilgili bir sorun çözdü.",
        "Sistem {time} boyunca {state} durumda kaldı.",
        "Yeni {tool} kurulumu başarıyla tamamlandı."
    ],
    "İşçi": [
        "Üretim hattında {machine} {action} yapıldı.",
        "Yeni {material} depoya {time} ulaştırıldı.",
        "Vardiya sırasında {problem} ile karşılaşıldı."
    ],
    "Temizlik": [
        "{area} temizliği {time} tamamlandı.",
        "{material} ile tüm {object} detaylıca temizlendi.",
        "{task} sırasında {problem} meydana geldi."
    ],
    "Yönetici": [
        "{meeting} toplantısı {time} yapıldı.",
        "Yeni {policy} çalışanlara duyuruldu.",
        "{process} değerlendirmesi tamamlandı."
    ]
}

words = {
    "personel": ["Ahmet", "Ayşe", "Mehmet", "Elif", "Kemal"],
    "action": ["bakım", "güncelleme", "onarım"],
    "time": ["sabah", "öğleden sonra", "akşam"],
    "state": ["aktif", "bakımda", "kapalı"],
    "tool": ["yazılım", "sunucu", "ağ cihazı"],
    "machine": ["pres makinesi", "montaj bandı", "robot kol"],
    "material": ["hammadde", "parça", "paket"],
    "problem": ["arıza", "gecikme", "hata"],
    "area": ["ofis", "depo", "fabrika sahası"],
    "object": ["zemin", "raf", "cam"],
    "task": ["temizlik", "dezenfeksiyon"],
    "meeting": ["strateji", "performans", "güvenlik"],
    "policy": ["güvenlik politikası", "çalışma kılavuzu"],
    "process": ["üretim", "dağıtım"]
}

def generate_sentence(template, words):
    return template.format(**{key: random.choice(values) for key, values in words.items() if f"{{{key}}}" in template})

unique_sentences = set()
for category, templates_list in templates.items():
    while len(unique_sentences) < 12500 * len(templates):
        for template in templates_list:
            sentence = generate_sentence(template, words)
            unique_sentences.add((category, sentence))

csv_file_path = "factory_unique_sentences.csv"
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Birim", "Cümle"])
    writer.writerows(unique_sentences)

print(f"CSV dosyası oluşturuldu: {csv_file_path}")

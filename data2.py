import csv
import random

# Cümle şablonları ve kelime havuzları
templates = {
    "IT": [
        "{personel} bugün {action} ile ilgili bir sorun çözdü.",
        "Sistem {time} boyunca {state} durumda kaldı.",
        "Yeni {tool} kurulumu başarıyla tamamlandı.",
        "Ağ {time} boyunca kesintiye uğradı.",
        "{personel} {tool} için {action} işlemi başlattı."
    ],
    "İşçi": [
        "Üretim hattında {machine} {action} yapıldı.",
        "Yeni {material} depoya {time} ulaştırıldı.",
        "Vardiya sırasında {problem} ile karşılaşıldı.",
        "Makine {action} sırasında {problem} oluştu.",
        "{worker} için {task} süreci başarıyla tamamlandı."
    ],
    "Temizlik": [
        "{area} temizliği {time} tamamlandı.",
        "{material} ile tüm {object} detaylıca temizlendi.",
        "{task} sırasında {problem} meydana geldi.",
        "Yemekhane temizliği saat {time} yapıldı.",
        "Fabrika sahasında {task} işlemi başarıyla yapıldı."
    ],
    "Yönetici": [
        "{meeting} toplantısı {time} yapıldı.",
        "Yeni {policy} çalışanlara duyuruldu.",
        "{process} değerlendirmesi tamamlandı.",
        "Yönetici {manager} yeni bir {policy} önerdi.",
        "Fabrika hedefleri {time} içinde gözden geçirildi."
    ]
}

# Gelişmiş kelime havuzları
words = {
    "personel": ["Ahmet", "Ayşe", "Mehmet", "Elif", "Kemal", "Serdar", "Leyla", "Hasan", "Zeynep", "Fatma", "Burak", "Seda", "Veli", "Murat", "Nazan"],
    "action": ["bakım", "güncelleme", "onarım", "test", "iyileştirme", "kontrol", "yükseltme", "denetleme", "optimizasyon", "düzeltme"],
    "time": ["sabah", "öğleden sonra", "akşam", "gece", "bugün", "bu hafta", "yıl sonunda", "dün", "bu ay", "önümüzdeki hafta"],
    "state": ["aktif", "bakımda", "kapalı", "çalışıyor", "kapalı", "devre dışı", "hizmet dışı"],
    "tool": ["yazılım", "sunucu", "ağ cihazı", "bilgisayar", "yazıcı", "veritabanı", "işletim sistemi", "program", "donanım", "yazılım geliştirme aracı"],
    "machine": ["pres makinesi", "montaj bandı", "robot kol", "forklift", "laser kesim makinesi", "konveyör", "kaynak makinesi", "makine parkı", "el işleme robotu"],
    "material": ["hammadde", "parça", "paket", "kimyasal", "plastik malzeme", "metal levha", "lastik", "elektronik bileşen", "alüminyum", "içerik malzemesi"],
    "problem": ["arıza", "gecikme", "hata", "sistem sorunu", "donma", "yavaşlama", "kapanma", "elektrik kesintisi", "bağlantı problemi"],
    "area": ["ofis", "depo", "fabrika sahası", "yemekhane", "yönetici odası", "toplantı odası", "tuvaletler", "iş sahası", "veri odası"],
    "object": ["zemin", "raf", "cam", "duvar", "kapı", "pencere", "koridor", "tavan", "aydınlatma", "koltuk"],
    "task": ["temizlik", "dezenfeksiyon", "bakım", "onarım", "denetim", "gözetim", "düzenleme", "kontrol", "deneysel çalışma"],
    "worker": ["işçi", "teknisyen", "eleman", "operatör", "uzman", "servis teknisyeni", "bakım personeli", "çalışan", "imalat işçisi", "denetçi"],
    "meeting": ["strateji", "performans", "güvenlik", "planlama", "değerlendirme", "yönetim", "toplantı", "revizyon", "paylaşım", "kriz yönetimi"],
    "policy": ["güvenlik politikası", "çalışma kılavuzu", "çalışan hakları", "yönetim politikası", "çevre politikası", "iş güvenliği", "veri koruma politikası"],
    "process": ["üretim", "dağıtım", "imalat", "planlama", "geliştirme", "test", "işlemler", "denetim", "teknoloji entegrasyonu"],
    "manager": ["Ahmet", "Ayşe", "Mehmet", "Serdar", "Leyla", "Burak", "Murat", "Nazan", "Veli", "Seda"]
}

# Rastgele cümle oluşturucu
def generate_sentence(template, words):
    return template.format(**{key: random.choice(values) for key, values in words.items() if f"{{{key}}}" in template})

# Veri seti oluşturma
unique_sentences = set()
total_sentences = 50000  # Toplamda 50.000 cümle
unit_count = total_sentences // len(templates)  # Her birim için eşit sayıda cümle

for category, templates_list in templates.items():
    while len(unique_sentences) < unit_count * len(templates):
        for template in templates_list:
            sentence = generate_sentence(template, words)
            unique_sentences.add((category, sentence))

# CSV'ye kaydetme
csv_file_path = "factory_unique_sentences.csv"
with open(csv_file_path, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Birim", "Cümle"])
    writer.writerows(unique_sentences)

print(f"CSV dosyası oluşturuldu: {csv_file_path}")

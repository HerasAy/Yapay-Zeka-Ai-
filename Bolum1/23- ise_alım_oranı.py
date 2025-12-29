import pandas as pd

# Simüle Edilmiş "Geçmiş İşe Alım" Verisi
# Erkeklerin %80'i işe alınmış, Kadınların %20'si.
data = [
    {'Cinsiyet': 'Erkek', 'Tecrübe': 5, 'İşe_Alındı': 1},
    {'Cinsiyet': 'Erkek', 'Tecrübe': 2, 'İşe_Alındı': 1},
    {'Cinsiyet': 'Erkek', 'Tecrübe': 3, 'İşe_Alındı': 0},
    {'Cinsiyet': 'Erkek', 'Tecrübe': 5, 'İşe_Alındı': 1},
    {'Cinsiyet': 'Kadın', 'Tecrübe': 5, 'İşe_Alındı': 0}, # Aynı tecrübe, red!
    {'Cinsiyet': 'Kadın', 'Tecrübe': 4, 'İşe_Alındı': 0},
    {'Cinsiyet': 'Kadın', 'Tecrübe': 6, 'İşe_Alındı': 1},
    {'Cinsiyet': 'Kadın', 'Tecrübe': 2, 'İşe_Alındı': 0},
]
df = pd.DataFrame(data)

# Basit İstatistiksel Analiz
bias_check = df.groupby('Cinsiyet')['İşe_Alındı'].mean()

print("--- İşe Alım Oranları (Bias Kontrolü) ---")
print(bias_check)

# Kural Tabanlı (Naive) Bir Model Yaparsak:
def biased_model(gender, experience):
    # Veriye bakan model şunu öğrenir: "Erkekse şansı yüksek"
    if gender == 'Erkek':
        return "Yüksek İhtimalle İşe Alınır"
    else:
        return "Düşük İhtimal"

print("\nModel Kararı:")
print(f"5 Yıllık Erkek: {biased_model('Erkek', 5)}")
print(f"5 Yıllık Kadın: {biased_model('Kadın', 5)}")

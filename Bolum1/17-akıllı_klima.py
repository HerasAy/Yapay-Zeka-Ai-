import numpy as np
import matplotlib.pyplot as plt

# Üçgen Üyelik Fonksiyonu
def triangular(x, a, b, c):
    """
    a: Başlangıç, b: Tepe, c: Bitiş
    """
    return np.maximum(0, np.minimum((x-a)/(b-a), (c-x)/(c-b)))

# X ekseni aralıkları
x_temp = np.linspace(0, 40, 100) # 0-40 Derece
x_fan  = np.linspace(0, 100, 100) # %0-%100 Hız

# Üyelik Kümeleri (Sıcaklık)
temp_cold = triangular(x_temp, 0, 0, 20)
temp_warm = triangular(x_temp, 15, 25, 35)
temp_hot  = triangular(x_temp, 30, 40, 40)

# Görselleştirme (Opsiyonel ama önerilir)
plt.plot(x_temp, temp_cold, label="Soğuk")
plt.plot(x_temp, temp_warm, label="Ilık")
plt.plot(x_temp, temp_hot, label="Sıcak")
plt.legend()
plt.title("Sıcaklık Üyelik Fonksiyonları")
plt.show() # Notebook'ta grafiği gösterir

def fuzzy_controller(input_temp):
    # 1. BULANIKLAŞTIRMA (Fuzzification)
    # Gelen sıcaklığın hangi kümeye ne kadar ait olduğunu bul
    mu_cold = np.interp(input_temp, x_temp, temp_cold)
    mu_warm = np.interp(input_temp, x_temp, temp_warm)
    mu_hot  = np.interp(input_temp, x_temp, temp_hot)

    print(f"Giriş: {input_temp}°C -> Soğuk:{mu_cold:.2f}, Ilık:{mu_warm:.2f}, Sıcak:{mu_hot:.2f}")

    # 2. KURAL TABANI VE ÇIKARIM (Inference)
    # Kural 1: Eğer Soğuk ise -> Fan Düşük
    # Kural 2: Eğer Ilık ise  -> Fan Orta
    # Kural 3: Eğer Sıcak ise -> Fan Yüksek

    # Mamdani Yöntemi (Basitleştirilmiş): Kuralın gücü, çıktı kümesini o seviyede keser (clip).
    # Burada ağırlıklı ortalama (Centroid) mantığına giden basit bir yol izleyeceğiz.

    # Çıktı kümelerinin temsili değerleri (Centroids)
    fan_low_val = 20
    fan_med_val = 50
    fan_high_val = 80

    # Ağırlıklı Ortalama (Defuzzification - Center of Gravity yaklaşımı)
    # Pay: (Üyelik * Değer) toplamı
    numerator = (mu_cold * fan_low_val) + (mu_warm * fan_med_val) + (mu_hot * fan_high_val)
    # Payda: Üyelik toplamı
    denominator = mu_cold + mu_warm + mu_hot

    if denominator == 0: return 0 # Tanımsız durum

    result_fan_speed = numerator / denominator
    return result_fan_speed

# Test Edelim
temp_input = 28 # Derece
fan_speed = fuzzy_controller(temp_input)
print(f"Sonuç: Fan Hızı %{fan_speed:.2f} olmalı.")

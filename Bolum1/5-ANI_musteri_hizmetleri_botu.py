import re

class NarrowAIBot:
    def __init__(self):
        # ANI'nin "Uzmanlık" Alanı: Anahtar kelime eşleştirme
        self.knowledge_base = {
            r".*iade.*": "İade işlemleri için sipariş numaranızı giriniz.",
            r".*sipariş.*": "Siparişiniz kargoya verildi, takip no: 123456.",
            r".*fiyat.*": "Ürün fiyatlarımız web sitesinde günceldir."
        }

    def respond(self, user_input):
        """
        Sadece tanımlı regex kurallarına (Narrow Domain) göre cevap verir.
        Genel zekası yoktur.
        """
        user_input = user_input.lower()

        for pattern, response in self.knowledge_base.items():
            if re.match(pattern, user_input):
                return f"[BOT]: {response}"

        # Alanı dışına çıkıldığında başarısız olur
        return "[BOT]: Üzgünüm, bunu anlayamadım. Ben sadece bir sipariş botuyum."

# Simülasyon
def test_ani_limits():
    bot = NarrowAIBot()

    questions = [
        "Sipariş durumum nedir?",   # Alan içi (Başarılı)
        "Ürünü iade etmek istiyorum", # Alan içi (Başarılı)
        "Hayatın anlamı nedir?",      # Alan dışı (Genel Zekâ gerektirir - Başarısız)
        "2 + 2 kaç eder?"             # Alan dışı (Matematik yeteneği yok - Başarısız)
    ]

    print(f"{'KULLANICI GİRDİSİ':<30} | {'BOT CEVABI'}")
    print("-" * 80)

    for q in questions:
        print(f"{q:<30} | {bot.respond(q)}")

test_ani_limits()

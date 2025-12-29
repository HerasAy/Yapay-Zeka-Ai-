import random
from collections import defaultdict

class NGramModel:
    def __init__(self, n=2):
        self.n = n
        # Sözlük yapısı: { ('kelime1', 'kelime2'): ['kelime3', 'kelime4'] }
        self.model = defaultdict(list)

    def train(self, text):
        """Metni okur ve kelime dizilerini öğrenir"""
        tokens = text.split()

        # N-Gramları oluştur
        for i in range(len(tokens) - self.n):
            # Geçmiş (n tane kelime)
            history = tuple(tokens[i : i + self.n])
            # Gelecek (Bir sonraki kelime)
            next_word = tokens[i + self.n]

            self.model[history].append(next_word)

    def generate(self, start_words, length=20):
        """Öğrendiklerine dayanarak yeni metin üretir"""
        current_history = tuple(start_words.split())
        output = list(current_history)

        for _ in range(length):
            if current_history in self.model:
                # Olası devam kelimelerinden birini rastgele seç
                next_word = random.choice(self.model[current_history])
                output.append(next_word)

                # Geçmişi kaydır (Pencereyi ilerlet)
                current_history = tuple(output[-self.n:])
            else:
                break # Zincir koptu

        return " ".join(output)

# --- Test ---
# Örnek Veri (Basit bir tekerleme veya metin)
corpus = """
Yapay zeka geleceği şekillendiriyor. Yapay zeka insanlığa yardımcı olacak.
Geleceği şekillendiriyor çünkü teknoloji hızla gelişiyor.
Teknoloji hızla gelişiyor ve insanlığa yeni kapılar açıyor.
"""

# Modeli Eğit (Bigram: 2 kelimeye bak, 3.yü tahmin et)
bot = NGramModel(n=2)
bot.train(corpus)

# Üretim Yap
print("--- Üretilen Metin ---")
print(bot.generate("Yapay zeka", length=10))

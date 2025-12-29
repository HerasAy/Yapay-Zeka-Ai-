import random
import string

TARGET = "YAPAY ZEKA"
POPULATION_SIZE = 100
GENES = string.ascii_uppercase + " " # Kullanılabilecek harfler

class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.calculate_fitness()

    @classmethod
    def create_gnome(cls):
        """Rastgele genlerden oluşan bir birey yarat"""
        return [random.choice(GENES) for _ in range(len(TARGET))]

    def calculate_fitness(self):
        """
        Hedefe ne kadar benziyor?
        Her doğru harf için +1 puan.
        """
        score = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == TARGET[i]:
                score += 1
        return score

    def mate(self, partner):
        """
        İki bireyden yeni bir çocuk (Crossover) üret.
        Her gen için %45 anne, %45 baba, %10 mutasyon ihtimali.
        """
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, partner.chromosome):
            prob = random.random()
            if prob < 0.45:
                child_chromosome.append(gp1)
            elif prob < 0.90:
                child_chromosome.append(gp2)
            else:
                child_chromosome.append(random.choice(GENES)) # Mutasyon
        return Individual(child_chromosome)

# --- Evrim Simülasyonu ---
generation = 1
population = [Individual(Individual.create_gnome()) for _ in range(POPULATION_SIZE)]

while True:
    # 1. Popülasyonu puana göre sırala (En iyi en üstte)
    population = sorted(population, key=lambda x: x.fitness, reverse=True)

    # En iyiyi yazdır
    best_ind = population[0]
    print(f"Nesil: {generation} | Şifre: {''.join(best_ind.chromosome)} | Puan: {best_ind.fitness}")

    # Çözüm bulundu mu?
    if best_ind.fitness == len(TARGET):
        break

    # 2. Yeni Nesil Üretimi
    new_generation = []

    # Elitizm: En iyi %10 doğrudan yeni nesle geçer (ölümsüzlük)
    s = int((10*POPULATION_SIZE)/100)
    new_generation.extend(population[:s])

    # Kalan %90, en iyiler arasından çiftleşerek üretilir
    s = int((90*POPULATION_SIZE)/100)
    for _ in range(s):
        parent1 = random.choice(population[:50]) # İlk 50'den seç
        parent2 = random.choice(population[:50])
        child = parent1.mate(parent2)
        new_generation.append(child)

    population = new_generation
    generation += 1

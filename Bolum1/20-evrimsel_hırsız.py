import random

# --- Problem Tanımı ---
# (Eşya Adı, Değer ($), Ağırlık (kg))
ITEMS = [
    ("Laptop", 500, 3), ("Kulaklık", 150, 1), ("Kahve Makinesi", 60, 5),
    ("Tablo", 1000, 8), ("Heykel", 400, 10), ("Altın Külçe", 800, 2),
    ("Gitar", 300, 4), ("Antika Saat", 450, 2), ("Kitap Seti", 50, 6),
    ("Pırlanta", 2000, 1)
]
MAX_WEIGHT = 15 # Çanta kapasitesi
POPULATION_SIZE = 50
GENERATIONS = 100
MUTATION_RATE = 0.1

class Individual:
    def __init__(self, chromosome=None):
        if chromosome is None:
            # Rastgele başlangıç: %50 ihtimalle eşyayı al ya da alma
            self.chromosome = [random.randint(0, 1) for _ in range(len(ITEMS))]
        else:
            self.chromosome = chromosome
        self.fitness = self.get_fitness()

    def get_fitness(self):
        total_value = 0
        total_weight = 0
        for i in range(len(self.chromosome)):
            if self.chromosome[i] == 1:
                total_value += ITEMS[i][1]
                total_weight += ITEMS[i][2]

        # CEZA MEKANİZMASI: Çanta kapasitesini aşarsa fitness 0 olur (Ölür)
        if total_weight > MAX_WEIGHT:
            return 0
        return total_value

def selection(population):
    # Turnuva Seçimi: Rastgele 3 kişi seç, en iyisini al
    tournament = random.sample(population, 3)
    return max(tournament, key=lambda x: x.fitness)

def crossover(parent1, parent2):
    # Tek Noktalı Çaprazlama
    point = random.randint(1, len(ITEMS)-1)
    child_chrom = parent1.chromosome[:point] + parent2.chromosome[point:]
    return Individual(child_chrom)

def mutation(individual):
    # Genetik çeşitlilik için bit çevirme (Bit Flip)
    for i in range(len(individual.chromosome)):
        if random.random() < MUTATION_RATE:
            individual.chromosome[i] = 1 - individual.chromosome[i] # 1->0 veya 0->1
    # Fitness'ı yeniden hesapla
    individual.fitness = individual.get_fitness()

# --- Ana Döngü ---
population = [Individual() for _ in range(POPULATION_SIZE)]

for gen in range(GENERATIONS):
    # 1. Sıralama
    population = sorted(population, key=lambda x: x.fitness, reverse=True)

    # En iyiyi göster
    if gen % 20 == 0:
        best = population[0]
        weight = sum(ITEMS[i][2] for i in range(len(ITEMS)) if best.chromosome[i] == 1)
        print(f"Nesil {gen:<3} | Değer: ${best.fitness:<4} | Ağırlık: {weight}kg")

    # 2. Yeni Nesil (Elitizm: En iyi 2 kişiyi aynen koru)
    new_gen = population[:2]

    while len(new_gen) < POPULATION_SIZE:
        p1 = selection(population)
        p2 = selection(population)
        child = crossover(p1, p2)
        mutation(child)
        new_gen.append(child)

    population = new_gen

# --- Sonuç ---
best_sol = population[0]
print("\n--- EN İYİ ÇÖZÜM ---")
print(f"Toplam Değer: ${best_sol.fitness}")
print("Alınan Eşyalar:")
total_w = 0
for i, gene in enumerate(best_sol.chromosome):
    if gene == 1:
        print(f"- {ITEMS[i][0]} (${ITEMS[i][1]}, {ITEMS[i][2]}kg)")
        total_w += ITEMS[i][2]
print(f"Toplam Ağırlık: {total_w} / {MAX_WEIGHT} kg")

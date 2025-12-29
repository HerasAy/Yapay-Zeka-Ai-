import random

# Hedef Fonksiyon: f(x) = x^2 (Minimum noktası x=0'dır)
def cost_function(x):
    return x ** 2

class Particle:
    def __init__(self):
        self.position = random.uniform(-10, 10) # Rastgele başlangıç (-10 ile 10 arası)
        self.velocity = random.uniform(-1, 1)
        self.pBest_pos = self.position
        self.pBest_val = cost_function(self.position)

    def update(self, gBest_pos, w=0.5, c1=1.5, c2=1.5):
        r1 = random.random()
        r2 = random.random()

        # Hız Güncelleme (Formülün kod hali)
        cognitive = c1 * r1 * (self.pBest_pos - self.position)
        social    = c2 * r2 * (gBest_pos - self.position)
        self.velocity = (w * self.velocity) + cognitive + social

        # Pozisyon Güncelleme
        self.position += self.velocity

        # pBest Güncelleme
        current_val = cost_function(self.position)
        if current_val < self.pBest_val:
            self.pBest_val = current_val
            self.pBest_pos = self.position

# --- PSO Algoritması ---
swarm_size = 15
particles = [Particle() for _ in range(swarm_size)]

# Başlangıç gBest
gBest_pos = particles[0].position
gBest_val = particles[0].pBest_val

print(f"Başlangıç En İyi Konum: {gBest_pos:.4f} (Hata: {gBest_val:.4f})")

for i in range(20): # 20 iterasyon
    # Sürüdeki en iyi değeri bul (Global Best)
    for p in particles:
        if p.pBest_val < gBest_val:
            gBest_val = p.pBest_val
            gBest_pos = p.pBest_pos

    # Her parçacığı güncelle
    for p in particles:
        p.update(gBest_pos)

    print(f"İterasyon {i+1:<2} | gBest x: {gBest_pos:.6f} | Değer: {gBest_val:.8f}")

print("\nBulunan Minimum Nokta:", round(gBest_pos, 5))

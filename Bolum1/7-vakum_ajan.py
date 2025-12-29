import random

class Environment:
    def __init__(self, width=5, height=5):
        self.width = width
        self.height = height
        # 0: Temiz, 1: Kirli
        self.grid = [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)]

    def is_dirty(self, x, y):
        return self.grid[y][x] == 1

    def clean(self, x, y):
        self.grid[y][x] = 0

    def display(self, agent_pos):
        print("\n--- ORTAM DURUMU ---")
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                cell = "🤢" if self.grid[y][x] == 1 else "✨"
                if (x, y) == agent_pos:
                    cell = "🤖" # Ajanın konumu
                line += cell + " "
            print(line)

class VacuumAgent:
    def __init__(self, env):
        self.env = env
        self.x = 0
        self.y = 0
        self.performance = 0

    def sense_and_act(self):
        # 1. SENSÖR: Bulunduğum yer kirli mi?
        if self.env.is_dirty(self.x, self.y):
            print(f"Konum ({self.x}, {self.y}) kirli. TEMİZLENİYOR...")
            self.env.clean(self.x, self.y)
            self.performance += 10 # Ödül
            return "CLEAN"

        # 2. HAREKET (Basit Rastgele Gezinti)
        else:
            move = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

            if move == "UP" and self.y > 0: self.y -= 1
            elif move == "DOWN" and self.y < self.env.height - 1: self.y += 1
            elif move == "LEFT" and self.x > 0: self.x -= 1
            elif move == "RIGHT" and self.x < self.env.width - 1: self.x += 1

            self.performance -= 1 # Enerji maliyeti
            print(f"Konum temiz. Hareket ediliyor: {move}")
            return "MOVE"

# Simülasyonu Çalıştır
env = Environment(3, 3) # 3x3 bir oda
bot = VacuumAgent(env)

for i in range(5):
    env.display((bot.x, bot.y))
    bot.sense_and_act()

print(f"\nToplam Performans Puanı: {bot.performance}")

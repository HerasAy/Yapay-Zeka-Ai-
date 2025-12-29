import matplotlib.pyplot as plt
import numpy as np
from queue import PriorityQueue

# --- 1. Labirent Ortamı (Environment) ---
class Maze:
    def __init__(self, size=20, obstacle_ratio=0.3):
        self.size = size
        # 0: Boş, 1: Duvar
        self.grid = np.zeros((size, size))
        self.start = (0, 0)
        self.end = (size-1, size-1)

        # Rastgele Duvarlar Ekle
        for i in range(size):
            for j in range(size):
                if (i, j) != self.start and (i, j) != self.end:
                    if np.random.rand() < obstacle_ratio:
                        self.grid[i][j] = 1

    def draw(self, path=None):
        plt.figure(figsize=(6, 6))
        plt.imshow(self.grid, cmap='Greys')

        # Başlangıç (Yeşil) ve Bitiş (Kırmızı)
        plt.plot(self.start[1], self.start[0], 'go', markersize=10, label='Başlangıç')
        plt.plot(self.end[1], self.end[0], 'ro', markersize=10, label='Bitiş')

        # Eğer bir yol bulunduysa çiz
        if path:
            y_coords = [p[0] for p in path]
            x_coords = [p[1] for p in path]
            plt.plot(x_coords, y_coords, 'b-', linewidth=2, label='Ajan Rotası')

        plt.legend()
        plt.grid(which='both', color='gray', linestyle='-', linewidth=0.5)
        plt.show()

# --- 2. A* Arama Ajanı (Agent) ---
def heuristic(a, b):
    # Manhattan Mesafesi (Kareli düzlem için ideal)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solve_maze(maze):
    start = maze.start
    end = maze.end
    grid = maze.grid
    size = maze.size

    frontier = PriorityQueue()
    frontier.put((0, start))

    came_from = {start: None}
    cost_so_far = {start: 0}

    while not frontier.empty():
        _, current = frontier.get()

        if current == end:
            break # Hedefe ulaşıldı

        # Komşulara bak (Yukarı, Aşağı, Sol, Sağ)
        neighbors = []
        x, y = current
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < size and 0 <= ny < size: # Sınır kontrolü
                if grid[nx][ny] == 0: # Duvar değilse
                    neighbors.append((nx, ny))

        for next_node in neighbors:
            new_cost = cost_so_far[current] + 1
            if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                priority = new_cost + heuristic(end, next_node)
                frontier.put((priority, next_node))
                came_from[next_node] = current

    # Yolu geri oluştur (Backtracking)
    if end not in came_from:
        return None # Yol yok

    path = []
    curr = end
    while curr != start:
        path.append(curr)
        curr = came_from[curr]
    path.append(start)
    return path[::-1] # Tersten çevir

# --- 3. Çalıştırma ---
# Rastgele bir labirent oluştur
my_maze = Maze(size=15, obstacle_ratio=0.25)

# Ajanı çalıştır
solution_path = solve_maze(my_maze)

if solution_path:
    print(f"Hedefe ulaşıldı! Yol uzunluğu: {len(solution_path)} adım.")
    my_maze.draw(solution_path)
else:
    print("Bu labirentin çözümü yok (Duvarlar yolu kapatmış). Tekrar deneyin.")

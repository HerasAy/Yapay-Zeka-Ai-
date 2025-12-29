import math
from queue import PriorityQueue

# Şehir Koordinatları (x, y)
romania_locations = {
    'Arad': (91, 492), 'Zerind': (75, 574), 'Oradea': (131, 571),
    'Sibiu': (207, 457), 'Fagaras': (305, 449), 'Rimnicu': (233, 410),
    'Pitesti': (320, 368), 'Timisoara': (94, 410), 'Lugoj': (165, 379),
    'Mehadia': (168, 339), 'Drobeta': (165, 299), 'Craiova': (253, 288),
    'Bucharest': (400, 327), 'Giurgiu': (375, 270)
}

def euclidean_distance(node_state, goal_state):
    """
    İki şehir arasındaki kuş uçuşu mesafeyi (Öklid) hesaplar.
    h(n) fonksiyonumuz budur.
    """
    x1, y1 = romania_locations[node_state]
    x2, y2 = romania_locations[goal_state]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Greedy Best-First Algoritması
def greedy_best_first_search(problem, h=None):
    """
    h(n) değerine göre en düşük olanı seçer.
    """
    # Priority Queue: (Öncelik Puanı, Düğüm) şeklinde saklar
    frontier = PriorityQueue()

    # Başlangıç düğümü
    initial_node = Node(problem.initial)
    # Öncelik = heuristic değeri
    priority = h(initial_node.state, problem.goal)

    frontier.put((priority, initial_node))
    explored = set()

    while not frontier.empty():
        # En düşük h(n) değerine sahip düğümü al
        _, node = frontier.get()

        if problem.is_goal(node.state):
            return node.path()

        explored.add(node.state)

        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)
            if child_state not in explored:
                child = Node(child_state, node, action)
                # Greedy sadece h(n)'e bakar
                priority = h(child_state, problem.goal)
                frontier.put((priority, child))

    return None

from collections import deque

# Düğüm (Node) Sınıfı: Arama ağacındaki her bir noktayı temsil eder
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def path(self):
        # Kökten bu düğüme kadar olan yolu geri izler
        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return list(reversed(path_back))

# 1. Genişlik Öncelikli Arama (BFS)
def breadth_first_search(problem):
    node = Node(problem.initial)

    # Başlangıçta hedefte miyiz?
    if problem.is_goal(node.state):
        return node.path()

    frontier = deque([node]) # FIFO Kuyruk
    explored = set()         # Ziyaret edilenler (Döngüye girmemek için)

    while frontier:
        node = frontier.popleft() # Kuyruğun başından al
        explored.add(node.state)

        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)

            # Eğer çocuk daha önce görülmediyse
            if child_state not in explored and \
               child_state not in [n.state for n in frontier]:

                child = Node(child_state, node, action)

                # Hedef kontrolü (BFS'de üretildiği an bakılır)
                if problem.is_goal(child.state):
                    return child.path()

                frontier.append(child)
    return None

# 2. Derinlik Öncelikli Arama (DFS)
def depth_first_search(problem):
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node.path()

    frontier = [node] # Stack (LIFO) - Python listesi stack gibidir
    explored = set()

    while frontier:
        node = frontier.pop() # Listenin sonundan al (En son eklenen)
        explored.add(node.state)

        # Hedef kontrolü (DFS'de genişletilirken bakılır)
        if problem.is_goal(node.state):
            return node.path()

        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)

            if child_state not in explored and \
               child_state not in [n.state for n in frontier]:
                child = Node(child_state, node, action)
                frontier.append(child)
    return None

def astar_search(problem, h=None):
    """
    A* Araması: f(n) = g(n) + h(n) değerini minimize eder.
    """
    frontier = PriorityQueue()
    initial_node = Node(problem.initial, path_cost=0)

    # f = g + h (Başlangıçta g=0 olduğu için f = h)
    f_score = 0 + h(initial_node.state, problem.goal)

    frontier.put((f_score, initial_node))

    # A*'da bir düğüme daha ucuz bir yoldan tekrar gelebiliriz.
    # Bu yüzden 'visited' yerine 'best_g' (en iyi maliyet) tutarız.
    best_g = {initial_node.state: 0}

    while not frontier.empty():
        _, node = frontier.get()

        if problem.is_goal(node.state):
            return node.path()

        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)

            # g(child) = g(parent) + step_cost
            # Romania haritasında step_cost, şehirler arası mesafedir.
            step_cost = romania_map[node.state][child_state]
            new_g = node.path_cost + step_cost

            # Eğer bu şehre daha önce hiç gelmediysek VEYA
            # şu an bulduğumuz yol daha kısaysa güncelle.
            if child_state not in best_g or new_g < best_g[child_state]:
                best_g[child_state] = new_g
                f_new = new_g + h(child_state, problem.goal)

                child = Node(child_state, node, action, new_g)
                frontier.put((f_new, child))

    return None

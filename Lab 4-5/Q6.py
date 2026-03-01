import random, copy
graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}

heuristic= {'S': 7, 'A': 5, 'B': 6, 'C': 3, 'D': 2, 'E': 4, 'G': 0}

# A* using manual sorted frontier (matching image code style)
def a_star(graph, start, goal):
    visited   = set()
    g_costs   = {start: 0}
    came_from = {start: None}
    frontier  = [[start, heuristic[start]]]   # [node, f = g + h]

    while frontier:
        # Sort frontier by f(n) = g(n) + h(n)
        frontier.sort(key=lambda x: x[1])
        current_node, current_f = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node, end=" ")
        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with A*. Path: {path}")
            return path, g_costs[goal]

        for neighbor, cost in graph[current_node].items():
            new_g  = g_costs[current_node] + cost         
            f_cost = new_g + heuristic[neighbor]    # f(n) = g(n) + h(n)

            if neighbor not in g_costs or new_g < g_costs[neighbor]:
                g_costs[neighbor]   = new_g
                came_from[neighbor] = current_node
                frontier.append([neighbor, f_cost])

    print("\nGoal not found")
    return None, float('inf')

def dynamic_edge_change(graph):
    edges = [(u, v) for u, nbrs in graph.items() for v in nbrs if nbrs]
    u, v  = random.choice(edges)
    old   = graph[u][v]
    delta = random.choice([-3, -2, 2, 3, 4])
    new   = max(1, old + delta)
    graph[u][v] = new
    print(f"  Edge {u}→{v} changed: {old} → {new}")
    return graph


random.seed(42)
graph = copy.deepcopy(graph)
for iteration in range(1, 4):
    print(f"\n Iteration {iteration}")
    if iteration > 1:
        graph = dynamic_edge_change(graph)
    path, cost = a_star(graph, 'S', 'G')
    print(f"  Optimal Path: {path}")
    print(f"  Total Cost  : {cost}")
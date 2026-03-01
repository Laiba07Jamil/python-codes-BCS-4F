import heapq
graph = {
    'S': {'A': 4, 'B': 2},
    'A': {'C': 5, 'D': 10},
    'B': {'E': 3},
    'C': {'G': 4},
    'D': {'G': 1},
    'E': {'D': 4},
    'G': {}
}

def ucs(graph, start, goal):
    frontier = [(0, start, [start])]
    visited = {}
    while frontier:
        cost, node, path = heapq.heappop(frontier)
        if node in visited and visited[node] <= cost:
            continue
        visited[node] = cost
        print(f"  Exploring: {node} , cost={cost}")
        if node == goal:
            return path, cost
        for neighbor, w in graph.get(node, {}).items():
            new_cost = cost + w
            heapq.heappush(frontier, (new_cost, neighbor, path + [neighbor]))
    return None, float('inf')


path, cost = ucs(graph, 'S', 'G')
print(f"\nLeast-Cost Path: {path}")
print(f"Total Cost     : {cost}")
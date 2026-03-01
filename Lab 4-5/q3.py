graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}


def dls_ids(graph, node, goal, depth, path):
    if node == goal:
        return path
    if depth == 0:
        return None
    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = dls_ids(graph, neighbor, goal, depth - 1, path + [neighbor])
            if result:
                return result
    return None

def ids(graph, start, goal):
    depth = 0
    while True:
        print(f"\n  Depth Level {depth}:")
        result = dls_ids(graph, start, goal, depth, [start])
        if result:
            print(f"  Goal found! Path: {result}")
            return result
        print("  Not found at this depth.")
        depth += 1


ids(graph, 'A', 'G')
graph = {
    'S': [('A', 3), ('B', 6), ('C', 5)],
    'A': [('D', 9), ('E', 8)],
    'B': [('F', 12), ('G', 14)],
    'C': [('H', 7)],
    'H': [('I', 5), ('J', 6)],
    'I': [('K', 1), ('L', 10), ('M', 2)],
    'D': [],'E': [],
    'F': [],'G': [],
    'J': [],'K': [],
    'L': [],'M': []
}

def hill_CLimbing(start,goal):
    current_node = start
    path = [current_node]

    while current_node != goal:
        neighbor = graph.get(current_node, [])
        if not neighbor:
            print(f"No more neighbors for node {current_node}")
        best_neighbor = min(neighbor, key=lambda x: heuristic[x[0]])
        best_neighbour_node = best_neighbor[0]

        if heuristic[best_neighbour_node] >= heuristic[current_node]:
            print(f"Stuck at hill")
            return path
        current_node = best_neighbour_node
        path.append(current_node)

        if(current_node == goal):
            print("Goal found")
            return path
        
    print("Goal not found")
    return None
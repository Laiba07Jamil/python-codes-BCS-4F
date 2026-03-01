tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': ['H'],
    'G': [],
    'H': []
}

def depth_limited_search(graph, current, target, limit, current_path, explored):
    print(f"Checking Node: {current} | Level: {len(current_path)-1}")

    if current == target:
        return current_path

    if limit <= 0:
        return None

    for next_node in graph.get(current, []):
        if next_node not in explored:
            explored.add(next_node)

            found_path = depth_limited_search(
                graph,
                next_node,
                target,
                limit - 1,
                current_path + [next_node],
                explored
            )

            if found_path is not None:
                return found_path

            explored.remove(next_node)

    return None

depth_limits = [2, 3]

for d in depth_limits:
    print(f"\n--- Trying Depth Limit: {d} ---")
    
    answer = depth_limited_search(tree, 'A', 'H', d, ['A'], {'A'})

    if answer:
        print("Goal Reached! Path:", answer)
    else:
        print("No solution within this depth.")
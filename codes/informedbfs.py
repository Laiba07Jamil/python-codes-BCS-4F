from queue import PriorityQueue

def best_first_search(start, goal, graph, heuristic):
    open_list = PriorityQueue()
    closed = set()
    open_list.put((heuristic[start], start))
    
    path = []

    while not open_list.empty():
        h, current = open_list.get()
        
        if current in closed:
            continue
        
        print(f"Selected: {current} (h={h})")
        path.append(current)
        closed.add(current)

        if current == goal:
            print("Goal reached!")
            return path

        for neighbor in graph[current]:
            if neighbor not in closed:
                open_list.put((heuristic[neighbor], neighbor))

    print("Goal not found")
    return path

heuristic = {
    "T0": 5, "T1": 3, "T2": 4,
    "T3": 2, "T4": 1, "T5": 2, "T6": 0
}

graph = {
    "T0": ["T1", "T2"],
    "T1": ["T3", "T4"],
    "T2": ["T5"],
    "T3": ["T6"],
    "T4": ["T6"],
    "T5": ["T6"],
    "T6": []
}
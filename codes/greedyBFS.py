graph = {
    'A': {'B': 4,'C':3},
    'B' : {'F':5,'E':12},
    'C':{'D':7,'E':10},
    'D':{'E':2},
    'E': {'G':5},
    'F':{'G':16},
    'G':{}
}

heuristic = {'A':14 , 'B':12, 'C':11 ,'D':6,'E' : 4,'F':11,'G':0}

def greedyBFS(start,goal,graph):
    frontier =[(start,heuristic[start])]
    visited = set()
    came_from = {start : None}

    while frontier:
        frontier.sort(key = lambda x :x[1])
        current_node ,_= frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node , end="->")
        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Path to goal node : {path}")
            return
        
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                came_from[neighbor] = current_node
                frontier.append((neighbor,heuristic[neighbor]))

    print(f"Goal not found")
    return None
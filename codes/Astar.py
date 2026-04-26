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

def a_star(start,goal,graph):
    frontier = [(start , 0 + heuristic[start])]
    came_from = {start : None}
    g_cost = {start : 0}
    visited = set()

    while frontier:
        frontier.sort(key = lambda x:x[1])
        current_node , current_f = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node , end = " ->")
        visited.add(current_node)

        if current_node == goal:
            path = []
            if current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"Path to goal node with A* search :{path}")
            return 
            
        for neighbour , cost in graph[current_node].items():
            new_g_cost = g_cost[current_node] + cost
            f_cost = new_g_cost + heuristic[neighbour]
            if neighbour not in g_cost or new_g_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_g_cost
                came_from[neighbour] = current_node
                frontier.append((neighbour,f_cost))
        
        print("Goal not found")
        return None
    
a_star('A','G',graph)

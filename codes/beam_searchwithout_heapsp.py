graph = {'S' : [('A,3' ), ('B,6'),('C,5')],
         'A' : [('D',9),('E',8)],
         'B':[('F',12),('G',14)],
         'C' :[('H',7)],
         'H':[('I',5),('J',6)],
         'I':[('K',1),('L',10),('M',2)],
         'D':[],
         'E':[],
         'F':[],
         'G':[],
         'J':[],
         'K':[],
         'L':[],
         'M':[]}
def heuristic(start):
    pass

def beam_Search(start,goal,beam_width = 2):
    frontier = [(start,heuristic[start])]  #path,cost
    all_frontier = []
    visited = set()
    came_from = {start : None}

    while frontier:
        frontier.sort(key=lambda x :x[1])
        frontier = frontier[:beam_width]
        all_frontier.append(list(frontier))
        next_frontier = []

        for current_node,_ in frontier:
            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                print(f"Path : {path}")
                return path , all_frontier
                
            for neighbor in graph[current_node]:
                next_frontier.append(neighbor,heuristic[neighbor])
                came_from[neighbor] = current_node
            
        frontier = next_frontier
        return None,all_frontier
    
def beamSearc(start,goal,graph,beam_width):
    frontier = [(start,heuristic[start])]
    visited = set()
    came_from = {start : None}

    while frontier:
        frontier.sort(key = lambda x:x[1])
        frontier = frontier[:beam_width]
        all_frontier = (list(frontier))
        next_frontier = []

        for current_node , _ in frontier:
            if current_node in visited:
                continue
            print(current_node , end=" ")
            visited.add(current_node)

            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                print(f"Goal found with path: {path}")
                return path,all_frontier
            
            for neighbors in graph[current_node]:
                if neighbors not in visited:
                    next_frontier.append(neighbors,heuristic[neighbors])
                    came_from[neighbors] = current_node

            frontier = next_frontier
        
        return "goal not found"
    


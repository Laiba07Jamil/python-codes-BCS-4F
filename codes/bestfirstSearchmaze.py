from queue import PriorityQueue

maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (4, 4)

class Node:
    def __init__(self,position,parent = None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0

    def _lh_(self,other):
        return self.f < other.f
        

def Manhattan_distance(current_pos , end_pos):
    return (abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1]))

def Best_first_Search(maze,start,end):
    frontier = PriorityQueue()
    visited = set()
    start_node = Node(start)
    end_node = Node(end)
    frontier.put(start_node)
    rows = len(maze)
    cols = len(maze[0])

    while not frontier.empty():
        current_node = frontier.get()
        current_pos =  current_node.position

        if current_pos == end:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            path.reverse()
            return path
         
        visited.add(current_pos) 

        for dx , dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_pos = (current_pos[0] + dx , current_pos[1] + dy)
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
                new_node = Node(new_pos , current_node)
                new_node.h = Manhattan_distance(new_pos,end)
                new_node.f = new_node.h
                frontier.append(new_node)
                visited.add(new_pos)

    return None

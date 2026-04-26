import math
from queue import PriorityQueue
maze = [
    [1, 1, 2, '#', 3],
    [1, '#', 2, '#', '#'],
    [1, 2, 1, 2, '#'],
    ['#', '#', 1, '#', '#'],
    [1, 1, 1, 2, 1]
]
start = (0, 0)
end = (4, 4)

class Node:
    def __init__(self,position,parent =None):
        self.position = position
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0
    
    def _lt__(self,other):
        return self.f < other.f
    
def hueristic(currentpos , endpos):
    return ((abs(currentpos[0] -endpos[0]) + abs(currentpos[1] - endpos[1])))

def Euclidean(current,endpos):
    return math.sqrt((current[0]-endpos[0])**2 + (current[1] - endpos[1])**2)


def a_star(maze,start,end):
    frontier = PriorityQueue()
    visited = set()
    start_node = Node(start)
    end_node = Node(end)
    rows = len(maze)
    cols = len(maze[0])
    while not frontier.empty():
        current_node = frontier.get()
        current_pos = current_node.position
        if current_pos == end:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            path.reverse()
            return path
        
        visited[current_pos] = current_node.g
        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            newrows = current_pos[0] + dx
            newcols = current_pos[1] + dy 
            if 0 <= newrows < rows and 0 <= newcols < cols:
                cell =  maze[newrows][newcols] 
                if cell != '#':
                    cost = int(cell)
                    new_pos = (newrows,newcols)
                    new_node = Node(new_pos,current_node)
                    new_node.h = hueristic(new_pos,end)
                    new_node.g = current_node.g + cost
                    new_node.f = new_node.h + new_node.g
                    if new_pos not in visited or new_node.g < visited[new_pos]:
                        frontier.put(new_node)
                        visited[new_pos] = new_node.g
    return None
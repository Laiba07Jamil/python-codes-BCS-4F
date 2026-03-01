from collections import deque
from queue import PriorityQueue

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent   = parent
        self.g = 0   # cost from start to current node
        self.h = 0   # heuristic estimate to end node
        self.f = 0   # total cost

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current_pos, end_pos):
    return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])

def best_first_search(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start)
    end_node   = Node(end)
    frontier   = PriorityQueue()
    frontier.put(start_node)
    visited    = set()

    while not frontier.empty():
        current_node = frontier.get()
        current_pos  = current_node.position

        if current_pos == end:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]   
        visited.add(current_pos)

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols
                    and maze[new_pos[0]][new_pos[1]] == 0
                    and new_pos not in visited):
                new_node   = Node(new_pos, current_node)
                new_node.g = current_node.g + 1
                new_node.h = heuristic(new_pos, end)
                new_node.f = new_node.h  
                frontier.put(new_node)
                visited.add(new_pos)

    return None  
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

heuristic_task5 = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 3, 'F': 3, 'G': 6, 'H': 2, 'I': 0}

def greedy_bfs(graph, start, goal):
    frontier  = [[start, heuristic_task5[start]]]   
    visited   = set()
    came_from = {start: None}

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, _ = frontier.pop(0)

        if current_node in visited:
            continue

        print(current_node, end=" ")
        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with GBFS. Path: {path}")
            return path

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                came_from[neighbor] = current_node
                frontier.append([neighbor, heuristic_task5[neighbor]])

    print("\nGoal not found")
    return None


# Part A: Grid-based Best-First Search
maze_grid = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 0]
]
start = (0, 0)
end   = (3, 3)
print("\nPart A: Grid Maze — Best-First Search:")
path = best_first_search(maze_grid, start, end)
if path:
    print("Path found:", path)
else:
    print("No path found")

# Part B: Graph-based Greedy Best-First Search 
print("\nPart B: Graph — Greedy Best-First Search:")
print("Following is the Greedy Best-First Search (GBFS):")
greedy_bfs(graph, 'A', 'I')
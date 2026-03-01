from collections import deque
building = [
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1]
]

def grid_to_graph(grid):
    rows, cols = len(grid), len(grid[0])
    graph = {}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                neighbors = []
                for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        neighbors.append((nr, nc))
                graph[(r, c)] = neighbors
    return graph

class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "Goal reached"
        return "Searching"

    def bfs_search(self, graph, start, goal):
        visited = []
        queue = []
        visited.append(start)
        queue.append(start)
        traversal_order = []

        while queue:
            node = queue.pop(0)
            traversal_order.append(node)
            print(f"  Visiting: {node}")
            if node == goal:
                return traversal_order, f"Goal {goal} found!"
            for neighbour in graph.get(node, []):
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return traversal_order, "Goal not found"

    def act(self, percept, graph):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal reached":
            return [], f"Goal {self.goal} found at start!"
        else:
            return self.bfs_search(graph, percept, self.goal)

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

def bfs_shortest_path(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    return None


graph = grid_to_graph(building)
agent   = GoalBasedAgent((3, 3))
env     = Environment(graph)
percept = env.get_percept((0, 0))
traversal, msg = agent.act(percept, graph)
print(f"\nTraversal Order: {traversal}")
path = bfs_shortest_path(graph, (0, 0), (3, 3))
print(f"Shortest Path  : {path}")
print(msg)
from queue import PriorityQueue

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0   # total cost from start
        self.f = 0   # same as g (since no heuristic)

    def __lt__(self, other):
        return self.f < other.f


def ucs_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])

    frontier = PriorityQueue()
    start_node = Node(start)
    start_node.g = int(maze[start[0]][start[1]])
    start_node.f = start_node.g

    frontier.put(start_node)

    visited = {}  # store best cost for each position

    while not frontier.empty():
        current_node = frontier.get()
        current_pos = current_node.position

        # Goal check
        if current_pos == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        visited[current_pos] = current_node.g

        # Explore neighbors
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            r = current_pos[0] + dx
            c = current_pos[1] + dy

            if 0 <= r < rows and 0 <= c < cols:
                cell = maze[r][c]

                if cell != '#':   # not blocked
                    move_cost = int(cell)
                    new_pos = (r, c)
                    new_cost = current_node.g + move_cost

                    if new_pos not in visited or new_cost < visited[new_pos]:
                        neighbor = Node(new_pos, current_node)
                        neighbor.g = new_cost
                        neighbor.f = new_cost   # UCS → f = g

                        frontier.put(neighbor)
                        visited[new_pos] = new_cost

    return None
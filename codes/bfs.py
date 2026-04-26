maze = [[1,1,0],
        [1,0,1],
        [1,1,1]]

directions = [[-1,0],[1,0],[0,1],[0,-1]]

def make_graph(maze):
    graph ={}
    rows = len(maze)
    cols = len(maze[0])

    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 1:
                neighbors = []
                for dx , dy in directions:
                    nx , ny = i+dx , j+dy
                    if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 1:
                     neighbors.append((nx,ny))

                graph[(i,j)] = neighbors

    return graph

def bfs(start,goal,graph):
    queue = []
    visited = []

    queue.append(start)
    visited.append(start)

    while queue:
        node = queue.pop(0)
        print("Visiting node: ", node , end = " ")
        if node == goal:
            print("Goal found")
            return visited

        for neighbors in graph[node]:
            if neighbors not in visited:
                visited.append(neighbors)
                queue.append(neighbors) 

    print("Goal not found")
    return None

graph = make_graph(maze)
start = (0,0)
goal = (2,2)

path = bfs(start,goal,graph)
print("Path:",path)
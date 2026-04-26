class Environment:
    def __init__(self,graph):
        self.graph = graph

    def get_percept(self,node):
        return node
    
class GoalBasedAgent:
    def __init__(self,goal):
        self.goal = goal

    def formulate_goal(self,percept):
        if percept == self.goal:
            return "Goal Found"
        else:
            return "Searching"
        
    def generate_graph(maze):
        graph = {}
        rows = len(maze)
        cols = len(maze[0])
        for i in range(rows):
            for j in range(cols):
                if maze[i][j] == '0' or maze[i][j] == 'P' or maze[i][j] == 'A':
                    neighbors = []
                    for dx,dy ,in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx , ny = (dx+i , dx+j)
                        if 0 <= nx < 0 and 0 <= ny < cols:
                            neighbors.append((nx,ny))

                    graph[(i,j)] = neighbors    
        return graph
    
    def dfs(self,start,goal,depth,graph,path):
        if depth < 0:
            return False
        path.append(start)
        if start == goal:
            return True
        for neighbors in graph.get(start,[]):
            if neighbors not in path:
                if self.dfs(neighbors,goal,depth-1,graph,path):
                    return True
        
        path.pop()
        return False
    
    def IDDFS(self,start,goal,limit,graph):
        for depth in range(limit+1):
            print(f"Depth: " ,depth)
            path = []

            if self.dfs(start,goal,depth,graph,path):
                return path
            
        return "Goal not Found"

    def act(self,percept,graph,depth):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal Found":
            return "Goal already at start"
        else:
            return self.IDDFS(percept,self.goal,depth,graph)
        
def run_agent(agent,environment,start,graph,depth_limit):
    percept = environment.get_percept(start)
    action = agent.act(percept,graph,depth_limit)
    print(action)

tree = {'A':['B','C'],
        'B':['A','C'],
        'C' : []}
agent = GoalBasedAgent('C')
maze = agent.generate_graph(tree)
environment = Environment(maze)
run_agent(agent,environment,'A',tree,2)
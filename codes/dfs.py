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
            print("Goal Found")
        else:
            print("Searching")

    def dfs(start,goal,graph):
        visited = []
        stack = []

        visited.append(start)
        stack.append(start)

        while stack:
            node = stack.pop()
            print(node , end = " ")
            if node == goal:
                print("Goal Found")
                return visited
            
            for neighbors in reversed(graph[node]):
                if neighbors is not None:
                    stack.append(neighbors)
                    visited.append(neighbors)
                                   
        print("Goal not found")
        return None
    
    def act(self,percept,graph,start):
        goal_staus = self.formulate_goal(percept)
        if goal_staus == "Goal Found":
            return "Found"
        else:
            return self.dfs(start,self.goal,graph)
        
def run_agent(self,agent,environment,start,graph):
    percept = environment.get_percept(start)
    action = agent.act(percept,graph,start)
    print("Action: ",action)


tree = {'A' : ['B','C'],
        'B' : ['C','D'],
        'D':['E','F'],
        'C' : ['G'],
        'E':[],
        'F':[],
        'G':[]}

environment =Environment(tree)
agent = GoalBasedAgent('E')
run_agent(agent,environment,'A,tree')
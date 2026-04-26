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

    def DLS(self,start,goal,depth_limit,graph):
        def dfs(node,depth,path):
            if depth > depth_limit:
                return None
            
            path.append(node)
            if goal == node:
                return path
            
            for neighbors in graph.get(node,[]):
                if neighbors not in path:
                    result = dfs(neighbors,depth+1,path)
                    if result is not None:
                        return result
            
            path.pop()
            return None
        
        result = dfs(start,0,[])
        if result is not None:
            return result
        else:
            return "Goal not found"



    def act(self,percept,graph,depth):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal Found":
            return "Goal already at start"
        else:
            return self.DLS(percept,self.goal,depth,graph)
        
def run_agent(agent,environment,start,graph,depth_limit):
    percept = environment.get_percept(start)
    action = agent.act(percept,graph,depth_limit)
    print(action)

tree = {'A':['B','C'],
        'B':['A','C'],
        'C' : []}
environment = Environment(tree)
agent = GoalBasedAgent('C')
run_agent(agent,environment,'A',tree,2)
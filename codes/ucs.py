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

    def ucs(self,start,goal,graph):
        frontier = [[start],0]
        visited =set()
        came_from = {start : None}
        cost_from ={start:0}
        while frontier:
            frontier.sort(key=lambda x:x[1])
            current_node , current_cost = frontier.pop(0)
            if current_node in visited:
                continue
            visited.add(current_node)

            if current_node == goal:
                path = []
                while current_node is not None:
                    path.append(current_node)
                    current_node = came_from[current_node]
                path.reverse()
                print(f"correct path with ucs cost is: {path} and {current_cost}")
                return path
                
        for neighbors,cost in graph.get(current_node,[]):
            new_cost = cost + current_cost
            if neighbors not in cost_from or new_cost < cost_from[neighbors]:
                frontier.append((neighbors,new_cost))
                came_from[neighbors] = current_node
                cost_from[neighbors] = new_cost
        
        return "Goal not Found"

    def act(self,percept,graph,depth):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal Found":
            return "Goal already at start"
        else:
            return self.ucs(percept,self.goal,graph)
        
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
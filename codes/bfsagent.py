class Environment:
    def __init__(self,graph):
        self.graph = graph

    def get_percept(self,node):
        return node


class GoalAgent:
    def __init__(self,goal):
        self,goal =goal

    def formulate_goal(self,percept):
        if percept == self.goal:
            return "Goal FOund"
        else:
            return "searching"

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


    def act(self,percept,start,graph):
        goal_status = self.formulate_goal(percept)
        if goal_status == "Goal FOund":
            return "Found"
        else:
            return self.bfs(start,self.goal,graph)

def run_agent(self,agent,environment,graph,start):
    percept = environment.get_percept(start)
    action = agent.act(percept,start,graph)
    print("Path: " ,action)

tree = {
'A': ['B', 'C'],
'B': ['D', 'E'],
'C': ['F','G'],
'D': ['H'],
'E': ['I'],
'G' : [],
'H' : [],
'I': [] }
start = 'A'
goal = 'I'
environment = Environment(tree)
agent = GoalAgent(goal)
run_agent(agent,environment,tree,start)
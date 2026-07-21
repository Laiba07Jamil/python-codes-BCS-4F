import math

class Node:
    def __init__(self,value):
        self.value = value
        self.children = []
        self.minimax_value = None

class AlphabetaAgent:
    def __init__(self,depth):
        self.depth = depth

    def formulate_goal(self,node):
        if node.minimax_value is not None:
            return "Goal found"
        else:
            return "Searching"
        
    def act(self,node,environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal found":
            print(f"Minimax value of root : {node.minimax_value}")
        else:
            return environment.minmax(node,-math.inf,math.inf,self.depth)
        
class Environment:
    def __init__(self,tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self,node):
        return node
    
    def minimax(self,node,alpha,beta,depth,maximizing_player = True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            return node.value
        
        if maximizing_player:
            value = -math.inf
            for node in node.children:
                child_value = self.minimax(node,alpha,beta ,depth -1,maximizing_player=  False)
                value = max(value,child_value)
                alpha = max(alpha,value)
                if beta <= alpha:
                    print(f"Pruned node : {node.value}")
                    break
            node.minimax_value = value
            self.computed_nodes.append(node.value)
            return value
        else:
            value = math.inf
            for node in node.children:
                child_value = self.minimax(node,alpha,beta,depth-1,maximizing_player=True)
                value = min(value,child_value)
                beta = min(beta,value)
                if beta <= alpha :
                    print (f"Pruned node : {node.value}")
                    break
            node.minimax_value = value
            self.computed_nodes.append(node.value)
            return value
            
def run_agent(agent,environmet,node):
    percept = environmet.get_percept(node)
    agent.act(percept,environmet)

root = Node('A')
n1 = Node('B')
n2 = Node('C')
root.children = [n1,n2]

n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')

n1.children = [n3,n4]
n2.children = [n5,n6]

n7 = Node(2)
n8 = Node(3)
n3.children = [n7,n8]

n9 = Node(5)
n10 = Node(9)
n4.children = [n9 , n10]

n11 = Node(0)
n12 = Node(1)
n5.children = [n11,n12]

n13 = Node(7)
n14 = Node(5)
n6.children = [n13,n14]

agent = AlphabetaAgent(depth=3)
environment = Environment(root)

run_agent(agent,environment,root)

print(f"Compute Nodes : {environment.computed_nodes}")
print(f"Minimax value")
print(f"A : {root.minimax_value}")
print(f"B : {n1.minimax_value}")
print(f"C : {n2.minimax_value}")
print(f"D : {n3.minimax_value}")
print(f"E : {n4.minimax_value}")
print(f"F : {n5.minimax_value}")
print(f"G : {n6.minimax_value}")

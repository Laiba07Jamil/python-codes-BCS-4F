import math
import copy

class Node:
    def __init__(self,grid):
        self.grid= grid
        self.children = []
        self.minimax_value = None
    
class MinMax_Agent:
    def __init__(self,depth):
        self.depth = depth

    def formulate_goal(self):
        return "To find best value of root"
    
    def act(self,node,environment):
        goal_status = self.formulate_goal()

        value = environment.compute_minimax(node,self.depth,True,environment)
        print(f"Best utility value : {value}")
        print(f"Computed Nodes :{environment.computed_nodes}")


class Environment:
    def __init__(self,root):
        self.root = root
        self.computed_nodes = 0

    def compute_minimax(self,node,depth , maximizing_playe , environment):
        self.computed_nodes += 1
        winner = check_winner(node.grid)
        if depth == 0 or winner != None or is_full(node.grid):
            if winner == 'X':
                node.minimax_value = 1
                return 1
            elif winner == 'O':
                node.minimax_value = -1
                return -1
            else:
                node.minimax_value = 0
                return 0
            
        if maximizing_playe:
            value = -math.inf
            node.children = generate_children(node.grid)
            for node in node.children :
                child_value = self.compute_minimax(node,depth-1,False,environment)
                value = max(value,child_value)
            node.minimax_value = value
            self.computed_nodes.append(node.grid)
            return value
        else:
            value = math.inf
            node.children = generate_children(node.grid)
            for node in node.children :
                child_value = self.compute_minimax(node,depth-1,True,environment)
                value = min(value,child_value)
            node.minimax_value = value
            self.computed_nodes.append(node.grid)
            return value

def check_winner(grid):
    for row in grid:
        if row[0] == row[1] == row[2] and row[0] != '_':
            return row[0]
    
    for col in range(3):
        if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != '_':
            return grid[0][col]

    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != '_':
        return grid[0][0]

    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != '_':
        return grid[0][2]

    return None

def is_full(grid):
    for row in grid:
        if '_' in row :
            return False
    return True

def generate_children(grid):
    children = []
    for i in range(3):
        for j in  range(3):
            if grid[i][j] == '_':
             newgrid = copy.deepcopy(grid)
             newgrid[i][j] = 'X'
             child = Node(newgrid)
             children.append(child)
    return children

def show(grid):
    for row in grid:
        print(row)
    print()

grid = [
['X', 'O', 'X'],
['_', 'O', '_'],
['_', 'X', '_']
]

root = Node(grid)

print("Current Grid:")
show(root.grid)

agent = MinMax_Agent(depth=3)
environment = Environment(root)

agent.act(root,environment)
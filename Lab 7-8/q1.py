import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minimax = None

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        if node.minimax is not None:
            return "Goal reached"
        else:
            return "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)

        if goal_status == "Goal reached":
            print(f"Minimax value for root node: {node.minimax}")
        else:
            result = environment.compute_minimax(node, self.depth)
            print(f"Minimax value for root node: {result}")

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def compute_minimax(self, node, depth, maximizing=True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            return node.value

        if maximizing:
            value = -math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, False)
                value = max(value, child_value)
        else:
            value = math.inf
            for child in node.children:
                child_value = self.compute_minimax(child, depth - 1, True)
                value = min(value, child_value)

        node.minimax = value
        return value

    def run_agent(self, agent, start_node):
        agent.act(start_node, self)


# Tree construction
root = Node()

n1 = Node()
n2 = Node()
root.children = [n1, n2]

n3 = Node()
n4 = Node()
n5 = Node()
n6 = Node()
n1.children = [n3, n4]
n2.children = [n5, n6]

# Leaf nodes
n3.children = [Node(4), Node(7)]
n4.children = [Node(2), Node(5)]
n5.children = [Node(1), Node(8)]
n6.children = [Node(3), Node(6)]

# Run Minimax
depth = 3
agent = MinimaxAgent(depth)
environment = Environment(root)

environment.run_agent(agent, root)

# Output
print("Computed Nodes:", environment.computed_nodes)

print("Minimax values:")
print("Root:", root.minimax)
print("N1:", n1.minimax)
print("N2:", n2.minimax)
print("N3:", n3.minimax)
print("N4:", n4.minimax)
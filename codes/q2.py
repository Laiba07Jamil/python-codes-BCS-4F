import math

# ---------------- NODE ----------------
class Node:
    def __init__(self, name, values=None):
        self.name = name
        self.values = values      # (card outcomes)
        self.children = []
        self.minimax_value = None


# ---------------- ENVIRONMENT ----------------
class Environment:
    def __init__(self, root):
        self.root = root
        self.computed_nodes = 0

    def compute_minimax(self, node, isMax):

        self.computed_nodes += 1

        # If leaf node (card outcomes)
        if node.values is not None:
            return min(node.values)   # opponent chooses MIN

        # MAX node (AI decision)
        if isMax:
            best = -math.inf

            for child in node.children:
                value = self.compute_minimax(child, False)
                best = max(best, value)

            node.minimax_value = best
            return best

        # MIN node (not used deeply here but structure kept)
        else:
            best = math.inf

            for child in node.children:
                value = self.compute_minimax(child, True)
                best = min(best, value)

            node.minimax_value = best
            return best


# ---------------- AGENT ----------------
class Minimax_Agent:

    def formulate_goal(self):
        return "Find best guaranteed payoff using Minimax"

    def act(self, environment, root):

        print("Goal:", self.formulate_goal())

        value = environment.compute_minimax(root, True)

        print("Best Utility Value:", value)
        print("Computed Nodes:", environment.computed_nodes)


# ---------------- BUILD TREE ----------------
A = Node("A", [7, 3])
B = Node("B", [6, 5])
C = Node("C", [9, 1])
D = Node("D", [5, 11])

# Root (AI chooses between cards)
root = Node("Root")
root.children = [A, B, C, D]


# ---------------- RUN ----------------
agent = Minimax_Agent()
environment = Environment(root)

agent.act(environment, root)
import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None


class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulate_goal(self, node):
        return "Goal reached" if node.minmax_value is not None else "Searching"

    def act(self, node, environment):
        goal_status = self.formulate_goal(node)

        if goal_status == "Goal reached":
            return f"Minimax value for root node: {node.minmax_value}"
        else:
            return environment.alpha_beta_search(
                node, self.depth, -math.inf, math.inf, True
            )


class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []
        self.pruned_nodes = []

    def get_percept(self, node):
        return node

    def alpha_beta_search(self, node, depth, alpha, beta, maximizing_player=True):

        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            return node.value

        if maximizing_player:
            value = -math.inf

            for child in node.children:
                val = self.alpha_beta_search(child, depth - 1, alpha, beta, False)
                value = max(value, val)
                alpha = max(alpha, value)

                print(f"{node.value} (Max): alpha={alpha}, beta={beta}")

                if beta <= alpha:
                    print(f"Pruned subtree at node: {child.value}")
                    self.pruned_nodes.append(str(child.value))
                    break

            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value

        else:
            value = math.inf

            for child in node.children:
                val = self.alpha_beta_search(child, depth - 1, alpha, beta, True)
                value = min(value, val)
                beta = min(beta, value)

                print(f"{node.value} (Min): alpha={alpha}, beta={beta}")

                if beta <= alpha:
                    print(f"Pruned subtree at node: {child.value}")
                    self.pruned_nodes.append(str(child.value))
                    break

            node.minmax_value = value
            self.computed_nodes.append(node.value)
            return value


def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    agent.act(percept, environment)


root = Node('Root')
n1 = Node('N1')
n2 = Node('N2')
root.children = [n1, n2]

n3 = Node('N3')
n4 = Node('N4')
n5 = Node('N5')
n6 = Node('N6')

n1.children = [n3, n4]
n2.children = [n5, n6]

n3.children = [Node(2), Node(3)]
n4.children = [Node(5), Node(9)]
n5.children = [Node(0), Node(1)]
n6.children = [Node(7), Node(5)]

depth = 3
agent = MinimaxAgent(depth)
environment = Environment(root)

run_agent(agent, environment, root)

print("\nComputed Nodes:", environment.computed_nodes)
print("Pruned Nodes:", environment.pruned_nodes)

print("\nMinimax values:")
print(f"Root: {root.minmax_value}")
print(f"N1: {n1.minmax_value}")
print(f"N2: {n2.minmax_value}")
print(f"N3: {n3.minmax_value}")
print(f"N4: {n4.minmax_value}")
print(f"N5: {n5.minmax_value}")
print(f"N6: {n6.minmax_value if n6.minmax_value is not None else 'Pruned'}")
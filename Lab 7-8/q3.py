import math

class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minmax_value = None
        self.best_child = None


class Environment:
    def __init__(self, root):
        self.root = root
        self.minimax_count = 0
        self.ab_count = 0
        self.pruned_nodes = []
        
    def minimax(self, node, depth, maximizing):
        if depth == 0 or not node.children:
            self.minimax_count += 1
            return node.value

        if maximizing:
            value = -math.inf
            best_child = None

            for child in node.children:
                val = self.minimax(child, depth-1, False)
                if val > value:
                    value = val
                    best_child = child

            node.minmax_value = value
            node.best_child = best_child
            return value

        else:
            value = math.inf
            best_child = None

            for child in node.children:
                val = self.minimax(child, depth-1, True)
                if val < value:
                    value = val
                    best_child = child

            node.minmax_value = value
            node.best_child = best_child
            return value

 
    def alpha_beta(self, node, depth, alpha, beta, maximizing):
        if depth == 0 or not node.children:
            self.ab_count += 1
            return node.value

        if maximizing:
            value = -math.inf
            best_child = None

            for child in node.children:
                val = self.alpha_beta(child, depth-1, alpha, beta, False)

                if val > value:
                    value = val
                    best_child = child

                alpha = max(alpha, value)

                if beta <= alpha:
                    print("Pruned:", child.value)
                    self.pruned_nodes.append(child.value)
                    break

            node.minmax_value = value
            node.best_child = best_child
            return value

        else:
            value = math.inf
            best_child = None

            for child in node.children:
                val = self.alpha_beta(child, depth-1, alpha, beta, True)

                if val < value:
                    value = val
                    best_child = child

                beta = min(beta, value)

                if beta <= alpha:
                    print("Pruned:", child.value)
                    self.pruned_nodes.append(child.value)
                    break

            node.minmax_value = value
            node.best_child = best_child
            return value

root = Node('Root')
n1 = Node('N1')
n2 = Node('N2')
root.children = [n1, n2]

n3 = Node('N3')
n4 = Node('N4')
n5 = Node('N5')
n6 = Node('N6')
n7 = Node('N7')   # new branch

n1.children = [n3, n4]
n2.children = [n5, n6, n7]

# modified leaves
n3.children = [Node(6), Node(3)]
n4.children = [Node(5), Node(9)]
n5.children = [Node(0), Node(1)]
n6.children = [Node(7), Node(5)]
n7.children = [Node(4), Node(8)]

env = Environment(root)

print("=== MINIMAX ===")
env.minimax(root, 3, True)

print("Minimax Root Value:", root.minmax_value)

print("Optimal Path (Minimax):")
node = root
while node:
    print(node.value, "→", end=" ")
    node = node.best_child
print()

print("\n=== ALPHA-BETA ===")
env.alpha_beta(root, 3, -math.inf, math.inf, True)

print("Alpha-Beta Root Value:", root.minmax_value)

print("Optimal Path (Alpha-Beta):")
node = root
while node:
    print(node.value, "→", end=" ")
    node = node.best_child
print()

print("\nNodes visited (Minimax):", env.minimax_count)
print("Nodes visited (Alpha-Beta):", env.ab_count)
print("Pruned Nodes:", env.pruned_nodes)
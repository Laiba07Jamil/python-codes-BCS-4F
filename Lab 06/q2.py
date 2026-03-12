goal = 20
start = 1
beam_width = 2

def h(n):
    return abs(goal - n)

def generate(n, visited):
    candidates = [n + 2, n + 3, n * 2]
    return [x for x in candidates if x <= goal and x not in visited]

beam = [(start, [start])]
visited = set([start])

level = 0
print("Level", level, ":", [node for node, path in beam])

while True:
    candidates = []

    for node, path in beam:
        children = generate(node, visited)
        for child in children:
            new_path = path + [child]
            candidates.append((child, new_path))
            visited.add(child)

    if not candidates:
        print("No more candidates. Goal not reachable.")
        break
    
    candidates.sort(key=lambda x: h(x[0]))
    beam = candidates[:beam_width]

    level += 1
    print("Level", level, ":", [node for node, path in beam])
    for node, path in beam:
        if node == goal:
            print("\nGoal found!")
            print("Final path:", path)
            exit()
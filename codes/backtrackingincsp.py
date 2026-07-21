slots = [1, 2, 3, 4, 5]

solutions = []

def is_valid(assign):
    
    # all different slots
    if len(set(assign.values())) != len(assign):
        return False

    # if variable not assigned yet
    if len(assign) < 5:
        return True

    T1, T2, T3, T4, T5 = assign["T1"], assign["T2"], assign["T3"], assign["T4"], assign["T5"]

    # Constraint 1: T1 and T3 not consecutive
    if abs(T1 - T3) == 1:
        return False

    # Constraint 2: T2 before T4
    if not (T2 < T4):
        return False

    # Constraint 3: T5 not in morning (1,2)
    if T5 in [1, 2]:
        return False

    # Constraint 4: T3 after T1
    if not (T3 > T1):
        return False

    # Constraint 5: T4 not final slot
    if T4 == 5:
        return False

    # Constraint 6: slot 3 only T1 or T2
    if not ((T1 == 3) or (T2 == 3)):
        return False

    return True


def backtrack(assign):

    if len(assign) == 5:
        solutions.append(assign.copy())
        return

    for var in ["T1", "T2", "T3", "T4", "T5"]:
        if var not in assign:
            for val in slots:
                assign[var] = val
                if is_valid(assign):
                    backtrack(assign)
                del assign[var]
            return


backtrack({})

print("All Valid Schedules:\n")
for sol in solutions:
    print(sol)


# Constraint Graph Representation

graph = {
    "T1": ["T3"],   # T1 related to T3 (not consecutive, ordering)
    "T2": ["T4"],   # T2 must come before T4
    "T3": ["T1"],
    "T4": ["T2"],
    "T5": []        # only unary constraints (no edges)
}

print("Constraint Graph:")
for node in graph:
    print(node, "->", graph[node])
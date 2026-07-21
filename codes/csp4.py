from ortools.sat.python import cp_model

model = cp_model.CpModel()

# Variables (slots 1 to 5)
T1 = model.NewIntVar(1, 5, "T1")
T2 = model.NewIntVar(1, 5, "T2")
T3 = model.NewIntVar(1, 5, "T3")
T4 = model.NewIntVar(1, 5, "T4")
T5 = model.NewIntVar(1, 5, "T5")

# All must be in different slots
model.AddAllDifferent([T1, T2, T3, T4, T5])

# -------------------------
# Constraint 1: T1 and T3 NOT consecutive
# |T1 - T3| != 1
diff = model.NewIntVar(-5, 5, "diff")
abs_diff = model.NewIntVar(0, 5, "abs_diff")
model.Add(diff == T1 - T3)
model.AddAbsEquality(abs_diff, diff)
model.Add(abs_diff != 1)

# -------------------------
# Constraint 2: T2 before T4
model.Add(T2 < T4)

# -------------------------
# Constraint 3: T5 not in morning (1,2)
model.Add(T5 != 1)
model.Add(T5 != 2)

# -------------------------
# Constraint 4: T3 after T1
model.Add(T3 > T1)

# -------------------------
# Constraint 5: T4 not final slot
model.Add(T4 != 5)

# -------------------------
# Constraint 6: ONLY T1 or T2 can be in slot 3

# T3, T4, T5 cannot take slot 3
model.Add(T3 != 3)
model.Add(T4 != 3)
model.Add(T5 != 3)

# At least one of T1 or T2 must be in slot 3
b1 = model.NewBoolVar("T1_is_3")
b2 = model.NewBoolVar("T2_is_3")

model.Add(T1 == 3).OnlyEnforceIf(b1)
model.Add(T1 != 3).OnlyEnforceIf(b1.Not())

model.Add(T2 == 3).OnlyEnforceIf(b2)
model.Add(T2 != 3).OnlyEnforceIf(b2.Not())

model.AddBoolOr([b1, b2])

# -------------------------
# Solve
solver = cp_model.CpSolver()
status = solver.Solve(model)

# Output
if status in [cp_model.FEASIBLE, cp_model.OPTIMAL]:
    print("Solution Found:\n")
    print("T1 =", solver.Value(T1))
    print("T2 =", solver.Value(T2))
    print("T3 =", solver.Value(T3))
    print("T4 =", solver.Value(T4))
    print("T5 =", solver.Value(T5))
else:
    print("No Solution Found")
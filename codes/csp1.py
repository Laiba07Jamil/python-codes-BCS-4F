from ortools.sat.python import cp_model

model = cp_model.CpModel()
num_vars = 3
x = model.new_int_var(0, num_vars - 1 , "x")
y = model.new_int_var(0, num_vars -  1, "y")
z = model.new_int_var(0, num_vars - 1 , "z")

model.add(x != y)
model.add(y != z)

solver = cp_model.CpSolver()
status = solver.solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(f"x = {solver.value(x)}")
    print(f"y = {solver.value(y)}")
    print(f"z = {solver.value(z)}")
else:
    print("no Solutions found")


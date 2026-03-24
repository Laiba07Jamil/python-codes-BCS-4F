from ortools.sat.python import cp_model

model = cp_model.CpModel()
numvals = 4
A = model.new_int_var(0 , numvals - 1 , "A")
B = model.new_int_var(0 , numvals - 1 , "B")
C = model.new_int_var(0 , numvals - 1 , "C")

model.add(A != B)
model.add(B != C)
model.add(A + B <= 4)

solver = cp_model.CpSolver()
status = solver.solve(model)
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
  print(f"A = {solver.value(A)}")
  print(f"B = {solver.value(B)}")
  print(f"C = {solver.value(C)}")
else:
  print("No solution found.")

from ortools.sat.python import cp_model

def main():
   model = cp_model.CpModel()
   domain = 20
   x = model.new_int_var(0 , domain , "x")
   y = model.new_int_var(0 , domain , "y")
   z = model.new_int_var(0 , domain , "z")

   model.add(x + 2*y + z <= 20)
   model.add(3*x + y <= 18)
   model.maximize(4*x + 2*y + z)

   solver = cp_model.CpSolver()
   status = solver.solve(model)
   if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
     print(f"Maximize value : {solver.objective_value}")
     print(f"x = {solver.value(x)}")
     print(f"y = {solver.value(y)}")
     print(f"z = {solver.value(z)}") 
   else:
     print("Values not found.")   

main()
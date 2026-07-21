import math
import time
from ortools.sat.python import cp_model
import random

class GridEnvironment:
    def __init__(self,size):
      self.size = size
      self.grid = [[0 for _ in range(size)] for _ in range(size)]
      self.start = (random.randint(0,size  - 1) , random.randint(0 , size - 1))
      self.goal = (random.randint(0, size - 1) , random.randint(0 , size - 1))

    def solveCSP(self):
       model = cp_model.CpModel()
       x1 ,y1 = self.start
       x2 , y2 = self.goal

       a = abs(x2 - x1)
       b = abs(y2 - y1)
       c = model.new_int_var(0 , self.size * 2 , "c")
       a_sq = model.new_int_var(0 , self.size ** 2 , "a_sq")
       b_sq = model.new_int_var(0 , self.size ** 2 , "b_sq")
       c_sq = model.new_int_var(0 , self.size ** 2 , "c_sq")

       model.add_multiplication_equality(a_sq , [a,a])
       model.add_multiplication_equality(b_sq , [b,b])
       model.add_multiplication_equality(c_sq , [c,c])
       model.add(c_sq == a_sq + b_sq)

       solver = cp_model.CpSolver()
       status = solver.Solve(model)

       if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
            return a, b, solver.Value(c)
            print(a, b, solver.Value(c))
       return a, b, math.sqrt(a**2 + b**2)  # Fallback to normal calculation

    def display(self):
        print(f"Start Position: {self.start}")
        print(f"Goal Position: {self.goal}")
        a, b, c = self.solve_csp()
        print(f"Calculated Distances: Base={a}, Height={b}, Hypotenuse={c:.2f}")


# Simulation
environment = GridEnvironment(10)
environment.display()
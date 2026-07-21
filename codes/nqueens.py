import time
from ortools.sat.python import cp_model

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self,variables : list[cp_model.IntVar]):
     cp_model.CpSolverSolutionCallback.__init__(self)
     self.__queens = variables
     self.__solution_count = 0
     self.__start_time = time.time()

    @property
    def getcount(self) -> int:
       return self.__solution_count
    
    def on_solution_callback(self):
       solution_count += 1
       print(f"Soltuion : {self.__solution_count}")

       board_size = len(self.__queens)
       for i in range(board_size):
          for j in range(board_size):
             if self.value(self.__queens[j]) == i:
                print("Q" , end = " ")
             else:
                print("__" , end = " ")
          print()
       print()

def search_all_soltuions():
   model = cp_model.CpModel

   board_size = 8
   queens = [model.new_int_var(0 , board_size -1 , f"x_{i}") for i in range(board_size)]

   model.add_all_different(queens)
   model.add_all_different(queens[i] + i for i in range(board_size))
   model.add_all_different(queens[i] - i for i in range(board_size))

   solver = cp_model.CpSolver()
   solver.parameters.enumerate_all_solutions = True
   solution_printer = VarArraySolutionPrinter(queens)
   status = solver.solve(model,solution_printer)


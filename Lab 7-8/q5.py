from ortools.sat.python import cp_model
class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
  def __init__(self , variables:list[cp_model.IntVar]):
    cp_model.CpSolverSolutionCallback.__init__(self)
    self.__variables = variables
    self.__solution_count = 0

  def on_solution_callback(self):
    self.__solution_count += 1
    for v in self.__variables:
      print(f"{v} : {self.value(v)} " , end = " ")
    print()

  @property
  def getcount(self) ->None:
    return self.__solution_count

def createmodel():
    model = cp_model.CpModel()
    numvals = 4
    A = model.new_int_var(0 , numvals - 1 , "A")
    B = model.new_int_var(0 , numvals - 1 , "B")
    C = model.new_int_var(0 , numvals - 1 , "C")

    model.add(A != B)
    model.add(B != C)
    model.add(A + B <= 4)

    solver = cp_model.CpSolver()
    solutionPrinter = VarArraySolutionPrinter([A,B,C])
    solver.parameters.enumerate_all_solutions = True
    status = solver.SearchForAllSolutions(model,solutionPrinter)

    print(f"Status = {solver.status_name(status)}")
    print(f"Solution Count: {solutionPrinter.getcount}")

  
  
createmodel()

from ortools.sat.python import cp_model

def solve_n_queens(n):
    model = cp_model.CpModel()
    queens = [model.NewIntVar(0, n - 1, f'q{i}') for i in range(n)]
    model.AddAllDifferent(queens)

    for i in range(n):
        for j in range(i + 1, n):
            model.Add(queens[i] - queens[j] != i - j)
            model.Add(queens[i] - queens[j] != j - i)
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        board = []
        for i in range(n):
            row = ['_'] * n
            col = solver.Value(queens[i])
            row[col] = 'Q'
            board.append(row)
        for row in board:
            print(' '.join(row))
    else:
        print("No solution found")

solve_n_queens(4)
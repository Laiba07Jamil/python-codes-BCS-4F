class Environment:
    def __init__(self,grid,start):
        self.grid = grid
        self.curr_pos = start
    
    def get_value(self,x,y):
        return self.grid[x][y]
    
    def clean(self,x,y):
        self.grid[x][y] = 0

    
class UtilitybasedAgent:
    def __init__(self,max_moves =8):
        self.moves = max_moves

    def utility(self,score):
        return score
    
    def best_path(self,env):
        total_score = 0
        x,y = env.curr_pos
        best_score = -1
        best = None
        moves = 0
        path = []
        path.append((x,y))
        
        while moves < self.moves:
            for dx , dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx = dx + x
                ny = dy + y
                if 0 <= nx < 4 and 0 <= ny < 5 :
                    if env.get_value(nx,ny) != 'X':
                        if self.utility(grid[nx][ny]) > best_score:
                            best_score = self.utility(grid[nx][ny])
                            best = (nx,ny)
            if best:
               x,y = best
               total_score += best_score
               moves += 1
               path.append((x,y))
               env.clean(x,y)
            else:
               break

        return total_score,path


def run_agent(agent,environment):
    action = agent.act(environment)
    print("Path ", action)



grid = [['S',2,0,0,1],
        [0,'X',1,2,0],
        [0,2,0,'X',0],
        [0,0,1,0,2]]
start=(0,0)
env = Environment(grid,start)
agent = UtilitybasedAgent()

run_agent(agent,env)

        
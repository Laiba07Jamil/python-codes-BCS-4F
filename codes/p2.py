class Environment:
  def __init__(self):
    self.movies = {"Dhurandar" : 8,
                   "PK" : 9,
                   "Hera pheri" : 7}

  def get_percept(self):
    return self.movies;

class utilityBasedAgent:
  def __init__(self,moodFactor):
    self.moodFactor = moodFactor

  def calculate_utility(self,percept):
    return self.moodFactor * percept

  
  def act(self,percept):
    best_movie = None
    total_utility = - float("inf")
    
    for movies in percept:
       utility = self.calculate_utility(percept[movies])
       if utility > total_utility:
        total_utility = utility
        best_movie = movies
  
    return best_movie

  
def run_agent(agent,environment):
  percept = environment.get_percept()
  movie = agent.act(percept)
  print("Movie: " , movie)

environment = Environment()
agent = utilityBasedAgent(moodFactor =0.7)

run_agent(agent,environment)


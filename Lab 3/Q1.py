#Task 1
class Environment:
  def __init__(self, traffic):
    self.traffic = traffic

  def get_percept(self):
    return self.traffic


class SimpleReflexAgent:
  def __init__(self):
    pass
  def act(self, percept):
    if percept == "Heavy":
      return "Extend Green Time"
    else:
      return "Normal Green Time"

def run_agent(agent, environment):
    percept = environment.get_percept()
    action = agent.act(percept)
    print(f"Percept: {percept} Traffic, Action: {action}")

agent = SimpleReflexAgent()
environment = Environment("Heavy")
run_agent(agent, environment)
environment1 = Environment("Light")
run_agent(agent, environment1)

"""Design a Model-Based Agent that controls classroom lights.
Environment States:
• Students Present: Yes / No
• Light Status: ON / OFF
Agent Model (Memory):
The agent must store:
• Previous student presence
• Previous light status
Rules:
1. If students are present and lights are OFF → Turn lights ON
2. If no students and lights are ON → Turn lights OFF
3. Otherwise → No action
The agent must update and display its internal model after each step.
Student presence should be randomly generated every iteration.
Run for 8 steps.
"""
import random

class Enviornment:
  def __init__(self):
    self.student = random.choice(["Yes", "No"])
    self.light = "Off"

  def get_percept(self):
    return {'Student': self.student, 'Light': self.light}
  
  def update(self):
    self.student = random.choice(["Yes", "No"])

  def lightOn(self):
    self.light = "On"

  def lightOff(self):
    self.light = "Off"

class ModelBasedAgent:
  def __init__(self):
    self.model = {"PrevStudent": None, "PrevLight": None, 'Student': None, 'Light': None}

  def act(self, percept):
    self.model['PrevStudent'] = self.model['Student']
    self.model['PrevLight'] = self.model['Light']
    self.model['Student'] = percept['Student']
    self.model['Light'] = percept['Light']

    if self.model['Student'] == "Yes" and self.model['Light'] == "Off": 
      return "ON"
    elif self.model['Student'] == "No" and self.model['Light'] == "On":
      return "OFF"
    else:
      return "No action"

def run_agent(agent, environment, steps=8):
  for i in range(1, steps+1):
    print(f"Step: {i}")

    environment.update()
    percept = environment.get_percept()
    action = agent.act(percept)

    if action == "ON":
      environment.lightOn()
    elif action == "OFF":
      environment.lightOff()
    
    print(f"Percept: {percept}")
    print(f"Action: {action}")
    print(f"Agent Model: {agent.model}")

environment = Enviornment()
agent = ModelBasedAgent()
run_agent(agent, environment)

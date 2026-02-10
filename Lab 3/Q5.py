import random

class LearningAgent:
  def __init__(self):
    self.actions = ["Play", "Rest"]
    self.rewards = {"Play": 5, "Rest": 1}
    self.Q = {"Play":0, "Rest":0}

  def run(self, steps=10):
    for step in range(1, steps+1):
      action = random.choice(self.actions)
      reward = self.rewards[action]
      self.Q[action]+=reward

      print(f"Step {step}: Action {action}, Reward +{reward}")

    print(f"\nQ-table Updated")
    print(self.Q)

agent = LearningAgent()
agent.run()

class GoalBasedAgent:
  def __init__(self, subjects):
    self.subjects=subjects
    self.completed=[]

  def action(self):
    for subject in self.subjects:
      if subject not in self.completed:
        print(f"Studying: {subject}")
        self.completed.append(subject)
    if len(self.completed) == len(self.subjects):
      print("Goal Achieved: All subjects completed") 

subject = ["AI", "Math", "Physics"]
agent = GoalBasedAgent(subject)
agent.action()

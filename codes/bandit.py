import random

class BanditAgent:
    def __init__(self):
        self.Q = {}
        self.actions = ['Slot1', 'Slot2', 'Slot3']
        self.alpha = 0.1
        self.epsilon = 0.2

    def get_Q(self, action):
        return self.Q.get(action, 0.0)

    def select_action(self):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        return max(self.actions, key=self.get_Q)

    def learn(self, action, reward):
        old_Q = self.get_Q(action)
        self.Q[action] = old_Q + self.alpha * (reward - old_Q)

# Run
agent = BanditAgent()
rewards = {'Slot1': 5, 'Slot2': 10, 'Slot3': 2}
for step in range(10):
    action = agent.select_action()
    r = rewards[action] + random.randint(-2,2)  # add randomness
    agent.learn(action, r)
    print(f"Step {step+1}: Action={action}, Reward={r}, Q={agent.Q}")
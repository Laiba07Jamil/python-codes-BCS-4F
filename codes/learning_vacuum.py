import random

class Agent:
    def __init__(self):
        self.Q = {}
        self.actions = ['Clean', 'Do nothing']
        self.alpha = 0.5
        self.gamma = 0.9
        self.epsilon = 0.2

    def get_Q(self, state, action):
        return self.Q.get((state, action), 0.0)

    def select_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        return max(self.actions, key=lambda a: self.get_Q(state, a))

    def learn(self, state, action, reward, next_state):
        old_Q = self.get_Q(state, action)
        best_next = max([self.get_Q(next_state, a) for a in self.actions])
        self.Q[(state, action)] = old_Q + self.alpha * (reward + self.gamma * best_next - old_Q)

class Environment:
    def __init__(self):
        self.state = 'Dirty'

    def perform_action(self, action):
        if action == 'Clean' and self.state == 'Dirty':
            self.state = 'Clean'
            return 10
        return 0

# Run
agent = Agent()
env = Environment()
for step in range(5):
    state = env.state
    action = agent.select_action(state)
    reward = env.perform_action(action)
    agent.learn(state, action, reward, env.state)
    print(f"Step {step+1}: State={state}, Action={action}, Reward={reward}")
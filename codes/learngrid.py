import random

class GridAgent:
    def __init__(self):
        self.Q = {}
        self.actions = ['up', 'down', 'left', 'right']
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

# Environment
grid = {
    (0,0): {'goal': False}, (0,1): {'goal': False},
    (1,0): {'goal': False}, (1,1): {'goal': True}
}

def reward(state):
    return 10 if grid[state]['goal'] else -1

# Run
agent = GridAgent()
state = (0,0)
for step in range(10):
    action = agent.select_action(state)
    # Simple movement logic
    next_state = {
        'up': (max(state[0]-1,0), state[1]),
        'down': (min(state[0]+1,1), state[1]),
        'left': (state[0], max(state[1]-1,0)),
        'right': (state[0], min(state[1]+1,1))
    }[action]
    r = reward(next_state)
    agent.learn(state, action, r, next_state)
    print(f"Step {step+1}: State={state}, Action={action}, Reward={r}, Next={next_state}")
    state = next_state
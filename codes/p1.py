class Environment:
    def __init__(self):
        self.distance = {"A": 3, "B": 5}
        self.rating = {"A": 7, "B": 9}

    def get_percept(self):
        return {"distance": self.distance, "rating": self.rating}


class UtilityBasedAgent:
    def __init__(self):
        self.distance = {"A": 3, "B": 5}
        self.rating = {"A": 7, "B": 9}

    def calculate_utility(self):
        utilities = {}
        for key in self.distance:
            utilities[key] = self.rating[key] - self.distance[key]
        return utilities

    def act(self):
        utilities = self.calculate_utility()
        best_restaurant = max(utilities, key=utilities.get)

        for key, value in utilities.items():
            print(f"Restaurant {key} utility: {value}")

        return best_restaurant, utilities[best_restaurant]


def run_agent(agent, environment):
    percept = environment.get_percept()
    best_restaurant, best_utility = agent.act()
    print("Selected restaurant:", best_restaurant, "with utility:", best_utility)


# Run the agent
environment = Environment()
agent = UtilityBasedAgent()
run_agent(agent, environment)
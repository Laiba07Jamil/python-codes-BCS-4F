import random

# Define weather states
states = ["Sunny", "Cloudy", "Rainy"]

# Transition matrix
transition_matrix = {
    "Sunny":  [0.6, 0.3, 0.1],
    "Cloudy": [0.4, 0.4, 0.2],
    "Rainy":  [0.2, 0.5, 0.3]
}

# Function to get next weather state
def next_state(current):
    probabilities = transition_matrix[current]
    return random.choices(states, probabilities)[0]

# Simulate weather for 10 days starting with Sunny
def simulate_weather(days=10):
    weather_sequence = ["Sunny"]
    current = "Sunny"

    for _ in range(days - 1):
        current = next_state(current)
        weather_sequence.append(current)

    return weather_sequence

# Run one simulation
weather_10_days = simulate_weather()
print("Weather for 10 Days:")
print(weather_10_days)

# Estimate probability of at least 3 rainy days
trials = 10000
count = 0

for _ in range(trials):
    simulation = simulate_weather()
    rainy_days = simulation.count("Rainy")

    if rainy_days >= 3:
        count += 1

probability = count / trials

print("\nProbability of at least 3 rainy days in 10 days:")
print(probability)
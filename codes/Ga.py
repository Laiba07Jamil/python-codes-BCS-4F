import random

def generate_individual():
    n = 4
    individual = []
    for i in range(n):
        individual.append(random.randint(0,1))

    return individual

def generate_population():
    population_size = 4
    population = []
    for i in range(population_size):
        population.append(generate_individual())

    return population

def calculate_fitness(individual):
    n = len(individual)
    decimal = individual[0]*2**3 + individual[1]*2**2 + individual[2]*2**1 + individual[3]*2**0

    f_value = (decimal)**2 - 3*(decimal) + 4
    return f_value

def evaluate_fitness(population):
    n = len(population)
    fitness = []
    for i in range(n):
        fitness.append(population[i])

    return fitness

def roulette_selection(population,fitness):
    total_fitness = sum(fitness)
    parents = []

    for _ in range(len(population) // 2):
        pick = random.uniform( 0 ,total_fitness)
        current = 0
        for i in range(len(population)):
            current += fitness[i]
            if current >= pick:
                parents.append(population[i])

    return parents

def cross_over(p1,p2):
    point = random.randint(0 , len(p1) -2)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p2[point:]

    return child1,child2

def mutation(individual):
    indx = random.randint(1 , len(individual)-2)
    individual[indx] = 1 - individual[indx]

    return individual

def genetic_algorithm():
    population = generate_population()
    generation = 0 
    best_fit = 158
    while generation <= 1 and best_fit < 158:
        fitness = evaluate_fitness(population)
        selection = roulette_selection(population,fitness)
        next_population = []

        for i in range(len(selection)):
            p1 , p2 = random.sample(selection,2)
            next_population.append(cross_over(p1,p2))

        for i in range(len(next_population)):
            next_population[i] = mutation(next_population[i])

        population = next_population
        generation += 1
        best = population[0]
        best_fit = calculate_fitness(best)

        for i in population:
            fit = calculate_fitness(population[i])
            if fit > best_fit:
                best_fit = fit
                best = population[i]

        final = (best_fit)**2 -3*best_fit +4
        print(f"Final value to maximum : {final}")
        




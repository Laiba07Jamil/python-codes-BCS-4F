import random
def population(n):
    popultaion= []
    for i in range(n):
        population.append(i)

    for i in range(n):
        j = random.randint(0,n-1)
        population[i],population[j] = population[j],population[i]

    return population

def generate_population(n):
    populations = []
    for i in range(10):
        populations.append(population(n))

    return populations

def calculate_fitness(individual,n):
    attackin_pairs = 0
    for i in range(n):
        for j in range(i+1 , n):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i-j):
                attackin_pairs += 1

    return attackin_pairs

def evaluates_fitness(population,n):
    fitness = []
    for i in range(10):
        fitness.append(calculate_fitness(population,n))

    return fitness

def selection(population , fitness):
    size = len(fitness)
    parents = []
    fitness_copy = fitness.copy()
    for i in range(size//2):
        max_index = 0
        for j  in range(size):
            if fitness[j] > fitness[max_index]:
                max_index = j
        
        parents.append(population[max_index])

        fitness_copy[max_index] = -1        
    print("Parents :" , parents)
    return parents


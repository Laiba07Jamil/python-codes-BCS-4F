import random
n=5

def generate_individual(n):
    return random.sample(range(n),n)

def generate_binary_individual():
    populaiton = []
    for i in range(5):
        populaiton.append(random.randint(0,1))
    return populaiton

def generate_population():
    pop = []
    for i  in range(10):
        pop.append(generate_binary_individual())
    return pop

def generate_popultaion():
    population = []
    population_size = 10
    for i in range(population_size):
        population.append(generate_individual(5))

    return population

def calculate_fitness(individual,n):
    attackin_pairs = 0
    for i in range(n):
        for j in range(i+1 , n):
            if individual[i] != individual[j] and abs(individual[i] - individual[j]) != abs(i-j):
                attackin_pairs += 1

    return attackin_pairs

def evaluate_fitness(population,n):
  fitness = []
  for i in population:
    fitness.append(calculate_fitness(i,n))

  return fitness

def selection(population , fitness):
    combined = list(zip(fitness , population))
    combined.sort(reverse= True , key = lambda x : x[0])
    individual = []
    for _, route in combined:
        individual.append(route)

    size = len(individual) //2
    parents =[]
    for i in range(size):
        parents.append(individual[i])

    return parents

def crossover(parents1,parents2,n):
    point = random.randint(0,n-2)
    child = parents1[:point] + parents2[point:]
    return child

def mutation(individual):
    indx1,indx2 = random.sample(range(5),2)
    individual[indx1],individual[indx2] = individual[indx2],individual[indx1]
    return individual

def mutation_binary(individual):
    index = random.randint(0,len(individual) -1)
    individual[index] = 1-individual[index]
    return individual

def genetic_algorithm():
    population = generate_popultaion()
    best_fitness = 0
    generation = 0

    while best_fitness < 0.01 and generation < 100:
        fitness = evaluate_fitness(population,n)
        parents = selection(population,fitness)
        best_fitness = max(fitness)
        best_individual = population[fitness.index(best_fitness)]
        print(f"Best fitness : {best_fitness} , Generation : {generation} , Best_individual: {best_individual}")

        next_population = []

        for i in range(len(parents)):
            parent1,parent2  = random.sample(parents,2)
            next_population.append(crossover(parent1,parent2,n))

        for i in range(len(parents)):
            if random.randint(0,1) < 1.0:
              next_population[i] = mutation(next_population[i])

        population = next_population
        generation += 1

    return best_fitness , generation




import random

def generate_individual(n):
    return random.sample(range(n),n)

def generate_population():
    population = []
    population_size = 10
    for i in range(population_size):
        population.append(generate_individual(5))
    
    return population

def generate_binary_individual():
    n = 5
    indvidual = []
    for i in range(n):
        indvidual.append(random.randint(0,1))

    return indvidual

def generate_binary_population():
    population = []
    for i in range(10):
        population.append(generate_binary_individual())

    return population

#f(x) = x**2 + x
def calculate_fitness(individual):
    n = len(individual) #will 5 always
    decimal = (individual[0]*2**4 +
                individual[1]*2**3 +
                 individual[2]*2**2 + 
                 individual[3]*2**1 + 
                 individual[4]*2**0)
    
    fitness = (decimal)**2 + decimal
    return fitness

def evaluate_fitness(population):
    fitness = []
    n = len(population)
    for i in population:
        fitness.append(calculate_fitness(i))

    return fitness
    
def Elitisim_selection(popoulation,fitness): #50% selection  
    combined = list(zip(fitness,popoulation))
    combined.sort(key=lambda x:x[0] , reverse=True)
    individual = []
    for _,i in combined:
        individual.append(i)

    parents = []
    size = len(popoulation) //2
    for i in range(size):
        parents.append(individual[i])

    return parents

def roulette_selection(population ,fitness):      #Roulette selection
    total_fitness = sum(fitness)
    parents = []

    for _ in range(len(population)//2):
        pick = random.uniform(0,total_fitness)
        current = 0

        for i in range(len(population)):
            current += fitness[i]
            if current >= pick:
                parents.append(population[i])

    return parents

def single_point_crossover(parent1,parent2):
    point = random.randint(1,len(parent1) - 2)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1,child2

def two_point_crossover(parent1,parent2):
    point1 = random.randint(1,len(parent1) - 2)
    point2 = random.randint(point1 + 1 ,len(parent1) -1)

    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]

    return child1,child2

def uniform_crossover(p1,p2):
    child1 = []
    child2 = []

    for i in range(len(p1)):
        if random.random() < 0.5:
            child1.append(p1[i])
            child2.append(p2[i])
        else:
            child1.append(p2[i])
            child2.append(p1[i])

    return child1,child2

def mutation(p1):
    indx1 , ind2 = random.sample(range(5),2)
    p1[indx1] = p1[ind2]
    p1[ind2] = p1[indx1]

    return p1

def mutation_binary(p1):
    indx = random.randint(0 , len(p1) -2)
    p1[indx] = 1 - p1[indx]
    return p1

def genetic_algorithm():
    population = generate_binary_population()
    generation = 0
    final = 0

    while generation < 10 and final < 63:
        fitness = evaluate_fitness(population)
        selection = roulette_selection(population,fitness)
        next_population = []
        
        for i in selection:
            p1 , p2 = random.sample(selection, 2)
            next_population.append(single_point_crossover(p1,p2))

        for i in next_population:
            if random.randint() < 0.5:
                next_population[i] = mutation_binary(next_population[i])

        population = next_population
        generation += 1
        best = population[0]
        best_fit = calculate_fitness(best)

        for i in population:
            fit = calculate_fitness(population[i])
            if fit > best_fit:
                best_fit = fit
                best = population[i]
    
        final = 2*best_fit + 1
        print(f"Final value is : {final}")



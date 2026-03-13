import random
def fitness(x):
  return x*x+2*x

def toDecimal(chromosome):
  return int(chromosome, 2)

def generateChromosome():
  return ''.join(random.choice('01') for _ in range(5))

def selection(population):
  population.sort(key=lambda c: fitness(toDecimal(c)), reverse=True)
  return population[:2]

def crossover(parent1, parent2):
  point=random.randint(1, 4)
  child1=parent1[:point]+parent2[point:]
  child2=parent1[point:]+parent2[:point]
  return child1, child2

def mutation(chromosome):
  chromosome = list(chromosome)
  point=random.randint(0,4)
  chromosome[point]='1' if chromosome[point]=='0' else '0'
  return ''.join(chromosome)

population = [generateChromosome() for _ in range(6)]

for generation in range(15):
  print(f"Generation: {generation}\nPopulation: {population}\n")
  parent1, parent2 = selection(population)
  child1, child2 = crossover(parent1, parent2)
  child1 = mutation(child1)
  child2 = mutation(child2)
  population=[parent1, parent2, child1, child2, generateChromosome(), generateChromosome()]

best = max(population, key=lambda c: fitness(toDecimal(c)))
x = toDecimal(best)

print(f"Best chromosome: {best}\nBest value of x: {x}\nBest fitness value: {fitness(x)}")
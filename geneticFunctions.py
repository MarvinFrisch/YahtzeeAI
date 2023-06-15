from train import calc_fitness
import numpy as np

from parameters import *

def next_generation(population):
    fitness_score = calc_fitness(population)
    max_score = max(fitness_score)
    print(f"Max Score: {max_score}")
    total_fitness = sum(fitness_score)
    relative_fitness = [i/total_fitness for i in fitness_score]

    next_generation = []
    next_generation.append(population[np.argmax(relative_fitness)])
    for i in range(population_size-1):
        pickedAgent = population[pickAgent(relative_fitness)]
        pickedAgent.mutate()
        next_generation.append(pickedAgent)

    return next_generation

def pickAgent(fitness):
    fitness_threshold = np.random.random()
    index = 0
    while fitness_threshold > 0:
        fitness_threshold -= fitness[index]
        index += 1
    return index-1
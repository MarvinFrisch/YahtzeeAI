from train import calc_fitness
import numpy as np

from parameters import *

def next_generation(population_roll, population_score):
    fitness_score = calc_fitness(population_roll, population_score)
    max_score = max(fitness_score)
    print(f"Max Score: {max_score}")
    total_fitness = sum(fitness_score)
    relative_fitness = [i/total_fitness for i in fitness_score]

    next_generation_roll = []
    next_generation_score = []
    next_generation_roll.append(population_roll[np.argmax(relative_fitness)])
    next_generation_score.append(population_score[np.argmax(relative_fitness)])
    for i in range(population_size-1):
        pickedAgent = population_roll[pickAgentBest(relative_fitness)]
        pickedAgent.mutate()
        next_generation_roll.append(pickedAgent)
        pickedAgent = population_score[pickAgentBest(relative_fitness)]
        pickedAgent.mutate()
        next_generation_score.append(pickedAgent)

    return next_generation_roll, next_generation_score, max_score

def pickAgentThreshold(fitness):
    fitness_threshold = np.random.random()
    index = 0
    while fitness_threshold > 0:
        fitness_threshold -= fitness[index]
        index += 1
    return index-1

def pickAgentBest(fitness):
    return np.argmax(fitness)
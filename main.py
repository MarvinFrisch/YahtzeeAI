from train import *
from geneticFunctions import *
from parameters import *

population_roll = [NeuralNetwork(19, 30, 20, 5) for i in range(population_size)]
population_score = [NeuralNetwork(18, 30, 20, 13) for i in range(population_size)]
max_score = 0

for generation in range(number_of_generations):
    print(f"Generation: {generation}")
    population_roll, population_score, max_score = next_generation(population_roll, population_score)



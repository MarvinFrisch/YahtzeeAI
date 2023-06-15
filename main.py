from train import *
from geneticFunctions import *
from parameters import *

population = [NeuralNetwork(30, 20, 13) for i in range(population_size)]

for generation in range(number_of_generations):
    print(f"Generation: {generation}")
    population = next_generation(population)
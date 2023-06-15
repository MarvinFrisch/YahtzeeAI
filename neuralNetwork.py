import tensorflow as tf
import numpy as np
from parameters import *

class NeuralNetwork:

    def __init__(self, layer1, layer2, output, copy=False):
        if copy:
            self.dense1 = layer1
            self.dense2 = layer2
            self.output = output
        else:
            self.dense1 = tf.keras.layers.Dense(layer1, activation='relu')
            self.dense2 = tf.keras.layers.Dense(layer2, activation='relu')
            self.output = tf.keras.layers.Dense(18, activation='softmax') # 13 possible scoring outputs + 5 reroll options
        self.genModel()

    def genModel(self):
        self.model = tf.keras.models.Sequential()
        self.model.add(tf.keras.Input(shape=(19,)))
        self.model.add(self.dense1)
        self.model.add(self.dense2)
        self.model.add(self.output)

    def call(self, inputs):
        return self.model(inputs)

    def copy(self):
        layer1 = tf.keras.layers.Dense.from_config(self.dense1.get_config())
        layer2 = tf.keras.layers.Dense.from_config(self.dense2.get_config())
        output = tf.keras.layers.Dense.from_config(self.output.get_config())
        copy = NeuralNetwork(layer1, layer2, output, copy=True)
        copy.model.set_weights(self.model.get_weights())
        return copy

    def mutate(self):
        weights = self.model.get_weights()
        for i in range(len(weights)):
            for j in range(len(weights[i])):
                try:
                    for k in range(len(weights[i][j])):
                        if np.random.random() < mutation_chance:
                            weights[i][j][k] += np.random.normal(0, 0.1)
                except Exception:
                    weights[i][j] += np.random.normal()





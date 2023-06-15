from neuralNetwork import *
from YahtzeeMain import *
from parameters import *

def callNetRoll(net, dice, player, toss):
    dice = [i/6 for i in dice]
    net_input = dice + player.scoreCheck + [toss]
    net_input = tf.convert_to_tensor(net_input)
    net_input = tf.reshape(net_input, shape=(1, 19))
    net_output = net.call(net_input).numpy().tolist()[0]

    net_decision = [1 if i > 0.5 else 0 for i in net_output]

    return net_decision

def callNetScore(net, dice, player):
    dice = [i / 6 for i in dice]
    net_input = dice + player.scoreCheck
    net_input = tf.convert_to_tensor(net_input)
    net_input = tf.reshape(net_input, shape=(1, 18))
    net_output = net.call(net_input).numpy().tolist()[0]
    return np.argmax(net_output)

def calc_fitness(population_roll, population_score):
    population_totalScore = [0 for i in range(population_size)]
    for pop_index in range(len(population_roll)):
        net_roll = population_roll[pop_index]
        net_score = population_score[pop_index]
        for game in range(number_of_games):
            player = Player()
            for round in range(13):
                dice = sorted([tossDie() for i in range(5)])
                for toss in range(2):
                    keepMask = callNetRoll(net_roll, dice, player, toss)
                    dice = sorted([dice[i] if keepMask[i] == 1 else tossDie() for i in range(len(dice))])
                scoreIndex = callNetScore(net_score, dice, player)
                if player.scoreCheck[scoreIndex] == 1:
                    zeros = np.where(np.array(player.scoreCheck) == 0)[0]
                    scoreIndex = zeros[np.random.randint(len(zeros))]
                player.scoreCheck[scoreIndex] = 1
                player.detailedScore[scoreIndex] = scoreToss(dice, scoreIndex)
        
            player.calcTotalScore()
            population_totalScore[pop_index] += player.totalScore
        population_totalScore[pop_index] /= number_of_games
    return population_totalScore
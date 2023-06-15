from neuralNetwork import *
from YahtzeeMain import *
from parameters import *

def callNet(net, dice, player, toss):

    net_input = dice + player.scoreCheck + [toss]
    net_input = tf.convert_to_tensor(net_input)
    net_input = tf.reshape(net_input, shape=(1, 19))
    net_output = net.call(net_input).numpy().tolist()[0]

    if toss < 2:
        net_decision = net_output[13:]
        net_decision = [1 if abs(i) > 0.5 else 0 for i in net_decision]
    else:
        net_decision = np.argmax(np.abs(net_output[:13]))

    return net_decision


def calc_fitness(population):
    population_score = [0 for i in range(population_size)]
    for pop_index in range(len(population)):
        net = population[pop_index]
        player = Player()

        for round in range(13):
            dice = sorted([tossDie() for i in range(5)])
            for toss in range(2):
                keepMask = callNet(net, dice, player, toss)
                dice = sorted([dice[i] if keepMask[i] == 1 else tossDie() for i in range(len(dice))])
            scoreIndex = callNet(net, dice, player, 3)
            if player.scoreCheck[scoreIndex] == 1:
                zeros = np.where(np.array(player.scoreCheck) == 0)[0]
                scoreIndex = zeros[np.random.randint(len(zeros))]
            player.scoreCheck[scoreIndex] = 1
            player.detailedScore[scoreIndex] = scoreToss(dice, scoreIndex)

        player.calcTotalScore()
        population_score[pop_index] = player.totalScore

    return population_score
import numpy as np

class Player:
    def __init__(self):
        self.totalScore = 0
        self.detailedScore = [0 for i in range(13)]
        self.scoreCheck = [0 for i in range(13)]

    def calcTotalScore(self):
        self.totalScore = sum(self.detailedScore)
        if sum(self.detailedScore[:6]) >= 63:
            self.totalScore += 35

def tossDie():
    return np.random.randint(1, 7)

def scoreToss(dice, scoreIndex):
    score = 0
    if scoreIndex <= 5:
        score = (scoreIndex+1) * dice.count(scoreIndex+1)
    elif scoreIndex == 6:
        counters = [dice.count(i) for i in range(5)]
        if max(counters)>=3:
            score = sum(dice)
    elif scoreIndex == 7:
        counters = [dice.count(i) for i in range(5)]
        if max(counters) >= 4:
            score = sum(dice)
    elif scoreIndex == 8:
        counters = [dice.count(i) for i in range(5)]
        if counters.count(3) == 1 and counters.count(2) == 1:
            score = 25
    elif scoreIndex == 9:
        if all(x in dice for x in [1,2,3,4]) or all(x in dice for x in [2,3,4,5]) or all(x in dice for x in [3,4,5,6]):
            score = 30
    elif scoreIndex == 10:
        if dice == [1, 2, 3, 4, 5] or dice == [2, 3, 4, 5, 6]:
            score = 40
    elif scoreIndex == 11:
        counters = [dice.count(i) for i in range(5)]
        if max(counters) == 5:
            score = 50
    elif scoreIndex == 12:
        score = sum(dice)
    else:
        score = 0

    return score
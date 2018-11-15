# tennisplayer.py

from random import random


class tennisPlayer:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0
        self.sets = 0
        self.games = 0
        self.wins = 0

    def winsServe(self):
        # Returns a boolean with the given probability of a win
        return random() < self.prob

    def updateScore(self):
        # Adds points for this player
        if self.score == 0 or self.score == 15:
            self.score = self.score + 15
        else:
            self.score = self.score + 10

    def getScore(self):
        # returns score of this player
        return self.score

    def resetScore(self):
        # sets scores for new game
        self.score = 0

    def addSets(self):
        self.sets = self.sets + 1

    def getSets(self):
        return self.sets

    def setGames(self, added):
        self.games = self.games + added

    def getGames(self):
        return self.games

    def addWin(self):
        self.wins = self.wins + 1

    def getWins(self):
        return self.wins

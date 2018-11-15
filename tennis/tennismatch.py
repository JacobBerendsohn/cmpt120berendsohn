# tennismatch.py

from tennisplayer import *
from simstats import *
from random import random


class tennisMatch:
    def __init__(self, probA, probB):
        self.playerA = tennisPlayer(probA)
        self.playerB = tennisPlayer(probB)
        if random() <= .5:
            self.server = self.playerA
        else:
            self.server = self.playerB

    def play(self):
        # play until match is over
        while not self.isOver():
            if self.server.winsServe():
                if self.server == self.playerA:
                    self.playerA.updateScore()
                elif self.server == self.playerB:
                    self.playerB.updateScore()
            elif self.server == self.playerA:
                self.playerB.updateScore()
            elif self.server == self.playerB:
                self.playerA.updateScore()

    def getPlayerWins(self):
        return self.playerA.getWins(), self.playerB.getWins()

    def getScores(self):
        # returns scores for players a and b
        return self.playerA.getScore(), self.playerB.getScore()

    def isOver(self):
        a, b = self.getScores()
        if a >= 50 and a - 20 >= b:
            self.playerA.resetScore()
            self.playerB.resetScore()
            self.playerA.setGames(1)
            if self.playerA.getGames() >= 6 and (self.playerA.getGames() - 2) >= self.playerB.getGames():
                self.playerA.addSets()
                self.switchServer()
                if self.playerA.getSets() - 2 >= self.playerB.getSets():
                    self.playerA.addWin()
                    return True
                else:
                    return False
        elif b >= 50 and b - 20 >= a:
            self.playerA.resetScore()
            self.playerB.resetScore()
            self.playerB.setGames(1)
            if self.playerB.getGames() >= 6 and (self.playerB.getGames() - 2) >= self.playerA.getGames():
                self.playerB.addSets()
                self.switchServer()
                if self.playerB.getSets() - 2 >= self.playerA.getSets():
                    self.playerB.addWin()
                    return True
                else:
                    return False
        else:
            return False

    def switchServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA

    def getPlayerAWins(self):
        return self.playerA.getWins()

    def getPlayerBWins(self):
        return self.playerB.getWins()

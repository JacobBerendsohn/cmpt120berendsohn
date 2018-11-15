# tennissimulation.py
from tennismatch import *
from tennisplayer import *
from simstats import *


def main():
    printIntro()
    totalWinsA = 0
    totalWinsB = 0
    probA, probB, n = getInputs()
    for i in range(n):
        oneGame = tennisMatch(probA, probB)
        oneGame.play()
        totalWinsA, totalWinsB = (totalWinsA + oneGame.getPlayerAWins()), (totalWinsB + oneGame.getPlayerBWins())
    final = SimStats(totalWinsA, totalWinsB)
    final.printReport()


def printIntro():
    # Prints an introduction to the program
    print("This program simulates a game of Tennis between two")
    print('players called "A" and "B". The abilities of each player is')
    print("indicated by a probability (a number between 0 and 1) that")
    print("the player wins the point when serving. A random player")
    print("has the first serve.\n")


def getInputs():
    # Returns probA, proB, number of games to simulate
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

main()

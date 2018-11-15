# simstats.py

from tennismatch import *
from tennisplayer import *


class SimStats:
    def __init__(self, a, b):
        self.winsA = a
        self.winsB = b

    def printReport(self):
        # prints a nicely formatted report
        n = self.winsA + self.winsB
        print("\n\nSummary of", n, "games:\n")
        print("          wins (% total)")
        print("------------------------")
        percA = (self.winsA / n) * 100
        percB = (self.winsB / n) * 100
        print("Player A: ", self.winsA, "  ", percA)
        print("Player B: ", self.winsB, "  ", percB)

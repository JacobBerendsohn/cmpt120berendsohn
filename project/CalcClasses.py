# CalcClasses.py
# Implements a GUI to a calculator with classes
from graphics import *


def main():
    win = drawCalc()
    takeInput(win)


def drawCalc():
    # Setting bound for calculator and buttons
    win = GraphWin("Calculator", 325, 440)
    win.setBackground("mistyrose1")
    win.setCoords(0, -3, 13, 19)

    # Drawing Display on screen
    Rectangle(Point(1, 18), Point(12, 16)).draw(win)

    # Drawing Rectangles
    for col in range(-2, 14, 3):
        for row in range(3, 13, 3):
            Rectangle(Point(row - 2, col + 2), Point(row, col)).draw(win)

    # List for buttons
    but = ["C", "Quit", "", "=", "(-)", "0", ".", "-", "1", "2", "3", "+",
           "4", "5", "6", "*", "7", "8", "9", "/", "M+", "M-", "MR", "MC"]

    # Iteration variable for buttons
    i = 0

    # Drawing buttons in correct rects in calculator GUI
    for col in range(-1, 15, 3):
        for row in range(2, 12, 3):
            Text(Point(row, col), but[i]).draw(win)
            i = i + 1

    return win


def takeInput(win):
    clicked = ""
    i = ""
    equation = []
    printedEquation = Text(Point(0, 0), "")
    printedEquation.undraw()

    # Memory Declaration
    memory = 0

    # Looping to get the equation until equals is pressed
    while (i != "="):
        # Adding clicked character to equation
        equation.append(clicked)
        printed = "".join(equation)

        # Printing equation in shell for confirmation
        print(printed)

        # Removing the last part of equation so there is no overlap
        printedEquation.undraw()
        printedEquation = Text(Point(6.5, 17), printed)

        # Drawing equation on screen
        printedEquation.draw(win)

        # Getting where mouse was clicked
        p = win.getMouse()
        x = p.getX()
        y = p.getY()

        whereClicked = Buttons(x, y, win, printed, memory, printedEquation, equation)
        clicked, equation, memory = whereClicked.findClick()


class Buttons:
    def __init__(self, x, y, win, printed, curMemory, printedEquation, equation):
        self.x = x
        self.y = y
        self.clicked = ""
        self.win = win
        self.printed = printed
        self.memory = curMemory
        self.printedEquation = printedEquation
        self.equation = equation

    def findClick(self):
        # If statement to confirm which character was chosen
        # Memory functions
        if self.y <= 15 and self.y >= 13:
            # M+
            if self.x <= 3 and self.x >= 1:
                self.clicked = ""
                newMem = int(self.printed)
                self.memory = (self.memory + newMem)
            # M-
            elif (self.x <= 6 and self.x >= 4):
                self.clicked = ""
                newMem = int(self.printed)
                self.memory = (self.memory - newMem)
            # MR
            elif (self.x <= 9 and self.x >= 7):
                self.printed = ""
                self.equation = []
                self.clicked = str(self.memory)
            # MC
            elif (self.x <= 12 and self.x >= 10):
                self.clicked = ""
                self.memory = 0
        if (self.y <= 12 and self.y >= 10):
            if (self.x <= 3 and self.x >= 1):
                self.clicked = "7"
            elif (self.x <= 6 and self.x >= 4):
                self.clicked = "8"
            elif (self.x <= 9 and self.x >= 7):
                self.clicked = "9"
            elif (self.x <= 12 and self.x >= 10):
                self.clicked = "/"
        elif (self.y <= 9 and self.y >= 7):
            if (self.x <= 3 and self.x >= 1):
                self.clicked = "4"
            elif (self.x <= 6 and self.x >= 4):
                self.clicked = "5"
            elif (self.x <= 9 and self.x >= 7):
                self.clicked = "6"
            elif (self.x <= 12 and self.x >= 10):
                self.clicked = "*"
        elif (self.y <= 6 and self.y >= 4):
            if (self.x <= 3 and self.x >= 1):
                self.clicked = "1"
            elif (self.x <= 6 and self.x >= 4):
                self.clicked = "2"
            elif (self.x <= 9 and self.x >= 7):
                self.clicked = "3"
            elif (self.x <= 12 and self.x >= 10):
                self.clicked = "+"
        elif (self.y <= 3 and self.y >= 1):
            if (self.x <= 3 and self.x >= 1):
                self.clicked = ""
                # Make it negative (Wont work)
            elif (self.x <= 6 and self.x >= 4):
                self.clicked = "0"
            elif (self.x <= 9 and self.x >= 7):
                self.clicked = "."
            elif (self.x <= 12 and self.x >= 10):
                self.clicked = "-"
        elif (self.y <= 0 and self.y >= -2):
            # Enter
            if (self.x <= 12 and self.x >= 10):
                # Calling calc_functions to get the correct answer
                PrintedDisplay = Display(self.printed)
                FinAnswer = Calculate(PrintedDisplay.getDispNum())
                FinAnswer.concat()
                FinAnswer.calc()

                self.printedEquation.undraw()
                finalAnswer = Text(Point(6.5, 17), FinAnswer.getFinAnswer())
                finalAnswer.draw(self.win)
                # Check to exit the loop
                i = "="
            # Clear
            elif (self.x <= 3 and self.x >= 1):
                self.clicked = ""
                self.printed = ""
                self.equation = []
            # Quit
            elif (self.x <= 6 and self.x >= 4):
                self.win.close()
        # Getting the mouse location after the loop is done iterating

        p = self.win.getMouse()
        self.x = p.getX()
        self.y = p.getY()

        # Clear after = has been pressed
        if ((self.y <= 0 and self.y >= -2) and (self.x <= 3 and self.x >= 1)):
            finalAnswer.undraw()
            takeInput(self.win)
        # Quit after = has been pressed
        if ((self.y <= 0 and self.y >= -2) and (self.x <= 6 and self.x >= 4)):
            self.win.close()
        return self.clicked, self.equation, self.memory



class Display:
    def __init__(self, dispNum):
        self.dispNum = dispNum

    def getDispNum(self):
        return self.dispNum

    def setDispNum(self, newNum):
        self.dispNum = newNum


class Calculate:
    def __init__(self, display):
        self.display = display
        self.finAnswer = 0
        self.endOperation = 0

    def getFinAnswer(self):
        return self.finAnswer

    # Completes the insertion of the new term and deletion of the old
    def ins(self, finalNum, i, equation=[]):
        del equation[i - 1:i + 2]
        equation.insert(i - 1, finalNum)
        print(equation)
        self.display = equation

    # Multiplication Function
    def mult(self, num1, num2):
        self.endOperation = num1 * num2

    # Division Function
    def div(self, num1, num2):
        self.endOperation = num1 / num2

    # Addition Function
    def add(self, num1, num2):
        self.endOperation = num1 + num2

    # Subtraction Function
    def sub(self, num1, num2):
        self.endOperation = num1 - num2

    def concat(self):
        finEq = []
        i = 0
        number = ""

        for n in range(len(self.display)):

            # Checks for the operators in the equation to know where the numbers are in relation to operators
            if self.display[n] == "+" or self.display[n] == "-" or self.display[n] == "*" or self.display[n] == "/":

                number = self.display[n - i: n]
                newNumber = "".join(number)
                finEq.append(newNumber)
                finEq.append(self.display[n])
                i = 0
                number = ""

            # This elif is for the last item in the list
            elif len(self.display) == n + 1:
                number = self.display[n - i: n + 1]
                newNumber = "".join(number)
                finEq.append(newNumber)
                i = 0
                number = ""

            # This is the counter to know how many numbers there are before the operator
            else:
                i = i + 1

        # Returns final concatentated equation to give to calculator function
        self.display = finEq

    # Does main calculations for the calulator
    def calc(self):

        # For loop to loop through given equation, and to close when one index remains
        while len(self.display) != 1:

            # Making sure pemdas works for multiple division and multiplication operators in same equation
            while ("*" in self.display) or ("/" in self.display):

                for i in range(1, len(self.display)):

                    # Beginning PEMDAS by checking for * or /
                    if (self.display[i] == "*") or (self.display[i] == "/"):

                        # Multiplication
                        if self.display[i] == "*":

                            self.mult(float(self.display[i - 1]), float(self.display[i + 1]))
                            self.endOperation = str(self.endOperation)
                            self.ins(self.endOperation, i, self.display)
                            break

                        # Division
                        elif self.display[i] == "/":

                            self.div(float(self.display[i - 1]), float(self.display[i + 1]))
                            self.endOperation = str(self.endOperation)
                            self.ins(self.endOperation, i, self.display)
                            break
                        break

            # Next step in PEMDAS by checking for + or -
            for i in range(1, len(self.display)):

                if (self.display[i] == "+") or (self.display[i] == "-"):

                    # Addition
                    if self.display[i] == "+":

                        self.add(float(self.display[i - 1]), float(self.display[i + 1]))
                        self.endOperation = str(self.endOperation)
                        self.ins(self.endOperation, i, self.display)
                        break

                    # Subtraction
                    elif self.display[i] == "-":

                        self.sub(float(self.display[i - 1]), float(self.display[i + 1]))
                        self.endOperation = str(self.endOperation)
                        self.ins(self.endOperation, i, self.display)
                        break

                    break

        self.finAnswer = self.display[0]
main()

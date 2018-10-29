# calculator.pyw
# Implements a GUI and display for calc_functions.

from graphics import *
import calc_functions

def main():
    win = drawCalc()
    takeInput(win)


def drawCalc():

    # Setting bound for calculator and buttons
    win = GraphWin("Calculator",325,440)
    win.setBackground("mistyrose1")
    win.setCoords(0,-3,13,19)

    # Drawing Display on screen
    Rectangle(Point(1,18),Point(12,16)).draw(win)

    # Drawing Buttons on Calculator with numbers
    # Top Row
    Rectangle(Point(1,15),Point(3,13)).draw(win)
    Text(Point(2,14),"M+").draw(win)
    Rectangle(Point(4,15),Point(6,13)).draw(win)
    Text(Point(5,14),"M-").draw(win)
    Rectangle(Point(7,15),Point(9,13)).draw(win)
    Text(Point(8,14),"MR").draw(win)
    Rectangle(Point(10,15),Point(12,13)).draw(win)
    Text(Point(11,14),"MC").draw(win)

    # Second
    Rectangle(Point(1,12),Point(3,10)).draw(win)
    Text(Point(2,11),"7").draw(win)
    Rectangle(Point(4,12),Point(6,10)).draw(win)
    Text(Point(5,11),"8").draw(win)
    Rectangle(Point(7,12),Point(9,10)).draw(win)
    Text(Point(8,11),"9").draw(win)
    Rectangle(Point(10,12),Point(12,10)).draw(win)
    Text(Point(11,11),"/").draw(win)

    # Third Row
    Rectangle(Point(1,9),Point(3,7)).draw(win)
    Text(Point(2,8),"4").draw(win)
    Rectangle(Point(4,9),Point(6,7)).draw(win)
    Text(Point(5,8),"5").draw(win)
    Rectangle(Point(7,9),Point(9,7)).draw(win)
    Text(Point(8,8),"6").draw(win)
    Rectangle(Point(10,9),Point(12,7)).draw(win)
    Text(Point(11,8),"*").draw(win)

    # Fourth Row
    Rectangle(Point(1,6),Point(3,4)).draw(win)
    Text(Point(2,5),"1").draw(win)
    Rectangle(Point(4,6),Point(6,4)).draw(win)
    Text(Point(5,5),"2").draw(win)
    Rectangle(Point(7,6),Point(9,4)).draw(win)
    Text(Point(8,5),"3").draw(win)
    Rectangle(Point(10,6),Point(12,4)).draw(win)
    Text(Point(11,5),"+").draw(win)

    # Fifth Row
    Rectangle(Point(1,3),Point(3,1)).draw(win)
    Text(Point(2,2),"(-)").draw(win)
    Rectangle(Point(4,3),Point(6,1)).draw(win)
    Text(Point(5,2),"0").draw(win)
    Rectangle(Point(7,3),Point(9,1)).draw(win)
    Text(Point(8,2),".").draw(win)
    Rectangle(Point(10,3),Point(12,1)).draw(win)
    Text(Point(11,2),"-").draw(win)

    # Bottom Row
    Rectangle(Point(10,0),Point(12,-2)).draw(win)
    Text(Point(11,-1),"=").draw(win)
    Rectangle(Point(1,0),Point(3,-2)).draw(win)
    Text(Point(2,-1),"C").draw(win)
    Rectangle(Point(4,0),Point(6,-2)).draw(win)
    Text(Point(5,-1),"Quit").draw(win)
    
    return win
    

def takeInput(win):
    clicked = ""
    i = ""
    equation = []
    printedEquation = Text(Point(0,0),"")
    printedEquation.undraw()

    # Memory Declaration
    memory = 0

    # Looping to get the equation until equals is pressed
    while(i != "="):
        # Adding clicked character to equation
        equation.append(clicked)
        printed = "".join(equation)
        # Printing equation in shell for confirmation
        print(printed)
        # Removing the last part of equation so there is no overlap
        printedEquation.undraw()
        printedEquation = Text(Point(6.5,17), printed)
        # Drawing equation on screen
        printedEquation.draw(win)
        # Getting where mouse was clicked
        p = win.getMouse()
        x = p.getX()
        y = p.getY()
        # If statement to confirm which character was chosen
        # Memory functions
        if(y <= 15 and y >= 13):
            # M+
            if(x <= 3 and x >= 1):
                clicked = ""
                newMem = int(printed)
                memory = (memory + newMem)
            # M-
            elif(x <= 6 and x >= 4):
                clicked = ""
                newMem = int(printed)
                memory = (memory - newMem)
            # MR
            elif(x <= 9 and x >= 7):
                printed = ""
                equation = []
                clicked = str(memory)
            # MC
            elif(x <= 12 and x >= 10):
                clicked = ""
                memory = 0
        if(y <= 12 and y >= 10):
            if(x <= 3 and x >= 1):
                clicked = "7"
            elif(x <= 6 and x >= 4):
                clicked = "8"
            elif(x <= 9 and x >= 7):
                clicked = "9"
            elif(x <= 12 and x >= 10):
                clicked = "/"
        elif(y <= 9 and y >= 7):
            if(x <= 3 and x >= 1):
                clicked = "4"
            elif(x <= 6 and x >= 4):
                clicked = "5"
            elif(x <= 9 and x >= 7):
                clicked = "6"
            elif(x <= 12 and x >= 10):
                clicked = "*"
        elif(y <= 6 and y >= 4):
            if(x <= 3 and x >= 1):
                clicked = "1"
            elif(x <= 6 and x >= 4):
                clicked = "2"
            elif(x <= 9 and x >= 7):
                clicked = "3"
            elif(x <= 12 and x >= 10):
                clicked = "+"
        elif(y <= 3 and y >= 1):
            if(x <= 3 and x >= 1):
                clicked = ""
                # Make it negative (Wont work)
            elif(x <= 6 and x >= 4):
                clicked = "0"
            elif(x <= 9 and x >= 7):
                clicked = "."
            elif(x <= 12 and x >= 10):
                clicked = "-"
        elif(y <= 0 and y >= -2):
            # Enter
            if(x <= 12 and x >= 10):
                # Calling calc_functions to get the correct answer
                answer = calc_functions.main(printed)
                printedEquation.undraw()
                finalAnswer = Text(Point(6.5,17), answer)
                finalAnswer.draw(win)
                # Check to exit the loop
                i = "="
            # Clear
            elif(x <= 3 and x >= 1):
                clicked = ""
                printed = ""
                equation = []
            # Quit
            elif(x <= 6 and x >= 4):
                win.close()
    # Getting the mouse location after the loop is done iterating
    p = win.getMouse()
    x = p.getX()
    y = p.getY()
    # Clear after = has been pressed
    if((y <= 0 and y >= -2) and (x <= 3 and x >= 1)):
        answer = calc_functions.main(printed)
        finalAnswer.undraw()
        takeInput(win)
    # Quit after = has been pressed
    if((y <= 0 and y >= -2) and (x <= 6 and x >= 4)):
        win.close()
main()



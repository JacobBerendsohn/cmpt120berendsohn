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

    # Drawing Rectangles
    for col in range(-2, 14, 3):
        for row in range(3, 13, 3):
            Rectangle(Point(row-2,col+2),Point(row,col)).draw(win)

    # List for buttons
    but = ["C","Quit","","=","(-)","0",".","-","1","2","3","+",
           "4","5","6","*","7","8","9","/","M+","M-","MR","MC"]
    
    # Iteration variable for buttons
    i = 0

    # Drawing buttons in correct rects in calculator GUI
    for col in range(-1, 15, 3):
        for row in range(2, 12, 3):
            Text(Point(row, col),but[i]).draw(win)
            i = i+1
    
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



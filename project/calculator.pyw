# calculator.pyw
# Implements a GUI and display for calc_functions.

from graphics import *

def main():
    drawCalc()


def drawCalc():

    # Setting bound for calculator and buttons
    win = GraphWin("Calculator",325,380)
    win.setBackground("grey")
    win.setCoords(0,0,13,19)

    # Drawing Display on screen
    Rectangle(Point(1,18),Point(12,16)).draw(win)

    # Drawing Buttons on Calculator with numbers
    # Top Row
    Rectangle(Point(1,15),Point(3,13)).draw(win)
    Text(Point(2,14),"7").draw(win)
    Rectangle(Point(4,15),Point(6,13)).draw(win)
    Text(Point(5,14),"8").draw(win)
    Rectangle(Point(7,15),Point(9,13)).draw(win)
    Text(Point(8,14),"9").draw(win)
    Rectangle(Point(10,15),Point(12,13)).draw(win)
    Text(Point(11,14),"/").draw(win)

    # Second Row
    Rectangle(Point(1,12),Point(3,10)).draw(win)
    Text(Point(2,11),"4").draw(win)
    Rectangle(Point(4,12),Point(6,10)).draw(win)
    Text(Point(5,11),"5").draw(win)
    Rectangle(Point(7,12),Point(9,10)).draw(win)
    Text(Point(8,11),"6").draw(win)
    Rectangle(Point(10,12),Point(12,10)).draw(win)
    Text(Point(11,11),"x").draw(win)

    # Third Row
    Rectangle(Point(1,9),Point(3,7)).draw(win)
    Text(Point(2,8),"1").draw(win)
    Rectangle(Point(4,9),Point(6,7)).draw(win)
    Text(Point(5,8),"2").draw(win)
    Rectangle(Point(7,9),Point(9,7)).draw(win)
    Text(Point(8,8),"3").draw(win)
    Rectangle(Point(10,9),Point(12,7)).draw(win)
    Text(Point(11,8),"+").draw(win)

    # Forth Row
    Rectangle(Point(1,6),Point(3,4)).draw(win)
    Text(Point(2,5),"(-)").draw(win)
    Rectangle(Point(4,6),Point(6,4)).draw(win)
    Text(Point(5,5),"0").draw(win)
    Rectangle(Point(7,6),Point(9,4)).draw(win)
    Text(Point(8,5),".").draw(win)
    Rectangle(Point(10,6),Point(12,4)).draw(win)
    Text(Point(11,5),"-").draw(win)

    # Bottom Row
    Rectangle(Point(10,3),Point(12,1)).draw(win)
    Text(Point(5,2),"C").draw(win)
    Rectangle(Point(1,3),Point(9,1)).draw(win)
    Text(Point(11,2),"=").draw(win)

main()



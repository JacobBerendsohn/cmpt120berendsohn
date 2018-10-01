# calculator.py
# Attempt to make a calculator using python

import graphics

def main():
    drawCalc()


def drawCalc():
    i = 0
    x = 25
    y = 80
    win = graphics.GraphWin("Calculator", 325, 380)

    # Display
    graphics.Rectangle(graphics.Point(x, y-60), graphics.Point(x+275, y-20)).draw(win)

    # Clear
    graphics.Rectangle(graphics.Point(x+65, y+240), graphics.Point(x+210, y+280)).draw(win)

    for i in range(16):
        if(i != 0 and i%4==0):
            y = y + 60
            x = x - 300
        rectTop = graphics.Point(x, y)
        rectBot = graphics.Point(x+50, y+40)
        graphics.Rectangle(rectTop, rectBot).draw(win)
        x = x + 75

main()

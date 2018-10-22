# CMPT 120 Intro to Programming
# Lab #6 – Lists and Error Handling
# Author: Your Name Here
# Created: YYYY-MM-DD
symbol = [ " ", "x", "o" ]

def printRow(row):
    # initialize output to the left border
    # for each square in the row...
    # add to output the symbol for this square followed by a border
    # print the completed output for this row
    pass

def printBoard(board):
    rowStr = "+-----------+"
    posVal = [" ", " ", " "]
    # Goes through list to print everything
    # Changes the values of the positions to display x or o
    for rows in range(3):
        print(rowStr)
        for cols in range(3):
            if(board[rows][cols] == 0):
                posVal[cols] = " "
            elif(board[rows][cols] == 1):
                posVal[cols] = "x"
            else:
                posVal[cols] = "o"
        # Prints the rows 3 times and not 4
        if(rows != 3):
            print("|",posVal[0],"|",posVal[1],"|",posVal[2],"|")
    # Prints the last bound one more time for the bottom
    print(rowStr)
    pass

def markBoard(board, row, col, player):
    # Making a requirement to check if selected tile is empty
    isTrue = True
    while isTrue:
        if(board[row][col] == 0):
            board[row][col] = player
            isTrue = False
        # Getting a new move if space is already taken
        else:
            row,col = getPlayerMove()
        

def getPlayerMove():
    # Inputting rows and columns
    rowNum = input("Enter the row you would like to play on:")
    colNum = input("Now the column:")
    # Making the inputs numbers
    # Subbing one so it is the correct rows and columns for code
    rowNum = (int(rowNum) - 1)
    colNum = (int(colNum) - 1)
    return (rowNum,colNum)

def hasBlanks(board):
    # Created a checker for number of blanks
    numEmpty = 0
    # 2 For loops for each row and column
    for rows in range(3):
        for cols in range(3):
            if(board[rows][cols] == 0):
                numEmpty = (numEmpty + 1)
    # Checking if board still contains blanks
    if(numEmpty == 0):
        return False
    else:
        return True

def main():
    board = [[0,0,0],[0,0,0],[0,0,0]]
    # Starting Player
    player = 1
    while hasBlanks(board):
        printBoard(board)
        row,col = getPlayerMove()
        markBoard(board,row,col,player)
        # switch player for next turn
        player = player % 2 + 1 
    printBoard(board)

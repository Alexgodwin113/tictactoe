from locale import currency
import random
from turtle import position


board = ["-","-","-",
        "-","-","-",
        "-","-","-"]
currentPlayer = "X"
winner =None
gameRunning = True

#printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2] )
    print("------")
    print(board[3] + " | " + board[4] + " | " + board[5] )
    print("------")
    print(board[6] + " | " + board[7] + " | " + board[8] )

#take player input

def playerInput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1]=="-":
        board[inp-1] = currentPlayer
    else :
        print("Oops player is already in that spot!")


# computer

def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()



#check for win or tie
def checkhorizontal(board):
    global winner #as winner is a global variable we should mention it while using it within a fucntion scope
    if board[0] == board [1] == board [2] and board[1] !="-":
        winner = board[0]
        return True #it helps when we call the fucntions to use if statments to check if it retunrs true and put some condition to it(like brak the game if ts true)
    elif board[3] == board [4] == board [5] and board[3] !="-":
        winner = board[3]
        return True
    elif board[6] == board [7] == board [8] and board[6] !="-":
        winner = board[6]
        return True

def checkrow(board):
    global winner 
    if board[0] == board [3] == board [6] and board[0] !="-":
        winner = board[0]
        return True 
    elif board[1] == board [4] == board [7] and board[1] !="-":
        winner = board[1]
        return True
    elif board[2] == board [5] == board [8] and board[2] !="-":
        winner = board[2]
        return True

def checkDiag(board):
    global winner 
    if board[0] == board [4] == board [8] and board[0] !="-":
        winner = board[0]
        return True 
    elif board[2] == board [4] == board [6] and board[2] !="-":
        winner = board[2]
        return True

def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

def checkWin(board):
    if checkDiag(board) or checkhorizontal(board) or checkrow(board):
        print(f"The winner is {winner}")
        gameRunning = False
        

#switch the player

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

#check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin(board)
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin(board)
    checkTie(board)

import random
from time import sleep

#------ Global Variables ------
tiles = [1,2,3,4,5,6,7,8,9]
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# if game is still going
game_still_going = True
winner = None
tie = None
currentPlayer = ""

def drawBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def players():
    global currentPlayer
    print("Select your sign")
    print("X or O")
    p1 = input("Player 1: " )
    p1 = p1.upper()
    currentPlayer = p1
    p2 = ""
    if p1 == "X":
        p2 = "O"
        print("Player 2: " + p2)
    elif p1 == "O":
        p2 = "X"
        print("Player 2: " + p2)

def handleTurn(player):
    position = int(input("Choose a position from 1-9: "))
    position = position - 1

    board[position] = player
    drawBoard()

def check_if_game_over():
    check_for_winner()
    checkTie()

def check_for_winner():
    #set up global variable
    global winner 

    #check rows
    row_winner = check_rows()
    #check colums
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        #there was a win
        winner = diagonal_winner
    else:
        #there was no win
        winner = None
    return

def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board [2] != "-"
    row_2 = board[3] == board[4] == board [5] != "-"
    row_3 = board[6] == board[7] == board [8] != "-"

    #if any row has a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    #return the winner( X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    #if any column has a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    
    #return the winner( X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going

    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"

    #if any diagonal has a match, flag that there is a win
    if diag_1 or diag_2:
        game_still_going = False
    
    #return the winner( X or O)
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    return


def checkTie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return

def switchPlayer():
    global currentPlayer

    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"
    return

#play game of tic tac toe
def playGame():

    #display initial board
    drawBoard()
    players()
    
    #while the game is still going
    while game_still_going:

        #handle a single turn of arbitrary player
        handleTurn(currentPlayer)

        #check if game has ended
        check_if_game_over()

        #flip to other player
        switchPlayer()

    #The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie game.")

playGame()

#def checkPossibilities(board):
#    l = []
#    for i in range(len(board)):
#        for j in range(len(board)):
#            if board[i][j] = 0:
#                l.append((i, j))
#    return(l)

# def inputPlayerLetter():
#     userLetter = input("Would you like to be X or O? ")
#     userLetter = userLetter.upper()
#     if userLetter == "X":
#         cpuLetter = "O"
#     else:
#         cpuLetter = "X"
#     return userLetter

# def makeMove():

#     position = int(input("Pick a number for where you want to go: "))
#     for x in tiles:
#         if x == position:
#             tiles.pop(tiles[x])
            
#     inputPlayerLetter()
#     drawBoard(board)
#     if position == 1:
#         board[0][0] = userLetter
#     elif position == 2:
#         board[0][1] = userLetter
#     elif position == 3:
#         board[0][2] = userLetter
#     elif position == 4:
#         board[1][0] = userLetter
#     elif position == 5:
#         board[1][1] = userLetter
#     elif position == 6:
#         board[1][2] = userLetter
#     elif position == 7:
#         board[2][0] = userLetter
#     elif position == 8:
#         board[2][1] = userLetter
#     elif position == 9:
#         board[2][2] = userLetter


# #def cpuMove():
#     sleep(2)
#     cputurn = random.choice(tiles)
#     for y in tiles:
#         if y == cputurn:
#             tiles.pop(tiles[y])

#     if position == 1:
#         board[0][0] = cpuLetter
#     elif position == 2:
#         board[0][1] = cpuLetter
#     elif position == 3:
#         board[0][2] = cpuLetter
#     elif position == 4:
#         board[1][0] = cpuLetter
#     elif position == 5:
#         board[1][1] = cpuLetter
#     elif position == 6:
#         board[1][2] = cpuLetter
#     elif position == 7:
#         board[2][0] = cpuLetter
#     elif position == 8:
#         board[2][1] = cpuLetter
#     elif position == 9:
#         board[2][2] = cpuLetter

#     drawBoard(board)

# #def play():
    # drawboard(board)
    # sleep(2)
    # inputPlayerLetter()
    # sleep(1)
    # makeMove()

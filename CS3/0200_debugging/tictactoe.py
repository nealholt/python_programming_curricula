'''
The following game of TicTacToe contains many errors, omissions, and mistakes.

For 100 points, fix this code, recording the before and after of at least
twelve mistakes along the way. Also, describe briefly (one or two sentences)
how you tracked down the more difficult to find bugs.

You will turn in:
    1. Working tic tac toe code
    2. A list of twelve mistakes with code showing before and after the fix.
       If the fix was a big change, just summarize it.
    3. A brief description of how you tracked down at least two bugs.

Use print or the step-thru debugger.

Hint: If you're having trouble finding twelve mistakes, consider what happens
if a player types in the wrong row or column.
'''

#Create the game board
board = []
for _ in range(3):
    board.append([' ',' ',' '])

#This function returns True if the game is over, False otherwise.
def checkForWin(board):
    #Check rows and columns for three in a row.
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]:
            return True
        if board[0][i]==board[1][i]==board[2][i]:
            return True
    #Check the diagonals
    if board[0][0]==board[1][1]==board[2][2]:
        return True
    if board[0][2]==board[1][1]==board[2][0]:
        return True
    else:
        return False

#Mark a team symbol on the indicated row and column on the board.
def markBoard(row, column, team, board):
    board[row][column] = team

#Print the board in a more readable format
def printBoard(board):
    print()
    for row in board:
        to_print = ''
        for c in row:
            to_print+=c
        print(to_print)

#Begin the game. X goes first.
team = 'X'
while not checkForWin(board):
    #Get the row and column
    row = input(team +' player, what row?')
    col = input(team +' player, what column?')
    markBoard(col, row, team, board)
    #Switch whose turn it is
    if team == 'X':
        team = 'O'
    else:
        team == 'X'
    #Check for a win
    if checkForWin(board):
        print('Congratulations '+team+'! You won!')

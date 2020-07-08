board = []
for _ in range(3):
    board.append([' ',' ',' '])

def checkForWin(board):
    #ERROR: this returns True on the empy board
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]: #ERROR
            return True
        if board[0][i]==board[1][i]==board[2][i]: #ERROR
            return True
    #Check the diagonals
    if board[0][0]==board[1][1]==board[2][2]: #ERROR
        return True
    if board[0][2]==board[1][1]==board[2][0]: #ERROR
        return True
    else: #ERROR
        return False

def markBoard(row, column, team, board):
    board[row][column] = team

def printBoard(board): #ERROR: this function is never called.
    for row in board:
        to_print = ''
        for c in row:
            to_print+=c
        print(to_print)

team = 'X'
while not checkForWin(board):
    row = input(team +' player, what row?') #ERROR these need converted to int
    col = input(team +' player, what column?') #ERROR these need converted to int
    markBoard(col, row, team, board) #ERROR
    if team == 'X':
        team = 'O'
    else:
        team == 'X' #ERROR
    if checkForWin(board): #ERROR this should go before team switch
        print('Congratulations '+team+'! You won!')

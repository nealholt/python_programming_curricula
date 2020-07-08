#This works, but you can still overwrite your opponent's answers.

board = []
for _ in range(3):
    board.append(['.','.','.'])

def checkForWin(board):
    for i in range(3):
        if board[i][0]==board[i][1] and board[i][1]==board[i][2]:
            if board[i][0]!='.':
                return True
        if board[0][i]==board[1][i] and board[1][i]==board[2][i]:
            if board[0][i]!='.':
                return True
    #Check the diagonals
    if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
        if board[0][0]!='.':
            return True
    if board[0][2]==board[1][1] and board[1][1]==board[2][0]:
        if board[0][2]!='.':
            return True
    return False

def markBoard(row, column, team, board):
    board[row][column] = team

def printBoard(board):
    for row in board:
        to_print = ''
        for c in row:
            to_print+=c
        print(to_print)

team = 'X'
while not checkForWin(board):
    row = int(input(team +' player, what row?'))
    col = int(input(team +' player, what column?'))
    markBoard(row, col, team, board)
    if checkForWin(board):
        print('Congratulations '+team+'! You won!')
    if team == 'X':
        team = 'O'
    else:
        team = 'X'
    print()
    printBoard(board)

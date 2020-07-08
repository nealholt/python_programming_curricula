import pygame, random, block

'''
This uses 2d arrays, nested loops, and recursion.
This is similar to the waves code in many respsects.
'''

#Setup
pygame.init()
width = 700
height = 550
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 32)
end_game_font = pygame.font.SysFont('Arial', 64)
black = 0,0,0
white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
tiles = 10 #Count of rows and columns in the board
size = 50 #Size of each tile in the board

score = 0
goal = 25
clicks = 3

def pickRandomColor():
    r = random.randint(0,4)
    if r == 0:
        return red
    elif r == 1:
        return green
    elif r == 2:
        return blue
    else:
        return yellow


#Respond to mouse click
def click(pos, board):
    row, col = getClickedRowCol(pos, board)
    clickTile(row, col, board)
    refillBoard(board)
    global clicks
    clicks = clicks-1


#Given mouse position and the board, determine row and col of cell clicked on.
#Look at the waves code for starters.
def getClickedRowCol(pos, board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col].rect.collidepoint(pos):
                return row, col
    return None


#Given a row and column, delete all touching same colors
def clickTile(row, col, board):
    color = board[row][col].color
    #delete current row,col
    board[row][col].color = None
    #Update score
    global score
    score = score + 1
    #Redraw to show updated screen
    draw()
    #recursively delete above, below, and to each side.
    if row>0 and board[row-1][col].color==color:
        clickTile(row-1,col,board)
    if row<len(board)-1 and board[row+1][col].color==color:
        clickTile(row+1,col,board)
    if col>0 and board[row][col-1].color==color:
        clickTile(row,col-1,board)
    if col<len(board[row])-1 and board[row][col+1].color==color:
        clickTile(row,col+1,board)


#Slide empty cells down and refill the top with new cells
def refillBoard(board):
    #Slide down all tiles. Basically bubble sort each column.
    for col in range(len(board[0])):
        #Continue pushing cells down until no more swaps are made
        swapped = True
        while swapped:
            swapped = False
            #If the top cell is empty, add a new tile there.
            if board[0][col].color == None:
                board[0][col].color = pickRandomColor()
            #Redraw to show updated screen
            draw()
            #Do one bubble sort pass of the column
            for row in range(len(board)):
                #If there is an empty cell beneath current cell, slide current cell down
                if board[row][col].color != None and \
                row<len(board)-1 and \
                board[row+1][col].color==None:
                    temp = board[row][col].color
                    board[row][col].color = None
                    board[row+1][col].color = temp
                    swapped = True
                    #Redraw to show updated screen
                    draw()

#Generate or regenerate a board
def resetBoard(screen, tiles, size):
    board = []
    for row in range(tiles):
        temp = []
        for col in range(tiles):
            temp.append(block.Block(screen, col*size, row*size, pickRandomColor(), size))
        board.append(temp)
    return board



def draw():
    #fill screen with black
    screen.fill(black)
    #Draw the board
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col].draw()
    #Draw score, goal, clicks remaining
    screen.blit(font.render('Score: '+str(score),
                True,white), (520, 50))
    screen.blit(font.render('Goal: '+str(goal),
                True,white), (520, 100))
    screen.blit(font.render('Clicks: '+str(clicks),
                True,white), (520, 150))
    if clicks <= 0:
        if score >= goal:
            screen.blit(end_game_font.render('YOU WON',
                True,white), (width/2-150, height/2-150))
        else:
            screen.blit(end_game_font.render('GAME OVER',
                True,white), (width/2-150, height/2-150))
    #Update the screen
    pygame.display.flip()
    #Delay to get 15 fps
    clock.tick(15)


#Fill the board with colors
board = resetBoard(screen, tiles, size)

#Main loop
done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if clicks > 0:
                pos = pygame.mouse.get_pos()
                click(pos, board)
            else: #reset game
                board = resetBoard(screen, tiles, size)
                score = 0
                clicks = 3
    draw()
pygame.quit()
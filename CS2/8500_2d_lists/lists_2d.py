import pygame,random
#Initialize pygame content
pygame.init()

#All keyboard and mouse input will be handled by the following function
def handleEvents():
    global awaiting_row, awaiting_col
    #Check for new events
    for event in pygame.event.get():
        #This if makes it so that clicking the X actually closes the game
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
        #Has any key been pressed?
        elif event.type == pygame.KEYDOWN:
            #Escape key also closes the game.
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); exit()
            #The event key for zero is 48 so we subtract 48
            #and then every number is its own key.
            number = event.key-48
            print(event.key-48)
            if awaiting_row:
                colorRow(number)
                awaiting_row = False
            else:
                colorColumn(number)
                awaiting_col = False


def colorRow(row):
    '''Paint the given row yellow.'''
    global row_guess
    row_guess = row
    for c in range(len(grid[row])):
        pygame.draw.rect(surface, yellow, grid[row][c])
    pygame.draw.rect(surface, red, grid[red_row][red_column])
    #Update the display surface with the new things that have been drawn
    pygame.display.flip()

def colorColumn(column):
    '''Paint the given column yellow.'''
    global row_guess
    for row in grid:
        pygame.draw.rect(surface, yellow, row[column])
    pygame.draw.rect(surface, red, grid[red_row][red_column])
    #Update the display surface with the new things that have been drawn
    pygame.display.flip()
    #Check if the player guessed the correct grid cell.
    if row_guess == red_row and column == red_column:
        print('CORRECT')
        print('grid['+str(row_guess)+']['+str(column)+']')
        clock.tick(1)
    else:
        print('wrong')
        print('your guess:     grid['+str(row_guess)+']['+str(column)+']')
        print('correct answer: grid['+str(red_row)+']['+str(red_column)+']')
        clock.tick(0.2)

#Initialize variables:
clock = pygame.time.Clock()
screen_width = 450
screen_height = 450
surface = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
yellow = 250,250,0
black = 0,0,0

#Boolean to determine if input should be row or column
awaiting_row = False
awaiting_col = False
#Store user input in these variables
row_guess = -1

#Create a grid of rectangles
size = 30
buffered_size = 35
screen_buffer = 50
grid = []
for row in range(8):
    temp_row = []
    for col in range(8):
        x = col*buffered_size+screen_buffer
        y = row*buffered_size+screen_buffer
        temp = pygame.Rect(x, y, size, size)
        temp_row.append(temp)
    grid.append(temp_row)

#Main program loop
while True:
    if awaiting_row or awaiting_col:
        if awaiting_row:
            print('Type in the row    grid[row][column]')
        else:
            print('Type in the column grid['+str(row_guess)+'][column]')
        handleEvents()
    else:
        #Reset awaiting variables
        awaiting_row = True
        awaiting_col = True
        #erase everything on the screen to black
        surface.fill(black)
        #Choose random rectangle to color
        red_row = random.randint(0,len(grid)-1)
        red_column = random.randint(0,len(grid[0])-1)
        #Draw the grid of rectangles
        for row in grid:
            for col in row:
                pygame.draw.rect(surface, green, col)
        pygame.draw.rect(surface, red, grid[red_row][red_column])
        #Update the display surface with the new things that have been drawn
        pygame.display.flip()
    #Delay to get 10 fps
    clock.tick(10)

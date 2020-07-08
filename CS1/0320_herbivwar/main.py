import pygame, block, critter, critterAI1, critterAI2, random

'''
Instructions:

Files attached.
Make sure to COPY THE FILES OUT of the zip folder after downloading it.
Run main.py
Edit critterAI1 and/or critterAI2

You can change your critter image and team name in main.py at
#Put a critter in the world
team = 0; row = 0; col = 0; team0_name = 'Frog'
critter_cells[row][col] = critterAI1.CritterAI1(screen, row, col, frames[0], team, team0_name)
critter_cells[row][col].direction_index = 1 #face east
team = 1; row = 9; col = 9; team1_name = 'Caterpillar'
critter_cells[row][col] = critterAI2.CritterAI2(screen, row, col, frames[12], team, team1_name)
critter_cells[row][col].direction_index = 3 #face west

'''

#Setup
pygame.init()
width = 800
height = 800
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 32)
black = 0,0,0
white = 255,255,255
tiles = 10 #Count of rows and columns in the board
size = 78 #Size of each tile in the board


def strip_from_sheet(sheet, start, img_size, columns, rows):
	"""Strips individual frames from a sprite sheet given
	a start location, sprite size, and number of
	columns and rows."""
	frames = []
	for j in range(rows):
		for i in range(columns):
			location = (start[0]+img_size[0]*i,
						start[1]+img_size[1]*j)
			rect = pygame.Rect(location, img_size)
			frames.append(sheet.subsurface(rect))
	return frames


#Image source: https://funnyjunk.com/channel/pokemon/Pokemon+green+sprites/qstsGdf/
sheet = pygame.image.load('pokemons.png')
sheet_size = sheet.get_size()
num_rows = 11
num_cols = 15
dimensions = (int(sheet_size[0]/num_cols),int(sheet_size[1]/num_rows))
frames = strip_from_sheet(sheet,
						(0,0), #start
						dimensions, #size
						num_cols, #columns
						num_rows) #rows


#Scale up the image
scaling = 1.2
dimensions = (int(dimensions[0]*scaling), int(dimensions[1]*scaling))
for i in range(len(frames)):
	frames[i] = pygame.transform.scale(
							frames[i],
							dimensions)


def draw():
    #fill screen with black
    screen.fill(black)
    #Draw the board
    for row in range(len(board)):
        for col in range(len(board[row])):
            board[row][col].draw()
            if critter_cells[row][col] != None:
                critter_cells[row][col].draw(size)
    pygame.display.flip()
    #Delay to get 60 fps
    clock.tick(60)


#Fill the board with colors
board = []
critter_cells = []
for row in range(tiles):
    temp = []
    temp2 = []
    for col in range(tiles):
        temp.append(block.Block(screen, col*size, row*size, size))
        temp2.append(None)
    board.append(temp)
    critter_cells.append(temp2)

#Put critters in the world.
#Starting both critters mid-board facing left
#reduces the advantage that the upper-leftmost player has
team = 0; row = 4; col = 5; team0_name = 'Frog'
critter_cells[row][col] = critterAI1.CritterAI1(screen, row, col, frames[random.randint(0,100)], team, 'Connor')
critter_cells[row][col].direction_index = 3 #face west
team = 1; row = 5; col = 5; team1_name = 'Caterpillar'
critter_cells[row][col] = critterAI2.CritterAI2(screen, row, col, frames[random.randint(0,100)], team, 'Jake')
critter_cells[row][col].direction_index = 3 #face west

#Main loop
done = False
round_limit = 100
count = 0
team0 = -1
team1 = -1
while not done and count<round_limit and team0!=0 and team1!=0:
    count += 1
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
    #Increase energy of all blocks
    for row in range(tiles):
        for col in range(tiles):
            board[row][col].energy += 1
    #Each loop through all the critters, count how many
    #there are. End early if one team wins
    team0 = 0
    team1 = 0
    #Update all the critters
    for row in range(tiles):
        for col in range(tiles):
            if critter_cells[row][col]!=None:
                if critter_cells[row][col].energy <= 0:
                    #Remove dead critters
                    critter_cells[row][col] = None
                else:
                    #Reset data
                    critter_cells[row][col].energy_change = 0
                    critter_cells[row][col].damage_taken = 0
                    #Choose action
                    action = critter_cells[row][col].takeAction(board,critter_cells)
                    critter_cells[row][col].recent_action = action
                    if action=='move':
                        critter_cells[row][col].move(critter_cells)
                    elif action=='right':
                        critter_cells[row][col].turnRight()
                    elif action=='left':
                        critter_cells[row][col].turnLeft()
                    elif action=='eat':
                        critter_cells[row][col].eat(board)
                    elif action=='reproduce':
                        critter_cells[row][col].reproduce(critter_cells)
                    elif action=='attack':
                        critter_cells[row][col].attack(critter_cells)
                    elif action=='rest':
                        critter_cells[row][col].rest()
                    draw()
                    #Get a count of each team to either
                    #end early or determine who won at the end
                    if critter_cells[row][col].team==0:
                        team0+=1
                    else:
                        team1+=1

if not done:
    #Determine winner and display winner text
    text = ''
    if team0>team1:
        text = team0_name+' is the Winner'
    elif team0<team1:
        text = team1_name+' is the Winner'
    else:
        text = 'Tie'
    end_game_font = pygame.font.SysFont('Arial', 80)
    screen.blit(end_game_font.render(text,True,white), (width/2-350, height/2-150))
    pygame.display.flip()
    import time
    time.sleep(4)

pygame.quit()
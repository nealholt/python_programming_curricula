import pygame, math, random

pygame.init()

initial_width = 144
initial_height = 144

scaling = 0.75

tile_width = int(initial_width*scaling)
tile_height = int(initial_height*scaling)

board_dimensions = 5
map_width = int(board_dimensions*tile_width)
map_height = int(board_dimensions*tile_height)

white = (255,255,255)
red = (255,0,0)

direction_list = ['north', 'east', 'south', 'west']

options = ['move','left','right']


def getPlayerAt(players, row, col):
    '''Returns player at given location or returns None.'''
    for p in players:
        if p.row == row and p.col == col:
            return p
    return None

def outOfBounds(board,row,col):
    return row<0 or col<0 or row>=len(board) or col>=len(board[0])

def canMove(board, players, row, col, direction):
    #Robots can always move out of bounds
    if outOfBounds(board, row, col):
        return True
    #Check indicated direction
    if direction == 0: #north
        #Make sure there is no wall to the north
        if board[row][col] != '1wu ':
            #If there is a player to the north...
            if getPlayerAt(players, row, col) != None:
                #...then recursively check that it can be moved north
                return canMove(board, players, row-1, col, direction)
    elif direction == 1: #east
        #Make sure there is no wall to the east
        if board[row][col] != '1wr ':
            #If there is a player to the east...
            if getPlayerAt(players, row, col+1) != None:
                #...then recursively check that it can be moved east
                return canMove(board, players, row, col+1, direction)
    elif direction == 2: #south
        #Make sure there is no wall to the south
        if board[row][col] != '1wd ':
            #If there is a player to the south...
            if getPlayerAt(players, row+1, col) != None:
                #...then recursively check that it can be moved south
                return canMove(board, players, row+1, col, direction)
    elif direction == 3: #west
        #Make sure there is no wall to the west
        if board[row][col] != '1wl ':
            #If there is a player to the west...
            if getPlayerAt(players, row, col-1) != None:
                #...then recursively check that it can be moved west
                return canMove(board, players, row, col-1, direction)
    else:
        print('ERROR This should be impossible.')
        exit()

class Robot:
    def __init__(self, screen, row, col, color):
        self.screen = screen
        self.row = row
        self.col = col
        self.color = color
        self.sides = 3
        self.radius = 40*scaling
        self.direction = 0
        self.checkpoint = (row,col)
    def doAction(self, board, players, action):
        if action == 'left':
            self.rotateLeft()
        elif action == 'right':
            self.rotateRight()
        elif action == 'move':
            self.move(board, players)
    def update(self, board):
        r = random.randint(0,2)
        if r == 0:
            return 'left'
        elif r == 1:
            return 'right'
        else:
            return 'move'
    def rotateLeft(self):
        self.direction -= 1
        if self.direction < 0:
            self.direction = len(direction_list)-1
    def rotateRight(self):
        self.direction = (self.direction+1)%len(direction_list)
    def forceMove(self, players, direction):
        temp_row = self.row
        temp_col = self.col
        if direction == 0: #north
            temp_row -= 1
        elif direction == 1: #east
            temp_col += 1
        elif direction == 2: #south
            temp_row += 1
        elif direction == 3: #west
            temp_col -= 1
        #Check for another player that got shoved and
        #pass the shove down the line.
        p = getPlayerAt(players, temp_row, temp_col)
        if p != None:
            p.forceMove(players, direction)
        #Complete the move
        self.row = temp_row
        self.col = temp_col
        self.eventAtLocation(board)
    def move(self, board, players):
        if canMove(board, players, self.row, self.col, self.direction):
            temp_row = self.row
            temp_col = self.col
            if self.direction == 0: #north
                temp_row -= 1
            elif self.direction == 1: #east
                temp_col += 1
            elif self.direction == 2: #south
                temp_row += 1
            elif self.direction == 3: #west
                temp_col -= 1
            #If someone else is in this space, shove them.
            p = getPlayerAt(players, temp_row, temp_col)
            if p != None:
                p.forceMove(players, self.direction)
            #Complete the move
            self.row = temp_row
            self.col = temp_col
            self.eventAtLocation(board)
    def eventAtLocation(self, board):
        '''Check for and activate any event at current location'''
        #Check for off the board and reset to a checkpoint
        if outOfBounds(board,self.row,self.col):
            self.row, self.col = self.checkpoint
        #Check for falling in a hole
        elif board[self.row][self.col] == 'hole':
            print('Fell in a hole. Reset to last checkpoint')
            self.row, self.col = self.checkpoint
        #Update our checkpoint if we landed on a checkpoint
        elif board[self.row][self.col] == 'chek':
            self.checkpoint = (self.row, self.col)
    def getCorners(self):
        #Returns list of points to draw the ship
        points = []
        offset_x = self.col*tile_width + tile_width/2
        offset_y = self.row*tile_height + tile_height/2
        heading = 0
        if self.direction == 0:
            heading = -math.pi/2
        elif self.direction == 2:
            heading = math.pi/2
        elif self.direction == 3:
            heading = math.pi
        #Nose
        angle = heading+math.pi*2
        x = offset_x + math.cos(angle)*self.radius*1.5
        y = offset_y + math.sin(angle)*self.radius*1.5
        points.append([x, y])
        #wing 1
        angle = heading+math.pi*2*(1.2/self.sides)
        x = offset_x + math.cos(angle)*self.radius
        y = offset_y + math.sin(angle)*self.radius
        points.append([x, y])
        #rear
        angle = heading+math.pi
        x = offset_x + math.cos(angle)*self.radius*0.5
        y = offset_y + math.sin(angle)*self.radius*0.5
        points.append([x, y])
        #wing 2
        angle = heading+math.pi*2*(1.8/self.sides)
        x = offset_x + math.cos(angle)*self.radius
        y = offset_y + math.sin(angle)*self.radius
        points.append([x, y])
        return points
    def draw(self):
        #Draw outline of ship.
        points = self.getCorners()
        pygame.draw.polygon(self.screen, self.color,
                            points,int(scaling*8))

class Sprite:
    def __init__(self, surface, x, y, image):
        self.surface = surface
        self.x = x
        self.y = y
        self.image = image
    def draw(self):
        surface.blit(self.image, (self.x, self.y))

def constructMap(filename, surface):
    # Dictionary mapping tileset abbreviations to file names
    image_dict = {'empt': 'tile-clear.png',
                  'hole': 'tile-hole.png',
                  '1wl ': 'tile-wall-1a.png',
                  '1wu ': 'tile-wall-1b.png',
                  '1wr ': 'tile-wall-1c.png',
                  '1wd ': 'tile-wall-1d.png',
                  'chek': 'tile-hammer-wrench.png'}
    # Open file to read in text representation of the map
    file_handle = open(filename, 'r')
    line = file_handle.readline()
    line = line.strip()
    images = []  # 2d array of sprites
    board = []   # 2d array of tile names
    while line:
        array = line.split(',')
        row_array_img = []
        row_array_name = []
        for i in range(len(array)):
            img = pygame.image.load('tiles/'+image_dict[array[i]])
            # Scale image
            img = pygame.transform.scale(img, (tile_width, tile_height))
            row_array_img.append(Sprite(surface, i*tile_width, len(images)*tile_width, img))
            row_array_name.append(array[i])
        images.append(row_array_img)
        board.append(row_array_name)
        line = file_handle.readline()
        line = line.strip()
    return images,board



def drawAll():
    surface.fill((0, 0, 0))  # fill surface with black
    for row in images:
        for col in row:
            col.draw()
    player1.draw()
    player2.draw()
    pygame.display.flip()
    # Delay to get 20 fps
    clock.tick(20)


clock = pygame.time.Clock()
surface = pygame.display.set_mode((map_width, map_height))

#images is a 2d array of images
#board is a 2d array of the names of tiles
images,board = constructMap('maps/map00.txt', surface)

player1 = Robot(surface, 0, 0, white)
player2 = Robot(surface, 4, 3, red)
player_list = [player1, player2]

#Use this list for ordering actions
action_list = []

# Draw all images on the surface
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == 32: #space bar
                #Reset the action list for the next round
                if len(action_list) == 0:
                    #All players decide what they want to do
                    for p in player_list:
                        action_list.append([p, p.update(board)])
                    #Randomize ordering of actions
                    random.shuffle(action_list)
                else:
                    #Take the next action
                    #Perform all actions
                    player, action = action_list.pop()
                    player.doAction(board, player_list, action)
            '''elif event.key == pygame.K_RIGHT:
                player.rotateRight()
            elif event.key == pygame.K_LEFT:
                player.rotateLeft()
            elif event.key == pygame.K_UP:
                player.move(board)'''
    drawAll() #Draw and pause
pygame.quit()
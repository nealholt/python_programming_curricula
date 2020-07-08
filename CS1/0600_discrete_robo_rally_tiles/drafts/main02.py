import pygame, math

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

direction_list = ['north', 'east', 'south', 'west']
class Robot:
    def __init__(self, screen, row, col):
        self.screen = screen
        self.row = row
        self.col = col
        self.sides = 3
        self.radius = 40*scaling
        self.direction = 0
        self.checkpoint = (row,col)
    def rotateLeft(self):
        self.direction -= 1
        if self.direction < 0:
            self.direction = len(direction_list)-1
    def rotateRight(self):
        self.direction = (self.direction+1)%len(direction_list)
    def move(self, board):
        if self.direction == 0: #north
            #Make sure there is no wall up above
            if board[self.row][self.col] != '1wu ':
                self.row -= 1
        elif self.direction == 1: #east
            #Make sure there is no wall right
            if board[self.row][self.col] != '1wr ':
                self.col += 1
        elif self.direction == 2: #south
            #Make sure there is no wall down
            if board[self.row][self.col] != '1wd ':
                self.row += 1
        elif self.direction == 3: #west
            #Make sure there is no wall left
            if board[self.row][self.col] != '1wl ':
                self.col -= 1
        #Check for off the board and reset to a checkpoint
        if self.row<0 or self.col<0 or self.row>=len(board) or self.col>=len(board[0]):
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
        pygame.draw.polygon(self.screen, white, points,int(scaling*8))

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


clock = pygame.time.Clock()
surface = pygame.display.set_mode((map_width, map_height))

images,board = constructMap('maps/map00.txt', surface)

player = Robot(surface, 0, 0)

# Draw all images on the surface
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_RIGHT:
                player.rotateRight()
            elif event.key == pygame.K_LEFT:
                player.rotateLeft()
            elif event.key == pygame.K_UP:
                player.move(board)
    surface.fill((0, 0, 0))  # fill surface with black
    for row in images:
        for col in row:
            col.draw()
    player.draw()
    pygame.display.flip()
    # Delay to get 30 fps
    clock.tick(30)
pygame.quit()
import pygame

pygame.init()

initial_width = 144
initial_height = 144

scaling = 0.25

tile_width = int(initial_width*scaling)
tile_height = int(initial_height*scaling)

board_dimensions = 20
map_width = int(board_dimensions*tile_width)
map_height = int(board_dimensions*tile_height)

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
                  'hole': 'tile-hole.png'}
    # Open file to read in text representation of the map
    file_handle = open(filename, 'r')
    line = file_handle.readline()
    line = line.strip()
    map = []  # 2d array of sprites
    while line:
        array = line.split(',')
        row_array = []
        for i in range(len(array)):
            # skip empty strings
            if array[i].strip() != '':
                img = pygame.image.load('tiles/'+image_dict[array[i]])
                # Scale image
                img = pygame.transform.scale(img, (tile_width, tile_height))
                row_array.append(Sprite(surface, i*tile_width, len(map)*tile_width, img))
            else:
                row_array.append(None)
        map.append(row_array)
        line = file_handle.readline()
        line = line.strip()
    return map


clock = pygame.time.Clock()
surface = pygame.display.set_mode((map_width, map_height))

layers = []
layers.append(constructMap('maps/map00.txt', surface))
#layers.append(constructMap('maps/map01.txt', surface))

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
                pass
            elif event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_UP:
                pass
    surface.fill((0, 0, 0))  # fill surface with black
    for layer in layers:
        for row in layer:
            for col in row:
                if col != None:
                    col.draw()
    pygame.display.flip()
    # Delay to get 30 fps
    clock.tick(30)
pygame.quit()
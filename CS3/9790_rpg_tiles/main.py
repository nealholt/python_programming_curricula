import pygame

pygame.init()

initial_width = 101
initial_height = 171
map_width = int(5*initial_width)
map_height = int(5*initial_height)

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
    image_dict = {'dirt': 'PlanetCutePNG/Dirt Block.png',
                  'tree': 'PlanetCutePNG/Tree Tall.png',
                  'pink': 'PlanetCutePNG/Character Pink Girl.png'}
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
                img = pygame.image.load(image_dict[array[i]])
                # Scale image
                img = pygame.transform.scale(img, (initial_width, initial_height))
                #All of the tiles have invisible space at the top, so use initial_width
                #for both the height and width.
                row_array.append(Sprite(surface, i*initial_width, len(map)*initial_width, img))
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
layers.append(constructMap('maps/map01.txt', surface))

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
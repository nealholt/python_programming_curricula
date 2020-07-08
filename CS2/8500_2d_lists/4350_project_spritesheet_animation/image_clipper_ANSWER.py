import pygame

#Image source: sprite_sheet_test_by_pfunked
#pfunked.deviantart.com/art/Sprite-Sheet-test-80837813

pygame.init()

def strip_from_sheet(sheet, start, size, columns, rows):
    """Strips individual frames from a sprite sheet given
    a start location, sprite size, and number of
    columns and rows."""
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i,
                        start[1]+size[1]*j)
            rect = pygame.Rect(location, size)
            frames.append(sheet.subsurface(rect))
    return frames


clock = pygame.time.Clock()
screen = pygame.display.set_mode((500,600))
screen_rect = screen.get_rect()
done = False
#Image source: dgkidderminster.blogspot.com/p/sprites.html
sheet = pygame.image.load('walksequence_spritesheet.png')
size = sheet.get_size()
dimensions = (240,296)
frames = strip_from_sheet(sheet,
                        (0,0), #start
                        dimensions, #size
                        6, #columns
                        5) #rows


#Scale up the image
scaling = 2
dimensions = (dimensions[0]*scaling,dimensions[1]*scaling)
for i in range(len(frames)):
    frames[i] = pygame.transform.scale(
                            frames[i],
                            dimensions)

image_index = 0

#Draw all images on the screen
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_RIGHT:
                image_index = (image_index+1)%len(frames)
    screen.fill((0,0,0)) #fill screen with black
    screen.blit(frames[image_index], (0,0))
    image_index = (image_index+1)%len(frames)
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()
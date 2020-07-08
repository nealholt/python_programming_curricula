import pygame
pygame.init()

black = (0, 0, 0) #r g b

screen = pygame.display.set_mode((400,400))
clock = pygame.time.Clock()

#Rotation works with all of these image types. It might be interesting to
#see if there is more efficiency with one type compared to another.
image_file = "destroyer.png"
#image_file = "destroyer.gif"
#image_file = "destroyer.jpg"

#Keep the original image around and always rotate from a copy
#of the original. Never rotate from an already rotated image.
#Doing so would degrade the image quality.
original_image = pygame.image.load(image_file)
image = original_image.copy()
rect = original_image.get_rect()
rect.x = 100
rect.y = 100

def rotateImage(image, original_rect, angle):
    '''Rotate an image while keeping its center the same.
    The size of the image's rectangle will change.
    Angle is in degrees.'''
    #Get a rotated image
    rotated_image = pygame.transform.rotate(image, angle)
    #Get the rectangle of the new image
    rotated_rect = rotated_image.get_rect()
    #Set the center of the new rectangle to match the center of the old rectangle
    rotated_rect.center = original_rect.center
    #Return new image and rectangle
    return rotated_image, rotated_rect

angle = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            #Rotate the image by 10 degrees when any button is pushed.
            angle = angle + 10
            image,rect = rotateImage(original_image, rect, angle)
    screen.fill(black)
    screen.blit(image, rect)
    pygame.display.flip()
    #Delay to get 30 fps
    clock.tick(30)
pygame.quit()
import pygame

'''The following code shows how to add transparency to an
image and shows which images can be made transparent.

This example was created using this tutorial
https://www.pygame.org/docs/tut/ChimpLineByLine.html
Line By Line Chimp
Author:	Pete Shinners

https://www.pygame.org/docs/ref/surface.html
Colorkey transparency makes a single color value transparent.
Per pixel alphas are different because they store a transparency value
for every pixel. This allows for the most precise transparency effects,
but it also the slowest. Per pixel alphas cannot be mixed with surface
alpha and colorkeys.
'''
def loadImage(name, colorkey=None):
    #Load the image from file
    try:
        image = pygame.image.load(name)
    except pygame.error:
        print('ERROR: Failed to load image named "'+name+'". Probably a typo.')
        pygame.quit()
        exit()
    #This next line creates a copy that will draw more quickly on the screen.
    image = image.convert()
    #If colorkey is None, then don't worry about transparency
    if colorkey is not None:
        #colorkey of -1 means that the color of upper left most pixel should
        #be used as transparency color.
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        '''The optional flags argument can be set to pygame.RLEACCEL to provide better performance on non accelerated displays. An RLEACCEL Surface will be slower to modify, but quicker to blit as a source.'''
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    #Return the image
    return image


if __name__ == "__main__":
    pygame.init()
    width = 600
    height = 600
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Transparency Example')
    pygame.mouse.set_visible(0) #Invisible mouse!
    black = 0,0,0
    white = 255,255,255
    blue = 0,0,255

    #Load images
    #-1 tells loadImage to use upper left most pixel color as transparent color
    image0 = loadImage('hand.jpg', -1) #Transparency DOES NOT work with jpegs
    image1 = loadImage('ball.png', -1) #Transparency works with pngs
    image2 = loadImage('destroyer.gif', -1)  #Transparency works with gifs
    image3 = loadImage('ball.png')  #No transparency because no -1
    image4 = loadImage('blue_example.png', blue) #Alternate colorkey example
    image5 = loadImage('planet002.png', -1) #Transparency works with previously transparent pixels

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(blue) #paint background blue
        #Draw all the images on the screen.
        screen.blit(image5, (0,0))
        screen.blit(image4, (300,300))
        screen.blit(image3, (100,400))
        screen.blit(image2, (200,200))
        screen.blit(image1, (400,400))
        screen.blit(image0, (0,0))
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
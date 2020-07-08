'''
Neal Holtschulte: I modified crop.py heavily to create a dictionary of
images using pygame.
'''

#!/usr/bin/env python3

import pygame


IMG_PATH = 'images/0x72_DungeonTilesetII_v1.2.png'
TILES_PATH = 'images/tiles_list.txt'


def scaleImage(image, scale_factor):
    #Resize the image
    rectangle = image.get_rect()
    dimensions = (int(rectangle.width*scale_factor), int(rectangle.height*scale_factor))
    return pygame.transform.scale(image, dimensions)



def getBox(arr, frameIndex = 0):
    w, h = int(arr[3]), int(arr[4])
    x, y = int(arr[1]) + w*frameIndex, int(arr[2])
    #print((x, y, w, h))
    return (x, y, w, h)


def load_image(name, colorkey=None):
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
    #Return the image and its rectangle
    return image, image.get_rect()


def getImageDictionary(scale_factor):
    '''Prints out all the keys and returns a dictionary of all the images.'''
    d = {}
    img,_ = load_image(IMG_PATH)
    f = open(TILES_PATH, 'r')
    for line in f.readlines():
        arr = line.split()
        if len(arr) == 0:
            pass # nothing here
        if len(arr) == 5:
            d[arr[0]] = scaleImage(img.subsurface(getBox(arr)), scale_factor)
            print(arr[0])
        if len(arr) == 6:
            numOfFrames = int(arr[5])
            for frameIndex in range(0, numOfFrames):
                title = arr[0] + '_f' + str(frameIndex)
                d[title] = scaleImage(img.subsurface(getBox(arr, frameIndex)), scale_factor)
                print(title)
    f.close()
    return d

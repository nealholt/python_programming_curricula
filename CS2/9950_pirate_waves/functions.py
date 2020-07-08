import pygame, math
from constants import *

def strip_from_sheet():
    '''Strips individual frames from specific sprite sheet.'''
    #Image source: hasgraphics.com/phaedy-explosion-generator/spritesheet3/
    sheet = pygame.image.load('images/spritesheet3-300x300.png')

    r = sheet.get_rect()
    rows = 6
    columns = 6
    img_width = r.w/columns
    img_height = r.h/rows

    frames = []
    for row in range(rows):
        for col in range(columns):
            rect = pygame.Rect(col*img_width, row*img_height, img_width, img_height)
            frames.append(sheet.subsurface(rect))
    return frames

def load_image(name, colorkey=None):
    #Load the image from file
    #try:
    print(':'+name+':')
    image = pygame.image.load(name)
    '''except pygame.error:
        print('ERROR: Failed to load image named "'+name+'". Probably a typo.')
        pygame.quit()
        exit()'''
    #This next line creates a copy that will draw more quickly on the screen.
    #TODO - this next line is corrupting these particular images for some reason.
    #image = image.convert()
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

def getWaterHeightAt(x,water_heights):
    index = 0
    for i in range(len(water_heights)):
        if spacing*i <= x and x <= spacing*(i+1):
            index = i
            break
    adjusted_x = x-spacing*index
    rise = water_heights[index]
    if index+1 < len(water_heights):
        rise = water_heights[index+1]-water_heights[index]
    run = spacing*(i+1)-spacing*i
    slope = rise/run
    return adjusted_x*slope+water_heights[index]

def shiftWaterHeight(mouse_pos, water_heights):
    '''Shift the height of the water at a point to the height
    of the mouse click.'''
    x,y = mouse_pos
    index = 0
    for i in range(len(water_heights)):
        if spacing*i <= x and x <= spacing*(i+1):
            index = i
            break
    water_heights[index] = y

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


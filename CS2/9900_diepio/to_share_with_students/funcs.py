from pygame import Rect
from constants import screen_width_half, screen_height_half

def adjustScreenCoordinates(x,y, povx, povy):
    x += screen_width_half - povx
    y += screen_height_half - povy
    return x,y

def insertInOrder(sprite, sprite_list):
    '''Insert the sprite into sprite_list in order by x
    coordinate. This is important for keeping the all_sprites
    list sorted. Otherwise collisions may be missed.'''
    #This could be more efficient using a binary search since
    #We can assume that sprite_list is sorted.
    if len(sprite_list)==0 or sprite.rect.left <= sprite_list[0].rect.left:
        sprite_list.insert(0, sprite)
        return
    for i in range(len(sprite_list)-1):
        if sprite.rect.left > sprite_list[i].rect.left and \
        sprite.rect.left <= sprite_list[i+1].rect.left:
            sprite_list.insert(i, sprite)
            return
    sprite_list.append(sprite)

def getSpritesInRange(all_sprites, radius, x,y):
    '''Pre: all_sprites is sorted by x coord.
    Post: Returns a sprite list with all the sprites within
    radius distance of x,y'''
    to_return = []
    r_sqd = radius**2
    for a in all_sprites:
        if (a.x-x)**2+(a.y-y)**2 < r_sqd:
            to_return.append(a)
        elif a.x > x+radius:
            break
    return to_return

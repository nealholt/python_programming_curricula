from pygame import Rect

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
    Post: Returns a sprite list with all the sprites within a square
    radius of x,y'''
    r = Rect(x-radius, y-radius, radius*2, radius*2)
    to_return = []
    for a in all_sprites:
        if a.rect.colliderect(r):
            to_return.append(a)
        elif a.rect.x > r.right:
            break
    return to_return

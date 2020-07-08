import pygame, sprite

def clickerCookieAmount(level):
    '''Return the amount of cookies gained per click.'''
    return max(1, int((100*level**1.05)/100))

pygame.init()

black = 0,0,0
white = 255,255,255

width = 800
height = 600
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

cookie = sprite.Sprite('Cookie', #name
                    (width-250)/2, #x. Note 250 is the image width
                    0, #y
                    'CookieIcon.png', #image file
                    screen)

cursor = sprite.Sprite('Clicker', #name
                    10, #x
                    cookie.rect.height+50, #y
                    'CursorIcon.png', #image file
                    screen)

mine = sprite.Sprite('Mine', #name
                    width/3, #x
                    cookie.rect.height+50, #y
                    'MineIcon.png', #image file
                    screen)

farm = sprite.Sprite('Farm', #name
                    2*width/3, #x
                    cookie.rect.height+50, #y
                    'FarmIcon.png', #image file
                    screen)

#Draw all images on the screen
done = False
while not done:
    #Increase cookies based on mine and farm level
    cookie.level = cookie.level + mine.level*1.03**mine.level
    cookie.level = cookie.level + (100*1.03**mine.level)/100

    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #clicked on a cookie
            if cookie.rect.collidepoint(pos):
                cookie.level = cookie.level + clickerCookieAmount(cursor.level)
            #clicked on cursor level up
            elif cursor.rect.collidepoint(pos):
                if cookie.level >= cursor.level_up_function(cursor.level):
                    cookie.level = cookie.level-cursor.level_up_function(cursor.level)
                    cursor.level = cursor.level + 1
            #clicked on mine level up
            elif mine.rect.collidepoint(pos):
                if cookie.level >= mine.level_up_function(mine.level):
                    cookie.level = cookie.level-mine.level_up_function(mine.level)
                    mine.level = mine.level + 1
            #clicked on farm level up
            elif farm.rect.collidepoint(pos):
                if cookie.level >= farm.level_up_function(farm.level):
                    cookie.level = cookie.level-farm.level_up_function(farm.level)
                    farm.level = farm.level + 1
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True

    screen.fill(black) #fill screen

    cookie.draw()
    cursor.draw()
    mine.draw()
    farm.draw()

    pygame.display.flip()
    #Delay to get 60 fps
    clock.tick(60)
pygame.quit()


'''
weapon_knife
weapon_rusty_sword
weapon_regular_sword
weapon_red_gem_sword
weapon_big_hammer
weapon_hammer
weapon_baton_with_spikes
weapon_mace
weapon_katana
weapon_saw_sword
weapon_anime_sword
weapon_axe
weapon_machete
weapon_cleaver
weapon_duel_sword
weapon_knight_sword
weapon_golden_sword
weapon_lavish_sword
weapon_red_magic_staff
weapon_green_magic_staff
'''

import pygame, image_loader, sprite, math

pygame.init()


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


screen = pygame.display.set_mode((500,300))
clock = pygame.time.Clock()
fps = 30

#Original dimensions of each square image
original_size = 16

#Dictionary of images
scale_factor = 3 #3x larger
images = image_loader.getImageDictionary(scale_factor)

#Scaled size of each square image
size = original_size*scale_factor


y = 100

sword = sprite.Sprite(screen, 100, y, images['weapon_regular_sword'])

knight = sprite.Sprite(screen, 80, y, images['knight_m_idle_anim_f0'])

sequence=[0,1,2,3,4,5,6,5,4,3,2,1]
angle_sequence = []
height_sequence = [0,3,8,12,16,32,40,32,16,12,8,3]
for i in sequence:
    angle_sequence.append(-(i/5)*90)
    #height_sequence.append(i/4)

index = 0

done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill((255,255,255)) #fill the screen with black. Erase previous images

    knight.draw()
    sword.draw()

    index = (index+1)%len(angle_sequence)
    sword.image, sword.rect = rotateImage(images['weapon_regular_sword'], images['weapon_regular_sword'].get_rect(), angle_sequence[index])
    sword.y = y+height_sequence[index]+8


    pygame.display.flip()
    #Delay to get desired frames per second
    clock.tick(fps)

pygame.quit()
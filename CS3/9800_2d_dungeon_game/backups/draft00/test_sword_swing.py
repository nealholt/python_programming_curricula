import pygame, image_loader

pygame.init()




#Dwell on each image for this many frames.
dwell_reset = 5

class AnimatedSprite:
    def __init__(self, screen, x, y, frames):
        self.screen = screen
        self.x = x
        self.y = y
        self.index = 0
        self.dwell = dwell_reset
        self.frames = frames
        self.rect = self.frames[self.index].get_rect()

    def advanceImage(self):
        self.dwell -= 1
        if self.dwell < 0:
            self.index = (self.index+1)%len(self.frames)
            self.dwell = dwell_reset

    def draw(self):
        screen.blit(self.frames[self.index],
                     ( int(self.x-self.rect.width/2),
                       int(self.y-self.rect.height/2) ))


screen = pygame.display.set_mode((500,200))
clock = pygame.time.Clock()
fps = 60

#Dictionary of images
scale_factor = 4 #4x larger
images = image_loader.getImageDictionary(scale_factor)

w_idle = 'wizzard_m_idle_anim_f'
w_idle_num = 4
frames = []
for i in range(w_idle_num):
    frames.append(images[w_idle+str(i)])
sprite_idle = AnimatedSprite(screen, 100, 50, frames)


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

w_run = 'wizzart_m_run_anim_f'
w_run_num = 4
frames = []
for i in range(w_run_num):
    frames.append(images[w_run+str(i)])
sprite_run = AnimatedSprite(screen, 250, 50, frames)

done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill((0,0,0)) #fill the screen with black. Erase previous images

    sprite_idle.draw()
    sprite_idle.advanceImage()

    sprite_run.draw()
    sprite_run.advanceImage()

    pygame.display.flip()
    #Delay to get desired frames per second
    clock.tick(fps)

pygame.quit()
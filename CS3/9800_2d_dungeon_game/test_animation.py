import pygame, image_loader, sprite

pygame.init()

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
sprite_idle = sprite.AnimatedSprite(screen, 100, 50, frames, 5)

w_run = 'wizzart_m_run_anim_f'
w_run_num = 4
frames = []
for i in range(w_run_num):
    frames.append(images[w_run+str(i)])
sprite_run = sprite.AnimatedSprite(screen, 250, 50, frames,5)

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
#Source of this code: stackoverflow.com/questions/17935484/mouseover-in-pygame
import pygame
from pygame.locals import *
import time, sys

if __name__ == "__main__":
    pygame.init()
    size = (700, 700)
    screen = pygame.display.set_mode(size)
    font = pygame.font.SysFont('Impact',20,16)

    title = font.render(('SQUASH!'), True, (255,255,255))
    title_r = title.get_rect()
    title_r.x, title_r.y = 400,400

    play = font.render(('PLAY'), True, (255,255,255))
    play_r = play.get_rect() #Get the rectangle of the image or text.
    play_r.x, play_r.y = 300,300

    # always use a Clock to keep your framerate constant
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((0,0,0,))
        screen.blit(title, (title_r.x, title_r.y))
        screen.blit(play, (play_r.x, play_r.y))

        pos = pygame.mouse.get_pos()
        #Print "Detected" if the rectangle around the text contains the mouse position
        if play_r.collidepoint(pos):
            print('Detected Play')
        if title_r.collidepoint(pos):
            print('Detected Squash')
        # Neal added this:
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)
        #Neal's note: I wonder about the relative merits of clock.tick versus time.sleep
        time.sleep(0.000000000000000000000000000000000000000000000000000000001)
        pygame.display.flip()
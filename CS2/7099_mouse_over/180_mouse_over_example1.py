#Source of this code: stackoverflow.com/questions/17935484/mouseover-in-pygame
import pygame

pygame.init()
screen = pygame.display.set_mode((200, 200))

# the 'normal' font
base_font = pygame.font.SysFont('Arial', 20, 16)

# the 'mouse-over' font
mod_font  = pygame.font.SysFont('Arial', 20, 16)
mod_font.set_underline(True)

# always use some kind of cache when rendering font
# font rendering is very expensive, and it *will*
# slow down your application if you render some text
cache = {}
def render(text, mod=False):
    if not mod in cache:
        cache[mod] = {}
    if not text in cache[mod]:
        cache[mod][text] = (mod_font if mod else base_font).render(text, True, (255, 255, 255))
    return cache[mod][text]

# create a list of (text, Rect)-tuples
x, y = 10, 20
objects = [(t, render(t).get_rect()) for t in ('Hi', 'please', 'click', 'me')]

# just move some objects around
for (_, r) in objects:
    r.top, r.left = y, x
    x *= 2
    y += 35

# always use a Clock to keep your framerate constant
clock = pygame.time.Clock()

run = True
while run:
    # clear the screen
    screen.fill((0, 0, 0))

    # draw all objects
    for (t, r) in objects:
        # decide if we want to render the text with or without the underline
        # based on the result of collidepoint(pygame.mouse.get_pos())
        # note that collidepoint is a method of Rect, not Surface
        screen.blit(render(t, r.collidepoint(pygame.mouse.get_pos())), r)

    # check which item is clicked
    if pygame.event.get(pygame.MOUSEBUTTONDOWN):
        # calling 'render' over and over again is cheap now, since the result is cached
        for text in [t for (t, r) in objects if r.collidepoint(pygame.mouse.get_pos())]:
            print("'{}' was clicked".format(text))

    # draw the screen ONCE
    pygame.display.flip()
    if pygame.event.get(pygame.QUIT): run = False
    # clear all unwanted events
    pygame.event.clear()
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(10)
pygame.quit()
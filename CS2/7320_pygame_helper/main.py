'''
For 45 points, answer the following questions about main.py and
sprite.py.

1. Use the arrow keys to move the hand. How does the movement
change when is code is commented out?
    #Reset movement
    hand.dx = 0
    hand.dy = 0

Uncomment the code from the previous question before continuing.

2. What line of code needs changed if I want to double the hand's
speed and what does the new code look like?

3. List the names of the functions (aka methods) that belong to
Sprite.

4. List the names of the variables (aka attributes) that belong to
Sprite.

5. Which is passed to Sprite's constructor, an image or the file
name where an image can be found?

6. What error do you get if instead of using the image file
"hand.png"you accidentally write "hand.pig"?

7. What error do you get if you try to load "hand.png" but that
image is in a different folder?

8. What are the default x and y values of a rectangle that you get
from an image? (Hint: to find out, print out rect.x and rect.y
in the getRect method in sprite BEFORE setting these values.

9. Change the code so that instead of setting dx and dy equal to a
number when you press the arrow keys, pressing the arrow keys adds
or subtracts one (depending on the direction) from dx and dy.
Show me the modified code as an answer to this question.

10. Describe the new movement controls after you make the changes
in question 9.

11. If you comment out these two lines of code
        rect.x = int(self.x)
        rect.y = int(self.y)
from the getRect method in sprite, what happens to the
coin and WHY?

'''
import pygame, sprite, random
pygame.init()

def checkForQuit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit(); exit()

width = 1000
height = 600
black = (0, 0, 0) #r g b
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

hand = sprite.Sprite(0,0,"hand.png")
coin = sprite.Sprite(0,0,"coin.png")
speed = 4

while True:
    checkForQuit()

    #Reset movement
    hand.dx = 0
    hand.dy = 0
    #Respond to keypress
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        hand.dy = -speed
    if keys[pygame.K_DOWN]:
        hand.dy = speed
    if keys[pygame.K_LEFT]:
        hand.dx = -speed
    if keys[pygame.K_RIGHT]:
        hand.dx = speed

    #move
    hand.move()

    #Check for collision and reposition coin
    if hand.collided(coin):
        x = random.randint(0, width-100)
        y = random.randint(0, height-100)
        coin.x = x
        coin.y = y

    #Draw everything
    screen.fill(black)
    hand.draw(screen)
    coin.draw(screen)
    pygame.display.flip()
    #Delay to get 60 fps
    clock.tick(60)
pygame.quit()
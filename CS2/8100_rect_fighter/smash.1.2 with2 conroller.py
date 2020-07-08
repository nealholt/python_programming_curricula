#-------------------------------------------------------------------------------
# Name:
# Purpose:
#
# Author:      Connor Gardiner
#
# Created:     27/11/2018
# Copyright:   (c) 2018
#-------------------------------------------------------------------------------
'''
Additions:
    Damaging bullets fly in from both sides of the screen.
    More bullets spawn as time goes onward.
    After a certain amount of time crouching is disabled.
    Draw an x briefly when a hit lands.
'''
import pygame
import math
import random
import time
pygame.init()
class Stage():
    def __init__(self):
         self.surface = surface
         self.color = green
         self.rect = pygame.Rect(50,650,900,50)
         self.terrain=[]
         self.previousx=100
         self.previousy=300
    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)
        for i in range(len(self.terrain)):
            pygame.draw.rect(self.surface,self.color,self.terrain[i])


class Player():
    def __init__(self,x,color):
        self.surface=surface
        self.rect=pygame.Rect(x,570,20,80)
        self.color=color
        self.jumped= False
        self.speedy=20
        self.grav=1
        self.fist=pygame.Rect(self.rect.x,self.rect.y+20,20,10)
        self.punchdir=False
        self.pduration=0
        self.punched=False
        self.health=100
        self.healthbar= pygame.Rect(x,50,self.health,20)
    #draws player
    def draw(self,x):
        #update health bar
        self.healthbar= pygame.Rect(x,50,self.health,20)
        #draw
        pygame.draw.rect(self.surface,self.color,self.rect)
        pygame.draw.rect(self.surface,self.color,self.fist)
        if self.health>0:
            pygame.draw.rect(self.surface,self.color,self.healthbar)
    #realistic jumping
    def jump(self):
        self.rect.y-=self.speedy
        self.speedy-=self.grav
    # checks to see if player landed
    def onfloor(self,background):
        if self.rect.colliderect(background.rect):
            print('collided')
            self.rect.y=background.rect.y-(self.rect.height-1)
            self.speedy=0
            return False
        else:
            return True
    #update fist
    def updatef(self):
        self.fist.x=self.rect.x
        self.fist.y=self.rect.y+20
        self.pduration=0
        self.punched= False
    #punch
    def punch(self):
        if self.punchdir:
            self.fist.x+=15
        else:
            self.fist.x-=10
    #did the punch land
    def planded(self,rect,p):
        if self.fist.colliderect(rect):
            p.health-=2
            if p.health<=0:
                rect.y+=500
    #crouch
    def crouch(self):
        self.rect=pygame.Rect(self.rect.x,self.rect.y,20,40)
    #uncrouch
    def uncrouch(self):
        self.rect=pygame.Rect(self.rect.x,self.rect.y,20,80)
#initialize variables
clock = pygame.time.Clock()
surface = pygame.display.set_mode((1000,800))
pygame.display.set_caption('smash box')
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0
brown =218,165,32

#saving objects as variables
background= Stage()
leftp=Player(200,red)
rightp=Player(700,blue)
#setup controller
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
num_buttons = joystick.get_numbuttons()
joystick2= pygame.joystick.Joystick(1)
joystick2.init()
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            #CONTROLLER CODE
        elif event.type == pygame.JOYBUTTONDOWN:
            if joystick.get_button(3):
                if rightp.rect.height>50:
                    rightp.punched=True
            elif joystick.get_button(1):
                if rightp.rect.colliderect(background.rect):
                    rightp.speedy=30
                rightp.jumped=True
                rightp.jump()
            elif joystick.get_button(4):
                rightp.punchdir=False
            elif joystick.get_button(5):
                rightp.punchdir=True
            if joystick2.get_button(3):
                if leftp.rect.height>50:
                    leftp.punched=True
            elif joystick2.get_button(1):
                if leftp.rect.colliderect(background.rect):
                    leftp.speedy=30
                leftp.jumped=True
                leftp.jump()
            elif joystick2.get_button(4):
                leftp.punchdir=False
            elif joystick2.get_button(5):
                leftp.punchdir=True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            #up key makes player jump
            elif event.key==pygame.K_UP:
               if rightp.rect.colliderect(background.rect):
                    rightp.speedy=25
               rightp.jumped=True
               rightp.jump()
            elif event.key==pygame.K_w:
                if leftp.rect.colliderect(background.rect):
                    leftp.speedy=25
                leftp.jumped=True
                leftp.jump()
            # punch button
            elif event.key==pygame.K_RSHIFT:
                rightp.punched=True
            elif event.key==pygame.K_LSHIFT:
                leftp.punched=True
    #controller movement
    x_motion = round(joystick.get_axis(0))
    y_motion = round(joystick.get_axis(1))
    if y_motion>0:
        rightp.crouch()
    else:
        rightp.uncrouch()
    rightp.rect.x+= x_motion * 7
    x_motion2 = round(joystick2.get_axis(0))
    y_motion2 = round(joystick2.get_axis(1))
    if y_motion2>0:
        leftp.crouch()
    else:
        leftp.uncrouch()
    leftp.rect.x+= x_motion2 * 7
    #players directional movement
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        rightp.punchdir=False
        rightp.rect.x-=10
    if pressed[pygame.K_RIGHT]:
        rightp.punchdir=True
        rightp.rect.x+=10
    if pressed[pygame.K_a]:
        leftp.punchdir=False
        leftp.rect.x-=10
    if pressed[pygame.K_d]:
        leftp.punchdir=True
        leftp.rect.x+=10
    #crouch
    if pressed[pygame.K_DOWN]:
       rightp.crouch()
    #else:
      # rightp.uncrouch()
    if pressed[pygame.K_s]:
        leftp.crouch()
   # else:
       # leftp.uncrouch()

    #jump
    if rightp.onfloor(background)==False:
        rightp.jumped=False
    else:
        rightp.jump()
    if leftp.onfloor(background)==False:
        leftp.jumped=False
    else:
        leftp.jump()
    #punch
    if rightp.punched and rightp.pduration<5:
       rightp.punch()
       rightp.pduration+=1
       rightp.planded(leftp.rect,leftp)
    else:
        rightp.updatef()
    if leftp.punched and leftp.pduration<5:
       leftp.punch()
       leftp.pduration+=1
       leftp.planded(rightp.rect,rightp)
    else:
        leftp.updatef()
    #drawing block
    surface.fill((245,245,245)) #fill surface with black
    background.draw()
    leftp.draw(150)
    rightp.draw(700)
    pygame.display.flip()
    pygame.display.update()
	#Delay to get 60 fps
    clock.tick(60)
print("Game Over")
pygame.quit()
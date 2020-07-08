import pygame, random

pygame.init()
font = pygame.font.SysFont('Arial', int(30))
gain_loss = pygame.font.SysFont('freesansbold', int(48))
blue = 0,0,255
green = 0,255,0
red = 255,0,0
orange = 255,120,0

directions = ['north','east','south','west']

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


class Critter:
    def __init__(self, screen, row, col, image, team, name):
        #Create a Sprite object
        self.screen = screen
        self.row = row
        self.col = col
        self.image = image
        self.original_image = self.image
        self.team = team
        self.name = name
        self.energy = 20
        self.fatigue = 0
        #Face a random direction
        self.direction_index = random.randint(0,3)
        self.updateImage()
        self.recent_action = ''
        self.energy_change = 0
        self.damage_taken = 0
    def draw(self, size):
        #r = self.image.get_rect()
        pos = (int(size*self.col), int(size*self.row))
        self.screen.blit(self.image, pos)
        #Draw most recent action
        text_pos = (pos[0]+int(size/6),pos[1]+int(size/2))
        text = font.render(self.recent_action,True,blue)
        self.screen.blit(text, text_pos)
        #Draw change in energy if any
        if self.energy_change != 0:
            text_pos = (pos[0]+int(size/6),pos[1])
            color = orange
            symbol = ''
            if self.energy_change > 0:
                color = green
                symbol = '+'
            text = gain_loss.render(symbol+str(self.energy_change),True,color)
            self.screen.blit(text, text_pos)
        #Draw damage taken from attack
        if self.damage_taken != 0:
            text_pos = (pos[0]+int(size/6),pos[1]+int(size/2))
            text = gain_loss.render(str(self.damage_taken),True,red)
            self.screen.blit(text, text_pos)
        #Draw death if dead
        if self.energy <= 0:
            start_pos = pos
            end_pos = (pos[0]+size,pos[1]+size)
            pygame.draw.line(self.screen, (0,0,0), start_pos, end_pos, 10)
    def takeAction(self, board, critter_cells):
        '''TODO: Students write code here.
        Each creature only takes one action per turn.

        Fatigue is reset by the rest action.

        Here are some other useful functions:
        energyHere(self, board)
        getCritterAhead(self, critter_cells)
        aheadInBounds(self, critter_cells)
        '''
        return 'rest'
    def energyHere(self, board):
        #Get how much energy is at current location
        return board[self.row][self.col].energy
    def eat(self, board):
        if self.energy<=0:
            return
        self.energy -= self.fatigue; self.energy_change = -self.fatigue; self.fatigue += 1 #use energy. get tired
        self.energy += board[self.row][self.col].energy
        self.energy_change += board[self.row][self.col].energy
        board[self.row][self.col].energy = 0
    def turnRight(self):
        if self.energy<=0:
            return
        self.energy -= self.fatigue; self.energy_change = -self.fatigue; self.fatigue += 1 #use energy. get tired
        self.direction_index = (self.direction_index+1)%len(directions)
        self.updateImage()
    def turnLeft(self):
        if self.energy<=0:
            return
        self.energy -= self.fatigue; self.energy_change = -self.fatigue; self.fatigue += 1 #use energy. get tired
        self.direction_index -= 1
        if self.direction_index < 0:
            self.direction_index = len(directions)-1
        self.updateImage()
    def updateImage(self):
        if directions[self.direction_index] == 'west':
            self.image = pygame.transform.flip(self.original_image, True, False)
        elif directions[self.direction_index] == 'east':
            self.image = self.original_image
        elif directions[self.direction_index] == 'north':
            self.image, _ = rotateImage(self.original_image, self.original_image.get_rect(), 90)
        elif directions[self.direction_index] == 'south':
            self.image, _ = rotateImage(self.original_image, self.original_image.get_rect(), -90)
    def getCritterAhead(self, critter_cells):
        if not self.aheadInBounds(critter_cells):
            return None
        elif directions[self.direction_index]=='north':
            return critter_cells[self.row-1][self.col]
        elif directions[self.direction_index]=='south':
            return critter_cells[self.row+1][self.col]
        elif directions[self.direction_index]=='east':
            return critter_cells[self.row][self.col+1]
        elif directions[self.direction_index]=='west':
            return critter_cells[self.row][self.col-1]
    def aheadInBounds(self, critter_cells):
        if directions[self.direction_index]=='north':
            return self.row>0
        elif directions[self.direction_index]=='south':
            return self.row<len(critter_cells)-1
        elif directions[self.direction_index]=='east':
            return self.col<len(critter_cells[0])-1
        elif directions[self.direction_index]=='west':
            return self.col>0
    def move(self, critter_cells):
        if self.energy<=0 or not self.aheadInBounds(critter_cells):
            return
        elif self.getCritterAhead(critter_cells) != None:
            return
        self.energy -= self.fatigue; self.energy_change = -self.fatigue; self.fatigue += 1 #use energy. get tired
        if directions[self.direction_index]=='north':
            critter_cells[self.row-1][self.col] = critter_cells[self.row][self.col]
            critter_cells[self.row][self.col] = None
            self.row -= 1
        elif directions[self.direction_index]=='south':
            critter_cells[self.row+1][self.col] = critter_cells[self.row][self.col]
            critter_cells[self.row][self.col] = None
            self.row += 1
        elif directions[self.direction_index]=='east':
            critter_cells[self.row][self.col+1] = critter_cells[self.row][self.col]
            critter_cells[self.row][self.col] = None
            self.col += 1
        elif directions[self.direction_index]=='west':
            critter_cells[self.row][self.col-1] = critter_cells[self.row][self.col]
            critter_cells[self.row][self.col] = None
            self.col -= 1
    def customReproduce(self, critter_cells, new_child):
        '''Pass in the new child so that each class
        (Critter, CritterAI1, and CritterAI2) can all
        produce a child of their same type.'''
        if self.energy <= 0 or not self.aheadInBounds(critter_cells):
            return
        elif self.getCritterAhead(critter_cells) != None:
            return
        self.energy -= self.fatigue; self.energy_change = -self.fatigue; self.fatigue += 1 #use energy. get tired
        #Lose half of own energy
        self.energy = int(self.energy/2)
        #Create new creature in adjacent cell with half my energy
        row = self.row
        col = self.col
        if directions[self.direction_index]=='north':
            row = self.row-1
        elif directions[self.direction_index]=='south':
            row = self.row+1
        elif directions[self.direction_index]=='east':
            col = self.col+1
        elif directions[self.direction_index]=='west':
            col = self.col-1
        new_child.row = row
        new_child.col = col
        critter_cells[row][col] = new_child
    def reproduce(self, critter_cells):
        new_child = Critter(self.screen, self.row, self.col, self.original_image, self.team, self.name)
        self.customReproduce(critter_cells, new_child)
    def attack(self, critter_cells):
        c = self.getCritterAhead(critter_cells)
        if self.energy > 0 and c!= None:
            self.energy -= self.fatigue; self.energy_change = -self.fatigue; self.fatigue += 1 #use energy. get tired
            #Attack deals 8 damage
            c.energy -= 8
            c.damage_taken = -8
    def rest(self):
        #Resting consumes one energy
        self.energy -= 1; self.energy_change = -1
        #Fatigue is reset to 1 not zero
        self.fatigue = 1
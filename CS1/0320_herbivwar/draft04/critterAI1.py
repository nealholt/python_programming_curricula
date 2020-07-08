import random, critter

class CritterAI1(critter.Critter):
    def __init__(self, screen, row, col, image, team, name):
        super().__init__(screen, row, col, image, team, name)

    def reproduce(self, critter_cells):
        '''You have to have this in each critter child
        class so that CritterAIs can reproduce with the
        same AI and not with a generic critter that
        happens to share the same image!'''
        new_child = CritterAI1(self.screen, self.row, self.col, self.original_image, self.team, self.name)
        self.customReproduce(critter_cells, new_child)

    def takeAction(self, board, critter_cells):
        '''TODO: Students write code here.

        Each creature only takes one action per turn.
        The action is the value returned, one of:
        'reproduce', 'eat', 'attack', 'left',
        'right', 'move', 'rest'

        Fatigue is the amount of energy consumed by
        each action.

        #how much fatigue do I have?
        print(self.fatigue)
        print("losing "+str(self.fatigue)+" energy this turn")

        #If fatigue is too high, reset fatigue to zero
        if self.fatigue > 4:
            return 'rest'

        The eat action consumes all the energy at the
        current location.

        #If there is lots of energy here, then eat.
        if self.energyHere(board) > 10:
            return 'eat'

        #Eat if I am low on energy
        if self.energy < 3:
            return 'eat'

        #Don't walk out of bounds
        if self.aheadInBounds(critter_cells):
            return 'move'
        else:
            return 'right'

        #Check to make sure ahead is inbounds and
        #not blocked by another creature before
        #reproducing.
        if self.aheadInBounds(critter_cells) and self.getCritterAhead(critter_cells)==None:
            return 'reproduce'

        #If there is an enemy ahead, attack them.
        other_critter = self.getCritterAhead(critter_cells)
        if other_critter != None and other_critter.team != self.team:
            return 'attack'

        #Choose one of three random actions
        r = random.randint(0,2)
        if r==0:
            return 'left'
        elif r==1:
            return 'right'
        else:
            return 'rest'
        '''
        #reproduce
        if self.energy > 4:
            if self.aheadInBounds(critter_cells) and self.getCritterAhead(critter_cells)==None:
                return 'reproduce'
        #rest
        if self.fatigue > 1:
            return 'rest'
        #eat
        if self.energyHere(board) > 4:
            return 'eat'
        #fight
        other = self.getCritterAhead(critter_cells)
        if other!=None and other.team!=self.team:
            return 'attack'
        #Otherwise random
        r = random.randint(0,2)
        if r==0:
            return 'left'
        elif r==1:
            return 'right'
        else:
            return 'rest'

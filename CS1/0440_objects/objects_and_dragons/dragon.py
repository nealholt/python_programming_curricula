
class Dragon:
    def __init__(self):
        '''Create a dragon with 3 health points.'''
        self.hp = 3

    def isDead(self):
        '''Return True if the dragon is dead.'''
        return self.hp <= 0

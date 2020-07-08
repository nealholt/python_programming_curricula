import random, robot
from functions import *

'''
The idea is to write a basic robot that's a little easier
for students to write. This was my experiment using some new
functions to make that possible.
'''
class EasierTestBot(robot.Robot):
    def __init__(self, screen, color,name):
        super().__init__(screen, color,name)

    def chooseAction(self, board, players, flags):
        current_flag = self.getNextFlag(flags)
        if self.hasPreselectedAction():
            print('Next in sequence: '+self.action_sequence[0])
            self.next_action = self.getPreselectedAction()
        elif self.wallAhead(board):
            print('Wall ahead')
            self.next_action = random.choice(['left','right'])
            self.addNextAction('move')
        elif self.holeAhead(board):
            print('hole ahead')
            self.next_action = random.choice(['left','right'])
            self.addNextAction('move')
        elif self.flagAhead(current_flag):
            print('move forward')
            self.next_action = 'move'
        elif self.flagLeft(current_flag):
            print('flag left')
            self.next_action = 'left'
        elif self.flagRight(current_flag):
            print('flag right')
            self.next_action = 'right'
        elif self.flagBehind(current_flag):
            print('flag behind')
            self.next_action = 'right'
            self.addNextAction('right')
        else:
            print('ERROR in robot_easier')
            self.next_action = 'wait'
        return self.next_action

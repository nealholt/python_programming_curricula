import robot
from constants import *

class Waitbot(robot.Robot): #It just waits
    def __init__(self, screen, color,name):
        super().__init__(screen, color,name)
    def chooseAction(self, board, players, flags):
        #Override parent class which chooses action randomly
        self.next_action = 'wait'
        return self.next_action


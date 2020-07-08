#Import random code and robot code
import random, robot
#Also import some useful function
from functions import *

#Define a new object named StudentBot. StudentBot is a child
#of robot.Robot which means that StudentBot borrows all of
#robot.Robot's code.
class StudentBot(robot.Robot):
    #__init__ is the constructor for StudentBot. __init__ tells
    #Python how it can create a StudentBot. Try not to worry
    #about it too much.
    def __init__(self, screen, color, name):
        super().__init__(screen, color,name)

    #This is an important function. Each time the robot needs
    #to decide what to do next, this function is called.
    #This function gets access to the game board, any other
    #players, and the flags the robot wants to collect.
    def chooseAction(self, board, players, flags):
        self.next_action = 'move'
        #This function must end with this line of code, which
        #tells the game what action this robot chose during its
        #turn
        return self.next_action

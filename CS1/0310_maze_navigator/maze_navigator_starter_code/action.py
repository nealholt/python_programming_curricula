from main import *


maze_file = 'mazes/trial03.txt'
fps = 4 #Frames per second


def goToGoal(runner, maze, goal_row, goal_col):
    '''Use the following functions to get the Maze Runner to the goal.

    runner.moveAhead(maze)

    runner.turnLeft()

    runner.turnRight()

    runner.setHeading(north) #or south, east, west

    #This function returns true if there is a wall ahead.
    runner.wallAhead(maze)

    #Returns the manhattan distance from the runner to the goal.
    runner.distanceToGoal(goal_row, goal_col)

    You should also consider using if statements to check which direction
    you need to move. For instance:
    #Check if the goal is to the north. If so, head that direction.
    if goal_row < runner.row:
        runner.setHeading(north)

    ADVANCED: The maze runner also has a limited amount of memory. If you
    need the runner to remember something you can put the information in
    one of the following variables like so:
    runner.memory0 = False
    runner.memory1 = "Been here before"
    up to
    runner.memory9
    This is not necessary, but may be useful on mazes 7 and 8, which are
    very challenging.

    There is also a built in list object that can be used.
    	runner.memorylist.append( (runner.col,runner.row) )
    '''
    pass #TODO Write your code here.







main(maze_file,fps,goToGoal)
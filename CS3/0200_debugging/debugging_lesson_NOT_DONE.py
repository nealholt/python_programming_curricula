'''
Debugging lesson

TODO - a whole set of programs based on color match?

Tic tac toe debugging and sanity checking.

circles and rects move top to bottom
circles and rects move right to left
when two circles collide they are both destroyed
when two rects collide they reverse direction
when anything leaves the screen it is deleted
Bugs: things leaving the screen are not deleted (multiple errors: 1. they are not drawn too early, before leaving the screen, the borders of the screen are wrong (flickering off some edges but not others), and at least one of the conditions is reversed.
when a circle and a rect collide they are destroyed
when two rects collide one does not reverse direction
there is a divide by zero error that occurs only when two rects collide
Use a function that returns a value, but the value isn't used. There is a function to create new rects and one to create new circles, both return something. Only one is used.

Lesson on debugging with print

First steps students shoud take: reduce randomness, create test cases,
shrink in size, and possibly slow things down.

Make error examples

does the code run?
	-malformed if
	-malformed or duplicate function call

are the values as expected?
	-incorrect calculation
	-forget return statement

use error of
-return in a loop or if-else with returns in a loop
-no return in one function case
-wrong sign < vs > in an if
-wrong parentheses in a calcuation
-accidentally indented an if inside another if (could use pygame keyboard input to debug this)

'''
import pygame, math

pygame.init()

clock = pygame.time.Clock()
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
surface = pygame.display.set_mode((1000,600))

offsetx=50
offsety=50
cell_size = 40
row_count = 12
col_count = 8

class Grid:
    def __init__(self):
        #Create a 2d grid of cells
        self.cells = []
        for i in range(row_count):
            temp = []
            for j in range(col_count):
                x = offsetx+cell_size*j+j
                y = offsety+cell_size*i+i
                c = Cell(surface,x,y, cell_size)
                temp.append(c)
            self.cells.append(temp)
    def draw(self):
        for row in self.cells:
            for col in row:
                col.draw()
    def clear(self):
        for row in self.cells:
            for col in row:
                col.color = blue
    def cellIsEmpty(self,row,col):
        print('checking',row,col) #TODO
        return self.cells[row][col].color == blue
    def cellsAreEmpty(self,row,col,adjustments):
        print() #TODO
        for a in adjustments:
            if not self.cellIsEmpty(row+a[1],col+a[0]):
                return False
        return True


class Cell:
    def __init__(self, surface, x, y, size):
        self.surface = surface
        self.rect = pygame.Rect(x,y,size,size)
        self.color = blue
    def draw(self):
        pygame.draw.rect(self.surface,self.color,self.rect)



class Piece:
    def __init__(self, surface, row, col, color):
        self.surface = surface
        #List of offsets from the given row and col
        self.orientations = [[(0,0),(0,-1),(0,-2),(1,0)], #L
                             [(-1,0),(-1,-1),(0,-1),(1,-1)], #backwards 7
                             [(0,0),(0,-1),(0,-2),(-1,-2)], #7
                             [(0,0),(1,-1),(1,0),(-1,0)] #backwards L
                            ]
        self.orient_index = 0
        #TODO TESTING DELETE START
        if color == red:
            self.orient_index = 2
        #TODO TESTING DELETE END
        self.color = color
        self.row = row
        self.col = col
    def colorInGrid(self, grid):
        for c in self.orientations[self.orient_index]:
            grid.cells[self.row+c[1]][self.col+c[0]].color = self.color
    def rotate(self, grid):
        #Set all your cells to blue to indicate empty
        for c in self.orientations[self.orient_index]:
            grid.cells[self.row+c[1]][self.col+c[0]].color = blue
        #Only rotate if the cells you are rotating into are clear
        temp_index = (self.orient_index+1) % len(self.orientations)
        if grid.cellsAreEmpty(self.row,self.col,self.orientations[temp_index]):
            self.orient_index = temp_index

board = Grid()

pieces = []

row = 4
col = 2
pieces.append(Piece(surface, row, col, red))

row = 3
col = 0
pieces.append(Piece(surface, row, col, green))

for p in pieces:
    p.colorInGrid(board)

done=False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print(event.key)
            if event.key == pygame.K_ESCAPE:
                done = True
            if event.key == 32: #space bar
                pieces[0].rotate(board)
                board.clear()
                for p in pieces:
                    p.colorInGrid(board)
        '''elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()'''

    surface.fill(black)
    board.draw()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
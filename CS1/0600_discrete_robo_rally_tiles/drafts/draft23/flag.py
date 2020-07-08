from constants import *

class Flag:
    def __init__(self, screen, row, col, color):
        self.screen = screen
        self.row = row
        self.col = col
        self.color = color
        self.radius = 40*scaling
    def getCenter(self):
        offset_x = self.col*tile_width + tile_width/2
        offset_y = self.row*tile_height + tile_height/2
        return offset_x, offset_y
    def getCorners(self, x_adjust=0, shrink=1):
        #Returns list of points to draw the flag
        points = []
        offset_x, offset_y = self.getCenter()
        #top
        x = offset_x + x_adjust
        y = offset_y - self.radius*1.3*shrink
        points.append([int(x), int(y)])
        #tri corner flag
        x = offset_x -0.8*self.radius*shrink + x_adjust
        y = offset_y - self.radius*shrink
        points.append([int(x), int(y)])
        x = offset_x + x_adjust
        y = offset_y - 0.7*self.radius*shrink
        points.append([int(x), int(y)])
        x = offset_x + x_adjust
        y = offset_y - self.radius*1.3*shrink
        points.append([int(x), int(y)])
        #base
        x = offset_x + x_adjust
        y = offset_y + self.radius*0.8*shrink
        points.append([int(x), int(y)])
        return points
    def draw(self):
        points = self.getCorners()
        pygame.draw.polygon(self.screen, self.color,
                            points,int(scaling*8))
        pygame.draw.circle(self.screen, self.color,
                        points[-1], int(scaling*12))
    def drawSmall(self, adjust, scale):
        points = self.getCorners(x_adjust=adjust, shrink=scale)
        pygame.draw.polygon(self.screen, self.color,
                            points,int(scaling*8))
        pygame.draw.circle(self.screen, self.color,
                        points[-1], int(scaling*12))

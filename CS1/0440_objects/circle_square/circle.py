import math

class Circle:
    #Create a Circle with the given radius
    def __init__(self, radius):
        self.radius = radius

    #Return the area of this circle
    def getArea(self):
        return math.pi*self.radius**2

    #Return the diameter of this circle
    def getDiameter(self):
        return 2*self.radius

    #Return the circumference of this circle
    def getCircumference(self):
        return math.pi*self.getDiameter()

'''Usually when we create a class, we give the class its own separate 
Python file. Since I have a Python file named circle.py in the same 
folder, I can simply import then use it.'''
import circle

radius = float(input("What would you like the radius to be?"))
#Create a circle object
c = circle.Circle(radius)
a = c.getArea()
print("Area: "+str(a))
circ = c.getCircumference()
print("Circumference: "+str(circ))
d = c.getDiameter()
print("Diameter: "+str(d))

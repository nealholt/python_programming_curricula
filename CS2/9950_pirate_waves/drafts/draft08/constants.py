
black=0,0,0
blue=(0,0,255)
red=(255,0,0)
green=(0,255,0)
screen_width = 1000
screen_height = 600

#Spacing between water height locations
spacing = 10 #pixels
sea_level = 200
friction = 0.01
surface_tension = 0.3

#For scaling down the image
scaling = 0.2

#Buffer of empty pixels around boat image to make the boat
#sink down in the water more.
buffer = 15

#Upward pressure from being under water. Is a function of depth
bouyancy = 0.09
#Constant downward acceleration
gravity = 0.5
air_friction = 0.01
water_friction = 0.1

#Use to oscillate the right-most water_heights value
amplitude = 100
period = 30

#Controls for the player's boat
jump_power = 20 #instantaneous change to dy when jumping
speed = 3 #shift left or right in pixels per frame
tilt = 1.5 #downward pressure from left and right movement

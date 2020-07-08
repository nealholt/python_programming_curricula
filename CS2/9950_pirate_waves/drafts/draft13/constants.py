
black=0,0,0
blue=(0,0,255)
sky_blue=(200,200,255)
red=(255,0,0)
green=(0,255,0)
yellow=(255,255,0)
screen_width = 1000
screen_height = 600

#Spacing between water height locations
spacing = 10 #pixels
sea_level = 200
friction = 0.02
surface_tension = 0.3
#Number of water spacings beyond the right side of the screen that
#the water extends
water_extension = 5

#For scaling down the image
scaling = 0.2
compass_scaling = 0.1

#Buffer of empty pixels around boat image to make the boat
#sink down in the water more.
buffer = 7

#Upward pressure from being under water. Is a function of depth
bouyancy = 0.2
#Constant downward acceleration
gravity = 0.6
air_friction = 0.01
water_friction = 0.1

#Use to oscillate the right-most water_heights value
amplitude = 150
period = 25

#Controls for the player's boat
jump_power = 22 #instantaneous change to dy when jumping
speed = 1.5 #shift left or right in pixels per frame

rum_scroll_speed_min = 2
rum_scroll_speed_max = 5
rum_respawn_min = 30
rum_respawn_max = 90
rum_collision_distance = 40

sword_respawn_min = 90
sword_respawn_max = 150

#How far above sea level to spawn swords and rum
spawn_above_sea_level = 100

#Speed of cannon ball shot
cannon_ball_speed=20
cannon_ball_arc=3.1415/3

#Depth at which the boat causes a splash in the water.
splash_depth = 45
splash_delay = 15 #delay in frames before the boat can cause another splash.
splash_adjust = 15 #adjustment to reduce magnitude of splash. Unit is pixels

#This determines how long to dwell on each frame of the cannon shot smoke.
#Dwell of zero skips the image
dwell_sequence = []
for _ in range(27):
    dwell_sequence.append(0)
for _ in range(6):
    dwell_sequence.append(5)
for _ in range(3):
    dwell_sequence.append(1)

#Drift for the smoke from cannon shots
smoke_dx = -3

#This determines how long to dwell on each frame of the cannon shot explosion.
blast_dwell_sequence = []
for _ in range(24):
    blast_dwell_sequence.append(1)
for _ in range(12):
    blast_dwell_sequence.append(0)

#Enemy boat attributes
enemy_health = 3
enemy_volley_count = 3 #Shots per volley
enemy_volley_delay = 180 #delay between volleys
arc_adder = 3.1415/8 #Adder to the enemy boat's cannon ball arc
random_arc_adder = 3.1415/4

#Delay before the next enemy boat spawn
enemy_spawn_delay = 60*20 #20 seconds

enemy_stop_point = screen_width/2
all_sprites = []

SHAPE_CIRCLE = 0
SHAPE_RECT = 1
SHAPE_TRI = 2
SHAPE_PENTA = 3

TYPE_CRITTER = 0
TYPE_FOOD = 1
TYPE_BULLET = 2
TYPE_ANIMATION = 3
TYPE_POWERUP = 4

red_food_xp = 1
red_food_hp = 2
red_food_radius = 25
red_food_hit_radius = 15
red_food_count = 50

yellow_food_xp = 3
yellow_food_hp = 5
yellow_food_radius = 25
yellow_food_hit_radius = 15
yellow_food_count = 25

blue_food_xp = 9
blue_food_hp = 15
blue_food_radius = 40
blue_food_hit_radius = 30
blue_food_count = 5

border_shove_impulse = 0.35
world_size = 2000
enemy_count = 0
bullet_friction = 0.01

powerup_time = 360 #frames
#Center the powerup hitbox better in the center of the word
powerup_x_shift = -40
powerup_options = ["invincibility", "teleporter",
        "spread shot","big shot", "speed boost", "shove"]

#Attribute indicies
ACCEL_INDEX = 0
HP_INDEX = 1
COLLISION_DAMAGE_INDEX = 2
REFIRE_DELAY_INDEX = 3
BULLET_DAMAGE_INDEX = 4
BULLET_SPEED_INDEX = 5
BULLET_LONGEVITY_INDEX = 6
BULLET_HP_INDEX = 7
HP_REGEN_INDEX = 8
BULLET_SIZE_INDEX = 9
RECOIL_INDEX = 10
VISION_RADIUS_INDEX = 11
SHOVE_INDEX = 12
FRICTION_INDEX = 13
ARMOR_INDEX = 14
BULLET_COUNT_INDEX = 15
BULLET_SPREAD_INDEX = 16

level_list = [
    [0,0.2,0.3,0.4], #accel
    [10,20], #hp
    [1,1], #collision damage
    [0,20], #refire delay
    [0,1], #bullet damage
    [0,7,8], #bullet speed
    [0,80,90,100,110,120], #bullet longevity
    [0,1], #bullet hp
    [0,0.01], #hp regen
    [0,6], #bullet size
    [0,2], #recoil
    [0,500], #vision radius
    [1,1], #shove out
    [0.05,0.05], #friction
    [1,1], #armor. this is a multiplier on damage taken. Used only for invincibility initially.
    [0,1], #bullet count
    [0,3.1415/32.0], #bullet spread
    ]

levelup_text = ['Accel','HP','Collision damage',
        'Refire','Bullet damage','Bullet speed',
        'Bullet life','Penetration','Regeneration']

#Points at which next level has been reached
level_cutoffs = [10,20,40,80,120,160,220,280,340]

screen_width = 1100
screen_height = 650
screen_width_half = int(screen_width/2)
screen_height_half = int(screen_height/2)
green = 0,255,0
red = 255,0,0
blue = 0,0,255
mid_blue = 100,200,255
pale_blue = 175,238,238
green = 0,255,0
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

def getDefault(level, index):
    '''Get default value at given level for the
    given attribute index.'''
    return level_list[index][level]

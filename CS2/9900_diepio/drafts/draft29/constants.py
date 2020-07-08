all_sprites = []

TYPE_CRITTER = 0
TYPE_FOOD = 1
TYPE_BULLET = 2
TYPE_ANIMATION = 3
TYPE_POWERUP = 4

border_shove_impulse = 0.35
world_size = 2000
food_hp = 10
food_radius = 15
food_count = 100
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
    [0,0.1,0.2,0.3], #accel
    [10,500], #hp
    [10,60], #collision damage
    [0,20], #refire delay
    [0,30], #bullet damage
    [0,7,8], #bullet speed
    [0,80,90,100,110,120], #bullet longevity
    [0,1], #bullet hp
    [0,1], #hp regen
    [0,6], #bullet size
    [0,2], #recoil
    [0,500], #vision radius
    [0.3,0.3], #shove out
    [0.05,0.05], #friction
    [1,1], #armor. this is a multiplier on damage taken. Used only for invincibility initially.
    [0,1], #bullet count
    [0,3.1415/16.0], #bullet spread
    ]

screen_width = 1100
screen_height = 650
green = 0,255,0
red = 255,0,0
blue = 0,0,255
green = 0,255,0
yellow = 255,255,0
white = 255,255,255
black = 0,0,0

def getDefault(level, index):
    '''Get default value at given level for the
    given attribute index.'''
    return level_list[index][level]

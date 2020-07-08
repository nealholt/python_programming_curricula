import pygame, image_loader, random, sprite
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
fps = 60

#Original dimensions of each square image
original_size = 16

#Dictionary of images
scale_factor = 2 #2x larger
images = image_loader.getImageDictionary(scale_factor)

#Scaled size of each square image
size = original_size*scale_factor

#Get spike floor frames
spike_floor_frames = []
for i in range(4): #4 is the number of spike floor frames
    spike_floor_frames.append(images['floor_spikes_anim_f'+str(i)])

#Get fountain mid red frames
fountain_mid_red_frames = []
for i in range(3): #3 is the number of fountain mid red frames
    fountain_mid_red_frames.append(images['wall_fountain_mid_red_anim_f'+str(i)])

#Get basin red frames
basin_red_frames = []
for i in range(3): #3 is the number of basin red frames
    basin_red_frames.append(images['wall_fountain_basin_red_anim_f'+str(i)])

'''
wall_fountain_mid_blue_anim_f0
wall_fountain_mid_blue_anim_f1
wall_fountain_mid_blue_anim_f2
wall_fountain_basin_blue_anim_f0
wall_fountain_basin_blue_anim_f1
wall_fountain_basin_blue_anim_f2
wall_hole_1
wall_hole_2
wall_banner_red
wall_banner_blue
wall_banner_green
wall_banner_yellow

wall_corner_top_left
wall_corner_top_right
wall_corner_left
wall_corner_right
wall_corner_bottom_left
wall_corner_bottom_right
wall_corner_front_left
wall_corner_front_right
wall_inner_corner_l_top_left
wall_inner_corner_l_top_right
wall_inner_corner_mid_left
wall_inner_corner_mid_right
wall_inner_corner_t_top_left
wall_inner_corner_t_top_right
'''

floors = ['floor_1','floor_2','floor_3','floor_4','floor_5','floor_6','floor_7','floor_8','floor_ladder','edge','hole','spike_trap']

def stringListToSpriteList(string_list,inset,buffer):
    '''This function takes a 2d list of strings and
    returns a 2d list of sprite objects.'''
    sprite_list = []
    for r in range(len(string_list)):
        temp = []
        for c in range(len(string_list[r])):
            s = getSprite(string_list[r][c],r,c,images,inset,buffer)
            temp.append(s)
        sprite_list.append(temp)
    return sprite_list

def getSprite(sprite_name, r, c, images, inset, buffer):
    if sprite_name == 'wall_fountain_mid_red':
        return sprite.AnimatedSprite(screen, inset+c*size, r*size+buffer, fountain_mid_red_frames, 15)
    elif sprite_name == 'wall_fountain_basin_red':
        return sprite.AnimatedSprite(screen, inset+c*size, r*size+buffer, basin_red_frames, 15)
    elif sprite_name == 'spike_trap':
        return sprite.AnimatedSprite(screen, inset+c*size, r*size+buffer, spike_floor_frames, 20)
    elif sprite_name == '':
        return None
    else:
        return sprite.Sprite(screen, inset+c*size, r*size+buffer, images[sprite_name])


def getBasicRoom(images,rows,columns):
    #Make top wall. This only makes the tippy
    #top of the wall
    top_row = ['wall_side_top_left','wall_corner_top_left']
    #minus 4 for the two wall tiles on each side, left and right
    for _ in range(columns-4):
        top_row.append('wall_top_mid')
    top_row.append('wall_corner_top_right')
    top_row.append('wall_side_top_right')
    #This next part makes the bulk of the wall
    second_row = ['wall_side_mid_left']
    #minus 2 for the one wall on each side, left and right
    for _ in range(columns-2):
        second_row.append('wall_right') #What about other options here?
        #Some tiles seem indistinguishable. I need to figure out if
        #there is a difference between wall_right, wall_left
        #wall_corner_front_right, and wall_corner_front_left
    second_row.append('wall_side_mid_right')
    #Make interior
    room = [top_row,second_row]
    #Minus 4 for the 2 rows at the top and 2 at the bottom
    for r in range(rows-4):
        temp = ['wall_side_mid_left']
        #minus 2 for the one wall on each side, left and right
        for c in range(columns-2):
            temp.append('floor_1')
        temp.append('wall_side_mid_right')
        room.append(temp)
    #Make bottom wall
    bottom_topper = ['wall_side_top_left']
    #minus 2 for the two wall tiles on each side, left and right
    for _ in range(columns-2):
        bottom_topper.append('wall_top_mid') #TODO try bottom mid
    bottom_topper.append('wall_side_top_right')
    room.append(bottom_topper)
    #This next part makes the bulk of the wall
    room.append(second_row)
    return room

def getRandomFloor(images,rows,columns,buffer,inset):
    dungeon_floor = []
    for r in range(rows):
        temp = []
        for c in range(columns):
            floor = random.choice(floors)
            s = getSprite(floor, r, c, images, inset, buffer)
            temp.append(s)
        dungeon_floor.append(temp)
    return dungeon_floor

#Build random flooring:
buffer = 30
inset = 10
rows = 8
columns = 8
#dungeon_floor = getRandomFloor(images, rows,columns,buffer,inset)

dungeon_floor = getBasicRoom(images,rows,columns)
dungeon_floor = stringListToSpriteList(dungeon_floor,inset,buffer)


#I extended the wall on purpose in the top row here
#to show how you could make a taller wall.
custom_dungeon =[
    ['','','','','','wall_corner_top_right',''],
    ['wall_side_top_left','wall_corner_top_left','wall_column_top','wall_top_mid','wall_fountain_top','wall_right','wall_side_top_right'],
    ['wall_side_mid_left','wall_right','wall_column_mid','wall_goo','wall_fountain_mid_red','wall_right','wall_side_mid_right'],
    ['wall_side_mid_left','floor_1','wall_column_base','wall_goo_base','wall_fountain_basin_red','floor_1','wall_side_mid_right'],
    ['wall_side_mid_left','floor_1','floor_1','floor_1','floor_1','floor_1','wall_side_mid_right'],
    ['wall_side_mid_left','floor_1','floor_1','column_top','floor_1','floor_1','wall_side_mid_right'],
    ['wall_side_front_left','floor_1','floor_1','column_mid','floor_1','floor_1','wall_side_mid_right'],
    ['wall_side_front_left','floor_1','floor_1','column_base','floor_1','floor_1','wall_side_front_right'],
    ['doors_all','doors_frame_left','doors_frame_top','doors_frame_right','doors_leaf_closed','doors_leaf_open'],
    ['','','','',''],

    ['wall_corner_top_left','wall_top_mid','wall_top_mid','wall_corner_top_right'],
    ['wall_corner_left','wall_right','wall_corner_front_right','wall_corner_right'],
    ['wall_corner_bottom_left','wall_top_mid','wall_top_mid','wall_corner_bottom_right']
    ]
walls = stringListToSpriteList(custom_dungeon,inset+300,buffer)

#TODO: Columns should be drawn overtop of floor tiles.

#TODO: Doors are twice as tall as regular tiles:
print(images['doors_frame_left'].get_rect().width)


done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0)) #fill the screen with black. Erase previous images

    for row in dungeon_floor:
        for c in row:
            if not(c is None):
                c.update()
                c.draw()


    for row in walls:
        for c in row:
            if not(c is None):
                c.update()
                c.draw()


    pygame.display.flip()
    #Delay to get desired frames per second
    clock.tick(fps)

pygame.quit()
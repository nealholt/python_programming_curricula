import pygame, image_loader, random, sprite

pygame.init()



screen = pygame.display.set_mode((500,600))
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


#Build random flooring:
rows = 5
columns = 8
dungeon_floor = []
for r in range(rows):
    temp = []
    for c in range(columns):
        floor = random.choice(floors)
        if floor == 'spike_trap':
            s = sprite.AnimatedSprite(screen, c*size, r*size, spike_floor_frames, 20)
        else:
            s = sprite.Sprite(screen, c*size, r*size, images[floor])
        temp.append(s)
    dungeon_floor.append(temp)



custom_dungeon =[
    ['wall_top_left','wall_column_top','wall_top_mid','wall_fountain_top','wall_corner_top_right','wall_side_top_right'],
    ['wall_left','wall_column_mid','wall_goo','wall_fountain_mid_red','wall_right','wall_side_mid_right'],
    ['floor_1','wall_column_base','wall_goo_base','wall_fountain_basin_red','floor_1','wall_side_mid_right'],
    ['wall_side_top_left','floor_1','floor_1','floor_1','floor_1','wall_side_mid_right'],
    ['wall_side_mid_left','floor_1','floor_1','column_top','floor_1','wall_side_mid_right'],
    ['wall_side_front_left','floor_1','floor_1','column_mid','floor_1','wall_side_mid_right'],
    ['wall_side_front_left','floor_1','floor_1','column_base','floor_1','wall_side_front_right'],
    ['doors_all','doors_frame_left','doors_frame_top','doors_frame_right','doors_leaf_closed','doors_leaf_open']
    ]

#Columns should be drawn overtop of floor tiles.

#Doors are twice as tall as regular tiles:
print(images['doors_frame_left'].get_rect().width)


buffer = 200
walls = []
for r in range(len(custom_dungeon)):
    temp = []
    for c in range(len(custom_dungeon[r])):
        if custom_dungeon[r][c] == 'wall_fountain_mid_red':
            s = sprite.AnimatedSprite(screen, c*size, r*size+buffer, fountain_mid_red_frames, 15)
        elif custom_dungeon[r][c] == 'wall_fountain_basin_red':
            s = sprite.AnimatedSprite(screen, c*size, r*size+buffer, basin_red_frames, 15)
        else:
            s = sprite.Sprite(screen, c*size, r*size+buffer, images[custom_dungeon[r][c]])
        temp.append(s)
    walls.append(temp)


done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill((0,0,0)) #fill the screen with black. Erase previous images

    for row in dungeon_floor:
        for c in row:
            c.update()
            c.draw()


    for row in walls:
        for c in row:
            c.update()
            c.draw()

    pygame.display.flip()
    #Delay to get desired frames per second
    clock.tick(fps)

pygame.quit()
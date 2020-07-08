import pygame, image_loader, random

pygame.init()




#Dwell on each image for this many frames.
dwell_reset = 20

class AnimatedSprite:
    def __init__(self, screen, x, y, frames):
        self.screen = screen
        self.x = x
        self.y = y
        self.index = 0
        self.dwell = dwell_reset
        self.frames = frames
        self.rect = self.frames[self.index].get_rect()

    def advanceImage(self):
        self.dwell -= 1
        if self.dwell < 0:
            self.index = (self.index+1)%len(self.frames)
            self.dwell = dwell_reset

    def draw(self):
        screen.blit(self.frames[self.index],
                     ( int(self.x-self.rect.width/2),
                       int(self.y-self.rect.height/2) ))


screen = pygame.display.set_mode((500,300))
clock = pygame.time.Clock()
fps = 60

#Dictionary of images
scale_factor = 2 #2x larger
images = image_loader.getImageDictionary(scale_factor)

spike_floor = 'floor_spikes_anim_f'
spike_floor_num = 4
frames = []
for i in range(spike_floor_num):
    frames.append(images[spike_floor+str(i)])
spike_floor = AnimatedSprite(screen, 100, 50, frames)

size = spike_floor.rect.width

spike_floor.x = size*2+size/2
spike_floor.y = size*3+size/2

'''
wall_fountain_top
wall_fountain_mid_red_anim_f0
wall_fountain_mid_red_anim_f1
wall_fountain_mid_red_anim_f2
wall_fountain_basin_red_anim_f0
wall_fountain_basin_red_anim_f1
wall_fountain_basin_red_anim_f2
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
column_top
column_mid
coulmn_base
wall_column_top
wall_column_mid
wall_coulmn_base
wall_goo
wall_goo_base
wall_side_top_left
wall_side_top_right
wall_side_mid_left
wall_side_mid_right
wall_side_front_left
wall_side_front_right
wall_corner_top_left
wall_corner_top_right
wall_corner_left
wall_corner_right
wall_corner_bottom_left
wall_corner_bottom_right
wall_corner_front_left
wall_corner_front_right
wall_inner_corner_l_top_left
wall_inner_corner_l_top_rigth
wall_inner_corner_mid_left
wall_inner_corner_mid_rigth
wall_inner_corner_t_top_left
wall_inner_corner_t_top_rigth
edge
hole
doors_all
doors_frame_left
doors_frame_top
doors_frame_righ
doors_leaf_closed
doors_leaf_open
'''

floors = ['floor_1','floor_2','floor_3','floor_4','floor_5','floor_6','floor_7','floor_8','floor_ladder']


#Build random flooring:
rows = 5
columns = 8
dungeon_floor = []
for r in range(rows):
    temp = []
    for c in range(columns):
        temp.append(random.choice(floors))
    dungeon_floor.append(temp)



wall_tops = ['wall_top_left','wall_top_mid','wall_top_mid','wall_top_mid','wall_top_right']


walls = ['wall_left','wall_mid','wall_mid','wall_mid','wall_right']



image_index = 0
done = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    screen.fill((0,0,0)) #fill the screen with black. Erase previous images

    for r in range(len(dungeon_floor)):
        for c in range(len(dungeon_floor[r])):
            screen.blit(images[dungeon_floor[r][c]],
                     (c*size, r*size) )


    spike_floor.draw()
    spike_floor.advanceImage()



    for w in range(len(walls)):
        screen.blit(images[walls[w]],
                     (w*size, 200) )


    pygame.display.flip()
    #Delay to get desired frames per second
    clock.tick(fps)

pygame.quit()
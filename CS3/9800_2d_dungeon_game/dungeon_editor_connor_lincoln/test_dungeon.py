import pygame, image_loader, random, sprite, json

pygame.init()

green = (0,0,225)

screen = pygame.display.set_mode((1200,1000))
clock = pygame.time.Clock()
fps = 60

font = pygame.font.SysFont('Arial',25)
save_text = font.render('save',True,(0,0,0))

with open('dungeon_1') as f:
    custom_dungeon = json.load(f)

#Original dimensions of each square image
original_size = 16

#Dictionary of images
scale_factor = 2 #2x larger
images = image_loader.getImageDictionary(scale_factor)
def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list
list = getList(images)
object_rects = []
object_names = []
for i in range(120):
    object_names.append(list[i])
print(object_names)

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

board = []
blacksquaregrid = True
class GridSquare:

    def __init__(self,color,x,y,screen):

        self.x = x
        self.y = y
        self.surface = screen
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = color

    def draw(self):
        self.rect = pygame.Rect(self.rect.x,self.rect.y, 32, 32)
        pygame.draw.rect(self.surface, self.color, self.rect, 0)

for i in range(18):
    colomns = []
    blacksquaregrid = not blacksquaregrid
    for s in range(18):
        if blacksquaregrid == True:
            colomns.append(GridSquare((0,0,0),i*32,s*32,screen))
        else:
            colomns.append(GridSquare((255,255,255),i*32,s*32,screen))
        blacksquaregrid = not blacksquaregrid
    board.append(colomns)

def GridUpdate():
    global screen,board
    for i in range(18):
        for s in range(18):
            board[i][s].draw()

def get_sprite(image_name,r,c):
    if image_name == 'spike_trap':
        s = sprite.AnimatedSprite(screen, c*size, r*size, spike_floor_frames, 20)
    elif image_name == 'wall_fountain_mid_red':
        s = sprite.AnimatedSprite(screen, c*size, r*size, fountain_mid_red_frames, 15)
    elif image_name == 'wall_fountain_basin_red':
        s = sprite.AnimatedSprite(screen, c*size, r*size, basin_red_frames, 15)
    else:
        s = sprite.Sprite(screen, c*size, r*size, images[image_name])
    return s


'''
wall_top_left = get_sprite('wall_top_left',19,1)
wall_top_left_rect = images['wall_top_left'].get_rect()
wall_top_left_rect.x = 19*size
wall_top_left_rect.y = 1*size
object_rects.append(wall_top_left_rect)

wall_mid = get_sprite('wall_mid',19,5)
wall_mid_rect = images['wall_mid'].get_rect()
object_rects.append(wall_mid_rect)

floor_1 = get_sprite('floor_1',19,3)
floor_1_rect = images['floor_1'].get_rect()
object_rects.append(floor_1_rect)
'''
objects = []
x = 17
y = 1
for i in range(120):
    x += 2
    objects.append(get_sprite(object_names[i],y, x))
    object_rects.append(images[object_names[i]].get_rect())
    object_rects[i].x = x*size
    object_rects[i].y = y*size
    if x >= 35:
        y += 2
        x = 17
'''
custom_dungeon =[
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ['nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing','nothing'],
    ]
'''


#Columns should be drawn overtop of floor tiles.

#Doors are twice as tall as regular tiles:
print(images['doors_frame_left'].get_rect().width)
save_box = pygame.Rect(1100, 550, 100, 50)

buffer = 200
walls = []
for r in range(len(custom_dungeon)):
    temp = []
    for c in range(len(custom_dungeon[r])):
        print(custom_dungeon[r][c])
        s = get_sprite(custom_dungeon[r][c],r,c)
        temp.append(s)
    walls.append(temp)



object_selected = 'floor_1'
done = False
while not done:
    #Handle events
    pos = pygame.mouse.get_pos()
    b1,b2,b3 = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        for i in range(18):
            for s in range(18):
                #if event.type == pygame.MOUSEBUTTONUP and board[i][s].rect.collidepoint(pos):
                if b1 == True and board[i][s].rect.collidepoint(pos):
                    custom_dungeon[s][i] = object_selected
                    p = get_sprite(custom_dungeon[s][i],s,i)
                    walls[s][i] = p
        for i in range(len(object_rects)):
            if b1 == True and object_rects[i].collidepoint(pos):
                object_selected = object_names[i]
                print(object_selected)
        if b1 == True and save_box.collidepoint(pos):
            file_name = input("What do you want the file name to be? (no special characters or spaces)")
            with open(file_name, "w") as f:
                json.dump(custom_dungeon, f)
            done = True

    screen.fill((0,0,0)) #fill the screen with black. Erase previous images

    GridUpdate()

    for row in walls:
        for c in row:
            c.update()
            c.draw()

    for i in range(120):
        objects[i].draw()

    pygame.draw.rect(screen, (0,255,0), save_box, 0)
    screen.blit(save_text,(1130,560))

    pygame.display.flip()

    #Delay to get desired frames per second
    clock.tick(fps)

pygame.quit()
exit()

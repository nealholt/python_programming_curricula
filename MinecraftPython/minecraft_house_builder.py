import mcpi.minecraft
import mcpi.block as block
import time

'''
Procedural House-Building by Sam Lawyer
To use:
- start the script
- Place some diamond blocks in a pattern
- right click one with sword
- tada
'''

diamond = 57
tnt = 46
lapis = 21
cobble = 4
grassdirt = 2
plank = 5
ladder = 65
pane = 102
gravel = 13
slab = 44
stair = 53
air = 0
fence = 85
log = 17
leaf = 18
gold = 41

def checkHeight(x,y,z,data):
    larger = True
    height = 0
    while larger:
        block = mc.getBlockWithData(x,y+height,z);
        print(block.id, data)
        print(height, block.id == data)
        if block.id != data:
            larger = False
        else:
            height+=1
    return height



def wall(x,y,z):
    mc.setBlocks(x+3,y,z+3,x-3,y+2,z+3,plank)
    mc.setBlocks(x+2,y+1,z+3,x-2,y+1,z+3,pane)

def sidewall(x,y,z):
    mc.setBlocks(x+3,y,z+3,x+3,y+2,z+9,plank)
    mc.setBlocks(x+3,y+1,z+4,x+3,y+1,z+8,pane)



def roof(x,y,z):
    mc.setBlocks(x+3,y+3,z+2,x-3,y+3,z+10,slab)
    mc.setBlocks(x+4,y+3,z+3,x-4,y+3,z+9,slab)


def floor(x,y,z):
    mc.setBlocks(x+3,y-1,z+9,x-3,y-1,z+3,plank)


def doorway(x,y,z):
    mc.setBlocks(x+1,y+1,z+3,x-1,y+1,z+3,plank)
    mc.setBlocks(x,y+1,z+3,x,y,z+3,air)

def sideDoorway(x,y,z):
    mc.setBlocks(x+3,y+1,z+5,x+3,y+1,z+7,plank)
    mc.setBlocks(x+3,y+1,z+6,x+3,y,z+6,air)


def ladder(x,y,z,endy):
    if y > endy:
        mc.setBlocks(x-2,y,z+9,x-2,endy,z+9,plank)
        mc.setBlocks(x-2,y,z+8,x-2,endy,z+8,65, 2)

def groundFloor(x,y,z):
    floor(x,y,z)
    wall(x,y,z)
    roof(x,y,z)
    sidewall(x,y,z)
    sidewall(x-6,y,z)
    wall(x,y,z+6)
    doorway(x,y,z)
    doorway(x,y,z+6)
    sideDoorway(x,y,z)
    sideDoorway(x-6,y,z)

def noRoofFloor(x,y,z):
    floor(x,y,z)
    wall(x,y,z)
    sidewall(x,y,z)
    sidewall(x-6,y,z)
    wall(x,y,z+6)
    doorway(x,y,z)
    doorway(x,y,z+6)
    sideDoorway(x,y,z)
    sideDoorway(x-6,y,z)
    mc.setBlock(x-2,y+2,z+9,plank)

def tower(x,y,z,height):
    for i in range(height):
        j = i*4
        if i == 0:
            floor(x,y+j,z)
            wall(x,y+j,z)
            roof(x,y+j,z)
            sidewall(x,y,z)
            sidewall(x-6,y,z)
            wall(x,y+j,z+6)
            doorway(x,y,z)
        elif i == height-1:
            floor(x,y+j,z)
            wall(x,y+j,z)
            roof(x,y+j,z)
            sidewall(x,y+j,z)
            sidewall(x-6,y+j,z)
            wall(x,y+j,z+6)
            stairs(x,y+j-4,z)
        else:
            wall(x,y+j,z)
            roof(x,y+j,z)
            floor(x,y+j,z)
            sidewall(x,y+j,z)
            sidewall(x-6,y+j,z)
            wall(x,y+j,z+6)
            stairs(x,y+j-4,z)



def buildCors(x,y,z,x1,y1,z1):
    return (x - x1)*5 + x, (y-y1) * 3 + y, (z - z1) * 5 + z

def sprawl(x,y,z,startx,starty,startz,prevy,data):
    '''uses x,y,z for location, obviousyl, startx,y,and z allow it to
    calculate the difference from the starting point which helps
    when calculating where to build.
    data1 is the block that the blueprint must be built out of
    prevy is used to check where the last block was
    '''
    directions = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
    cords = buildCors(x,y,z,startx,starty,startz)
    x1,y1,z1 = cords[0],cords[1],cords[2]
    if prevy <= y:
        groundFloor(x1+10,y1,z1+7) # build at coordinates
    else:
        noRoofFloor(x1+10,y1,z1+7)
    ladder(x1+10,y1-1,z1+7,starty)
    mc.setBlock(x,y,z,0) # erase initial block
    for direction in directions:
        x1,y1,z1 = x+direction[0],y+direction[1],z+direction[2]
        nextblock = mc.getBlockWithData(x1,y1,z1)
        if nextblock.id == data:
            sprawl(x1,y1,z1,startx,starty,startz,y,data)






'''Build thing
delet diamond
check and call neighbors
'''



def checkHits(mc):
    #Access all the hits
    hits = mc.events.pollBlockHits()
    for hit in hits:
        #Get the block that was hit
        hit_block = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z);
        print(hit_block.id)
        if hit_block.id == lapis:
            mc.player.setPos(0,100,0)
            mc.setBlocks(-100,-15,-100,100,10,100,cobble)
            mc.setBlocks(-100, 11, -100, 100, 30, 100,0)
        elif hit_block.id == diamond:
            x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
            sprawl(x,y,z,x,y,z,y,diamond)
            '''
            height = checkHeight(x,y,z,diamond)
            width = checkWidth(x,y,z,diamond)
            depth = checkDepth(x,y,z,diamond)
            cube = checkCube(x,y,z,diamond,width,height,depth)
            print(cube,width,height,depth)
            sprawl(x,y,z,cube,width,height,depth)'''
            #tower(x,y,z,checkHeight(x,y,z,diamond))
        '''
        #Change the data of the bock so that it can be exploded
        hit_block.data = (hit_block.data + 1) & 0xf;
        #Set the modified block back in the world
        mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, hit_block.id, hit_block.data)
        #Confirm success by posting to chat
        mc.postToChat("Block data is now " + str(hit_block.data))
'''

#Get a variable to use to reference the minecraft world
mc = mcpi.minecraft.Minecraft.create();

while True:
    checkHits(mc)
    time.sleep(0.1)

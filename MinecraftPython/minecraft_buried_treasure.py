#Minecraft buried treasure
#This is the classic game of Warmer/Colder in which you have to find
#a hidden object by moving around and getting clues as to whether
#you have moved closer (warmer) or further away (colder).
#In this case the hidden object is a block of gold. Hit it for victory.
import mcpi.minecraft
import mcpi.block as block
import time, random, math

#Get a variable to use to reference the minecraft world
mc = mcpi.minecraft.Minecraft.create();

#These numbers represent blocks of type air and gold
air = 0
gold = 41

#This function takes two 3-dimensional coordinates and returns the 
#distance between the coordinates.
def distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt(math.pow(x1-x2,2)+math.pow(y1-y2,2)+math.pow(z1-z2,2))

#Get random x and z coordinates. These axes are both horizontal.
#y is vertical.
gold_x = random.randint(-120, 120)
gold_z = random.randint(-120, 120)
gold_y = 100 #Start at top of the world
#Start at the top and move down until you find something other than air
gold_block = mc.getBlock(gold_x, gold_y, gold_z)
while gold_block == air:
    gold_y -= 1
    gold_block = mc.getBlock(gold_x, gold_y, gold_z)
#Move down two more spaces to put the gold underground.
gold_y += 2
mc.setBlock(gold_x, gold_y, gold_z, gold)

#Test by printing coordinates of the gold block
#print(gold_x, gold_y, gold_z)

#Get the player's current position and distance so that when the
#player moves we can determine if they got closer or further from
#the gold.
playerx,playery,playerz = mc.player.getPos()
dist = distance(playerx, playery, playerz, gold_x, gold_y, gold_z)
while True:
    x,y,z = mc.player.getPos()
    #Check to see if the player's position has changed
    if x!=playerx or y!=playery or z!=playerz:
        temp_dist = distance(x, y, z, gold_x, gold_y, gold_z)
        #Print warmer if the distance is smaller, otherwise colder
        if temp_dist < dist:
            mc.postToChat('Warmer!')
        else:
            mc.postToChat('Colder  :(')
        #Update player distance and location
        dist = temp_dist
        playerx,playery,playerz = x,y,z
    #Check for hitting a block of gold.
    hits = mc.events.pollBlockHits()
    for hit in hits: #Hit is a right click
        hit_block = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z);
        print(hit_block.id)
        if hit_block.id == gold:
            mc.postToChat('Victory!!!!')
    #Update only every tenth of a second
    time.sleep(0.1)

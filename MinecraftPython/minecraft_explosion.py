#This script lets you detonate TNT
#Source: http://www.minecraftforum.net/forums/other-platforms/minecraft-pi-edition/1959950-how-to-set-off-tnt-in-minecraft-pi

import mcpi.minecraft
import mcpi.block as block
import time

'''
To use:
- start the script
- Place some TNT
- Right click one block of TNT with a sword
- the chat should read "Block data is now 1"
- left click the block of TNT a couple times
- BOOM!
'''

#This function lets your hits detonate TNT.
def lightFuse(mc):
    #Access all the hits
    hits = mc.events.pollBlockHits()
    for hit in hits:
        #Get the block that was hit
        hit_block = mc.getBlockWithData(hit.pos.x, hit.pos.y, hit.pos.z);
        #Change the data of the bock so that it can be exploded
        hit_block.data = (hit_block.data + 1) & 0xf;
        #Set the modified block back in the world
        mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, hit_block.id, hit_block.data)
        #Confirm success by posting to chat
        mc.postToChat("Block data is now " + str(hit_block.data))

#Get a variable to use to reference the minecraft world
mc = mcpi.minecraft.Minecraft.create();

while True:
    lightFuse(mc)
    time.sleep(0.1)

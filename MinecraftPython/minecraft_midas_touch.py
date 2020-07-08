#Midas Touch
#Run this program to turn any blocks beneath the player's feet into gold.
import mcpi.minecraft
import mcpi.block as block
import time

#Get a variable to use to reference the minecraft world
mc = mcpi.minecraft.Minecraft.create();

#These numbers represent blocks of type air and gold
air = 0
gold = 41

#Run forever
while True:
    #Get the coordinates of the player's current position
    x,y,z = mc.player.getPos()
    #Get the block directly beneath the player.
    #Note that the x axis is left to right,
    #the y axis is up and down, and
    #the z axis is front to back, relative to the player.
    block_below = mc.getBlock(x, y-1, z)
    #Convert any non-air blocks beneath the player's feet into gold
    if block_below != air:
        mc.setBlock(x,y-1,z, gold)
    time.sleep(0.1)

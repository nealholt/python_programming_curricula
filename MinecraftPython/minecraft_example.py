#Open minecraft and create a new game first.
#Use tab to free the mouse from the minecraft window.

import mcpi.minecraft
import time
import mcpi.block as block

#Get a variable to use to reference the minecraft world
mc = mcpi.minecraft.Minecraft.create()  #Connect to and open minecraft world

#Teleport the player to a specific location.
def teleport():
    mc.postToChat('Teleporting...') #post message to chat
    mc.player.setPos(50, 100, 90) #x, y, z

#Teleport the player 50 blocks up into the air.
def superjump():
    mc.postToChat('Jump!') #post message to chat
    x, y, z = mc.player.getPos()
    mc.player.setPos(x, y+50, z) #x, y, z

#Construct a tower of 50 stones in front of the player.
def makeTower():
    mc.postToChat('Build Tower!') #post message to chat
    x, y, z = mc.player.getPos()
    stone = 1
    for i in range(50):
        mc.setBlock(x, y+i, z+5, stone)
        time.sleep(0.2)

#Construct a tower of 50 water in front of the player.
def makeWaterTower():
    mc.postToChat('Build Tower!') #post message to chat
    x, y, z = mc.player.getPos()
    water = 8
    for i in range(50):
        mc.setBlock(x, y+i, z+5, water)
        time.sleep(0.2)

#Construct a solid block of gold in front of the player.
def makeGoldBlock():
    mc.postToChat('Build Gold!') #post message to chat
    gold = 41
    x, y, z = mc.player.getPos()
    #Build a block of gold starting at your x and y and extending 10x10x10
    mc.setBlocks(x, y, z, x+10, y+10, z+10, gold)

#Construct a solid block of TNT in front of the player.
def makeTNTBlock():
    mc.postToChat('Build TNT!') #post message to chat
    gold = 41
    x, y, z = mc.player.getPos()
    #Build a block of TNT starting at your x and y and extending 10x10x10
    mc.setBlocks(x, y, z, x+10, y+10, z+10, block.TNT)

#As an example we will call the teleport function.
#Call the other functions to test them out.
teleport()
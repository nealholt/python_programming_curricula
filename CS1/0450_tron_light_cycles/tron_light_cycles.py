'''
For 300 points, create a game of Tron Light Cycles inspired by this clip:
www.youtube.com/watch?v=-3ODe9mqoDE

One player will use the arrow keys to change the direction of a red square.
The other player will use the wasd keys to change the direction of a blue square.

If either player's square runs into the other player's color or runs off the
screen, they lose.

The squares both keep moving even if the players are no longer pressing any
buttons.

You must use objects to represent the squares.

Study the following code. It will be very useful to you:

#Create a screen that is 700 pixels wide and 400 pixels tall
surface = pygame.display.set_mode((700,400))
#Create a variable for the color blue
blue = 0,0,255
#Create a variable for a pair of (x,y) coordinates on the screen
position = (4,10)
#Ask if the pixel at position is blue. If so, print "It's blue!"
#This will help you detect if one player is about to run into the
#other player's color.
if surface.get_at(position) == blue:
    print("It's blue!")

#Normally we do something like the following to erase the screen back
#to black or white between each frame. DON'T DO THIS for this project.
black = (0,0,0)
surface.fill(black) #fill surface with black

'''

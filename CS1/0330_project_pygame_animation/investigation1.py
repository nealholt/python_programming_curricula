
'''For 18 points, answer the following questions AFTER downloading
the images folder and the face_front image. Also make sure the code 
you are running to answer these questions is saved in a file in the
same folder as the images folder.'''

#1. Run the following program. Describe in one sentence what happens.
import pygame
pygame.init()
screen_width = 100
screen_height = 150
dimensions = (screen_width,screen_height)
surface = pygame.display.set_mode(dimensions)


#2. What happens when you try to close the above program?


#3. Modify your program by adding pygame.quit() to the end of it. What 
#happens now when you try to close it?


#4. Put
import time
#at the top of your program then add the following code after the
#creation of the surface variable, but before pygame.quit() then 
#describe what happens.

#Load an image from file
image = pygame.image.load('images/left000.png')
#Fill the drawing surface with black. (This also erases any previous images)
screen.fill((0,0,0))
#Draw the image on the surface
screen.blit(image, (0,0))
#Update the surface to dsiplay the new drawing.
pygame.display.flip()
#Pause for two seconds
time.sleep(2)


#6. What error do you get if you mis-type the image file name?


#Change the file name to use the face_front image. Note that this image
#is not in the same folder as the other images.
#7. What does your image.load line of code look like now?


#8. What happens if you forget this line?
pygame.display.flip()


#9. What do these numbers do? Figure it out by experimenting with 
#other values.
screen.blit(image, (0,0))


#10. Figure out what these numbers do by experimenting with other values.
screen.fill((0,0,0))

import pygame

pygame.init()

screen = pygame.display.set_mode((500,200))
clock = pygame.time.Clock()

right_images = ["images/right000.png","images/right001.png","images/right002.png","images/right003.png"]
left_images = ["images/left000.png","images/left001.png","images/left002.png","images/left003.png"]
turning_images = ["images/turning.png", "images/turningleft.png"]

x = 300
image_index = 0
done = False
moving_left = True
turning = False
while not done:
    #Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if turning:
        image = pygame.image.load(turning_images[image_index])
        image_index = image_index+1
        turning = image_index >= len(turning_images)
        if not turning:
            image_index = 0
    #Walk left
    elif moving_left:
        image = pygame.image.load(left_images[image_index])
        moving_left = x > 100
        x = x-5
        image_index = (image_index+1)%len(left_images)
        turning = not moving_left
        if turning:
            image_index = 0
    #Walk right
    elif not moving_left:
        image = pygame.image.load(right_images[image_index])
        moving_left = x > 300
        x = x+5
        image_index = (image_index+1)%len(right_images)
        turning = moving_left
        if turning:
            image_index = 0
    screen.fill((0,0,0)) #fill the screen with black. Erase previous images
    screen.blit(image, (x,20))
    pygame.display.flip()
    #Delay to get 10 fps
    clock.tick(10)

pygame.quit()
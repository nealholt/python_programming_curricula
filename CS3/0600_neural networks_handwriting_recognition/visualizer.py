'''
https://www.kaggle.com/strideradu/handwriting
'''
import pygame


def parseLine(file_handle):
    '''Reads in the next line and parses it into a 2d array of gray scale
    values.'''
    line = file_handle.readline()
    line = line.strip()
    line = line.split(',')
    data = []
    print()
    print("Value: "+line[0])
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(int(line[1+i*rows+j]))
        data.append(temp)
    return data

def drawData(data, screen):
    for i in range(rows):
        for j in range(columns):
            color = (data[i][j],data[i][j],data[i][j])
            pygame.draw.rect(screen, color, [j*pixel_size, i*pixel_size, pixel_size, pixel_size])
    pygame.display.flip()


if __name__ == "__main__":
    # Initialize the game engine
    pygame.init()

    rows = 28
    columns = 28
    pixel_size = 20
    # Set the height and width of the screen
    size = [columns*pixel_size, rows*pixel_size]
    screen = pygame.display.set_mode(size)

    #Start reading in training data
    file_handle = open('data/train.csv', 'r')
    file_handle.readline() #burn the first line. It's just the header

    #Loop until the user clicks the close button.
    done = False
    clock = pygame.time.Clock()
    while not done:
        # This limits the while loop to a max of 10 times per second.
        # Leave this out and we will use all CPU we can.
        clock.tick(10)

        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            elif event.type == pygame.KEYUP:
                #draw new data when any input arrives
                data = parseLine(file_handle)
                drawData(data, screen)
    file_handle.close()
    pygame.quit()

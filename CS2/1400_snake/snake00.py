import pygame
import sys
import time
import random

#Sarah Maurice found this online.

def main():
    """Snake v 1.01"""
    score = 0  # Initial score
    fps = pygame.time.Clock()
    direction = "RIGHT"  # Initial direction
    snake_position = [100, 50]  # Initial snake position
    snake_body = [[100, 50], [90, 50], [100, 50]]  # Initial snake body
    # It places the food randomly, excluding the border
    food_position = [random.randint(1, 71) * 10, random.randint(1, 45) * 10]
    food_spawn = True
    # Game surface
    player_screen = pygame.display.set_mode((720, 460))  # Set screen size
    pygame.display.set_caption("Snake v.1.01")  # Set screen title and version
    # Will define the colors
    red = pygame.Color("red")
    green = pygame.Color("green")
    black = pygame.Color("black")
    orange = pygame.Color("orange")
    white = pygame.Color("white")
 
    def bug_check():
        """ Checks the mistakes, and closes the program if it does while
       printing on the console how many bugs it has """
        bugs = pygame.init()
        if bugs[1] > 0:
            print("There are", bugs[1], "bugs! quiting.....")
            time.sleep(3)
            sys.exit("Closing program")
        else:
            print("The game was initialized")
 
    def you_lose():
        """ When the players loses, it will show a red message in times new
        roman font with 44 px size in a rectangle box"""
        font_game_over = pygame.font.SysFont("times new roman", 44)
        game_over_surface = font_game_over.render("aww you can do better :(", True, red)
        game_over_position = game_over_surface.get_rect()
        game_over_position.midtop = (360, 15)
        player_screen.blit(game_over_surface, game_over_position)
        scoring(1)
        pygame.display.flip()  # Updates the screen, so it doesnt freeze
        quiting()
 
    def quiting():
        """ When this function is called, it will wait 4 seconds and exit"""
        time.sleep(4)
        pygame.quit()
        sys.exit()
 
    def scoring(game_over=0):
        """ It will show the score on the top-left side of the screen in times new
       roman font with 16px size and black color in a rectangle box"""
        score_font = pygame.font.SysFont("times new roman", 16)
        score_surface = score_font.render("Score : {}".format(score), True, black)
        score_position = score_surface.get_rect()
        if game_over == 0:  # By default it puts it on the top-left
            score_position.midtop = (40, 10)
        else:  # Unless its game over, where it puts below the game over message
            score_position.midtop = (360, 80)
        player_screen.blit(score_surface, score_position)
 
    bug_check()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quiting()
            elif event.type == pygame.KEYDOWN:
                # Choose direction by user input, block opposite directions
                key_right = event.key == pygame.K_RIGHT or event.key == ord("d")
                key_left = event.key == pygame.K_LEFT or event.key == ord("a")
                key_down = event.key == pygame.K_DOWN or event.key == ord("s")
                key_up = event.key == pygame.K_UP or event.key == ord("w")
                if key_right and direction != "LEFT":
                    direction = "RIGHT"
                elif key_left and direction != "RIGHT":
                    direction = "LEFT"
                elif key_down and direction != "UP":
                    direction = "DOWN"
                elif key_up and direction != "DOWN":
                    direction = "UP"
                elif event.key == pygame.K_ESCAPE:
                    quiting()  # It will quit when esc is pressed
        # Simulates the snake movement(together with snake_body_pop)
        if direction == "RIGHT":
            snake_position[0] += 10
        elif direction == "LEFT":
            snake_position[0] -= 10
        elif direction == "DOWN":
            snake_position[1] += 10
        elif direction == "UP":
            snake_position[1] -= 10
        # Body mechanics
        snake_body.insert(0, list(snake_position))
        if snake_position == food_position:
            score += 1  # Every food taken will raise the score by 1
            food_spawn = False  # It removes the food from the board
        else:
            # If the food is taken it will not remove the last body piece(raising snakes size)
            snake_body.pop()
        if food_spawn is False:  # When a food is taken it will respawn randomly
            food_position = [random.randint(1, 71) * 10, random.randint(1, 45) * 10]
        food_spawn = True  # It will set the food to True again, to keep the cycle
        # Drawing
        player_screen.fill(white)  # Set the background to white
        for position in snake_body:  # Snake representation on the screen
            pygame.draw.rect(player_screen, green, pygame.Rect(position[0], position[1], 10, 10))
        # Food representation on the screen
        pygame.draw.rect(player_screen, orange, pygame.Rect(food_position[0], food_position[1], 10, 10))
        if snake_position[0] not in range(0, 711) or snake_position[1] not in range(0, 451):
            you_lose()  # Game over when the Snake hit a wall
        for block in snake_body[1:]:
            if snake_position == block:
                you_lose()  # Game over when the Snake hits itself
        scoring()
        pygame.display.flip()  # It constantly updates the screen
        fps.tick(20)  # It sets the speed to a playable value
 
 
if __name__ == "__main__":
    main()
import pygame  # creating the screen for the games
import time  # importing the time module for adding delay in execution time
import random  # importing a module named random for random number generation

pygame.init()  # initializing the display

display_height = 800
display_width = 600
# setting the mode as to how to display

display = pygame.display.set_mode((display_height, display_width))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)  # colors

pygame.display.update()  # this updates the screen to any changes
# setting the caption for the screen
pygame.display.set_caption("Snake Game v0.1")


snake_block = 10  # block size
snake_speed = 30  # block movement time


clock = pygame.time.Clock()  # clock the current time

font_style = pygame.font.SysFont(None, 50)  # no idea kya error aara

t = 2


def message(msg, color):
    message = font_style.render(msg, True, color)
    display.blit(message, [display_width/3, display_height/3])


def gameLoop():  # creating a function for the game controls
    game_over = False  # condition for quitting the game
    game_close = False  # condition to play again

    x1 = display_width / 2
    y1 = display_height / 2

    y1_change = 0
    x1_change = 0  # updating the pos of the block

    foodx = int(random.randrange(0, display_width-snake_block)/10.0)*10.0
    foody = int(random.randrange(0, display_width-snake_block)/10.0)*10.0
    # foods placement is determined

    while not game_over:  # looping the conditions
        while game_close == True:
            display.fill(white)
            message("You Lost! Press Q-Quit or P-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.hey == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            print(event)
            if (event.type == pygame.QUIT):  # in case the quit button is pressed
                game_over = True
            if (event.type == pygame.KEYDOWN):
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    y1_change = snake_block
                    x1_change = 0
            if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change
            display.fill(white)
            pygame.draw.rect(display, black, [int(x1), int(
                y1), snake_block, snake_block], 0, 2)
            pygame.draw.rect(
                display, blue, [foodx, foody, snake_block, snake_block])
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                print("Yummy!!")

            clock.tick(snake_speed)

    message("You lost", red)
    pygame.display.update()
    time.sleep(t)

    pygame.quit()
    quit()


gameLoop()

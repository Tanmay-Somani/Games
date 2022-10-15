import pygame  # creating the screen for the games
import time  # importing the time module for adding delay in execution time
import random  # importing a module named random for random number generation

pygame.init()  # initializing the show

yellow = (255, 255, 102)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 150, 255)
white = (255, 255, 255)
black = (0, 0, 0)  # colors

show_height = 600
show_width = 400
# setting the mode as to how to show
show = pygame.display.set_mode((show_height, show_width))
pygame.display.update()  # this updates the screen to any changes
# setting the caption for the screen
pygame.display.set_caption("Snake Game v0.45")
snake_block = 10  # block size
snake_speed = 15  # block movement time

clock = pygame.time.Clock()  # clock the current time

# no idea kya error aa/its just the font family name
font_style = pygame.font.SysFont("segoescript", 25)
font_score = pygame.font.SysFont("Monospace", 35)


def Score(score):
    value = font_score.render("Your Score: "+str(score), True, yellow)
    show.blit(value, [0, 0])  # type:none


def snakes(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(show, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mssage = font_style.render(msg, True, color)
    show.blit(mssage, [show_width/6, show_height/3])  # type: ignore


def gameLoop():  # creating a function for the game controls
    game_over = False  # condition for quitting the game
    game_close = False  # condition to play again

    x1 = show_width / 2
    y1 = show_height / 2

    y1_change = 0
    x1_change = 0  # updating the pos of the block

    snake_list = []
    Length_S = 1

    foodx = round(random.randrange(0, show_width-snake_block)/10.0)*10.0
    foody = round(random.randrange(0, show_width-snake_block)/10.0)*10.0

    while not game_over:  # looping the conditions

        while game_close == True:
            show.fill(blue)
            message("You Lost! Press Q-Quit or P-Play Again", red)
            Score(Length_S-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
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

            if x1 >= show_width or x1 < 0 or y1 >= show_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            show.fill(blue)

            pygame.draw.rect(
                show, blue, [foodx, foody, snake_block, snake_block], 0, 4)  # type: ignore

            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)

            if len(snake_list) > Length_S:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            snakes(snake_block, snake_list)
            Score(Length_S-1)
            pygame.display.update()

            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(
                    0, show_width-snake_block)/10.0)*10.0
                foody = round(random.randrange(
                    0, show_width-snake_block)/10.0)*10.0
                Length_S += 1

            clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()

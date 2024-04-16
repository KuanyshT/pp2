import pygame
import random

# Initialize Pygame
pygame.init()

#Sounds
pygame.mixer.music.load("/Users/aiymtursynbekova/Downloads/am-am-am.mp3")

#Images
img_background = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/background.jpeg")
img_apple = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/apple.png")
img_snakeblockcircle = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/graphics_04.png")
img_snakeblocksquare = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/graphics_03.png")
img_closedmouth = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/output-onlinepngtools.png")
img_openedmouth = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/output-onlinepngtools-2.png")

# Set up the screen
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 30
GRID_WIDTH, GRID_HEIGHT = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Set up colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

#Variables
score = 0
tnscore = 5
level = 1
game_speed = 8
font = pygame.font.Font(None, 36)
timer = 100
gameover = False
ifnear = False

# Set up the Snake
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (0, 1)  # Initial direction: down

# Set up the initial food position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Set up the game clock
clock = pygame.time.Clock()

#Function
def restart():
    global game_speed, level, snake, score, tnscore, gameover
    gameover = False
    game_speed = 8
    score = 0
    level = 1
    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    tnscore = 5

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)
    if not gameover:
        # Move the snake
        new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
        snake.insert(0, new_head)
        
        
        #Making harder
        if score == tnscore:
            tnscore += 5
            level += 1
            game_speed += 1
            
        # Check for collisions
        timer -= 1
        if timer != 0:
            if snake[0] == food:
                timer = 100
                pygame.mixer.music.play()
                food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                score += 1
            else:
                snake.pop()
        else:
            snake.pop()
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            timer = 100
        
        if snake[0][0] <= food[0] + 2 and snake[0][0] >= food[0] - 2 and snake[0][1] >= food[1] - 2 and snake[0][1] <= food[1] + 2:
            ifnear = True
        # Check for out of bounds
        if (
            snake[0][0] < 0
            or snake[0][0] >= GRID_WIDTH
            or snake[0][1] < 0
            or snake[0][1] >= GRID_HEIGHT
        ):
            gameover = True
            
        # Check for self-collision
        if len(snake) != len(set(snake)):
            gameover = True

        # Clear the screen
        screen.blit(pygame.transform.scale(img_background, (WIDTH, HEIGHT)), (0, 0))

        # Draw the snake
        for segment in snake:
            screen.blit(pygame.transform.scale(img_snakeblockcircle, (30, 30)), (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE))
            screen.blit(pygame.transform.scale(img_snakeblocksquare, (26, 26)), (segment[0] * GRID_SIZE + 2, segment[1] * GRID_SIZE + 2))
            # pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        if ifnear:
            screen.blit(pygame.transform.scale(img_openedmouth, (30, 30)), (snake[0][0] * GRID_SIZE, snake[0][1] * GRID_SIZE))
        else:
            screen.blit(pygame.transform.scale(img_closedmouth, (30, 30)), (snake[0][0] * GRID_SIZE, snake[0][1] * GRID_SIZE))
        # Draw the food
        screen.blit(pygame.transform.scale(img_apple, (30, 30)), (food[0] * GRID_SIZE, food[1] * GRID_SIZE))
        
        ifnear = False
        
        #Draw scores and level
        score_text = font.render("Score: " + str(score), True, WHITE)
        level_text = font.render("Level: " + str(level), True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (10, 50))
    
    else:
        screen.fill(WHITE)
        gameover_text = font.render("Game over! Press space to restart", True, (0, 0, 0))
        screen.blit(gameover_text, (200, 300))
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            restart()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(game_speed)

# Quit Pygame
pygame.quit()

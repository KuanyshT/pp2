import pygame
import random

# Initialize Pygame
pygame.init()

#Images
img_background = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/background.jpeg")
img_apple = pygame.image.load("/Users/aiymtursynbekova/Desktop/pp2/lab - 8/PygameTutorial_3_0/apple.png")

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

# Set up the Snake
snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_direction = (0, 1)  # Initial direction: down

# Set up the initial food position
food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

# Set up the game clock
clock = pygame.time.Clock()

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
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            score += 1
        else:
            snake.pop()
    else:
        snake.pop()
        food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
        timer = 100

    # Check for out of bounds
    if (
        snake[0][0] < 0
        or snake[0][0] >= GRID_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= GRID_HEIGHT
    ):
        running = False

    # Check for self-collision
    if len(snake) != len(set(snake)):
        running = False

    # Clear the screen
    screen.blit(pygame.transform.scale(img_background, (WIDTH, HEIGHT)), (0, 0))

    # Draw the snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Draw the food
    screen.blit(pygame.transform.scale(img_apple, (30, 30)), (food[0] * GRID_SIZE, food[1] * GRID_SIZE))
    
    #Draw scores and level
    score_text = font.render("Score: " + str(score), True, WHITE)
    level_text = font.render("Level: " + str(level), True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 50))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(game_speed)

# Quit Pygame
pygame.quit()

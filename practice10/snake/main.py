import pygame
import random

pygame.init()

# Screen size
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Levels")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 0, 0)

# Snake settings
block = 20
snake = [(100, 100)]
direction = (block, 0)

# Food
def generate_food():
    while True:
        x = random.randint(0, (WIDTH - block) // block) * block
        y = random.randint(0, (HEIGHT - block) // block) * block

        if (x, y) not in snake:
            return (x, y)

food = generate_food()

# Score & Level
score = 0
level = 1
speed = 8

font = pygame.font.SysFont("Arial", 24)

running = True
while running:
    screen.fill(BLACK)

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # movement control
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, block):
                direction = (0, -block)
            if event.key == pygame.K_DOWN and direction != (0, -block):
                direction = (0, block)
            if event.key == pygame.K_LEFT and direction != (block, 0):
                direction = (-block, 0)
            if event.key == pygame.K_RIGHT and direction != (-block, 0):
                direction = (block, 0)

    # MOVE SNAKE
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])

    # ❌ WALL COLLISION
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT):
        print("Game Over - Wall hit!")
        running = False

    # ❌ SELF COLLISION
    if new_head in snake:
        print("Game Over - Self collision!")
        running = False

    snake.insert(0, new_head)

    # 🍎 FOOD EAT
    if new_head == food:
        score += 1
        food = generate_food()

        # LEVEL SYSTEM
        if score % 3 == 0:
            level += 1
            speed += 2  # increase speed

    else:
        snake.pop()  # remove tail if no food eaten

    # DRAW FOOD
    pygame.draw.rect(screen, RED, (*food, block, block))

    # DRAW SNAKE
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, block, block))

    # SCORE + LEVEL TEXT
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL = 20  

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()


WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)


font = pygame.font.SysFont("Arial", 24)


snake = [(100, 100)]
dx, dy = CELL, 0 


def generate_food():
    """Тамақты snake үстіне түспейтіндей етіп генерациялау"""
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:
            return (x, y)

food = generate_food()

score = 0
level = 1
speed = 10  

running = True
while running:
    screen.fill(WHITE)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -CELL
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, CELL
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -CELL, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = CELL, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)

    if (
        head[0] < 0 or head[0] >= WIDTH or
        head[1] < 0 or head[1] >= HEIGHT
    ):
        print("Game Over: Wall collision")
        running = False

    
    if head in snake:
        print("Game Over: Self collision")
        running = False

    snake.insert(0, head)

    
    if head == food:
        score += 1


        food = generate_food()

        
        if score % 3 == 0:  
            level += 1
            speed += 2  
    else:
        snake.pop()

    
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL, CELL))

    
    pygame.draw.rect(screen, RED, (*food, CELL, CELL))

    
    score_text = font.render(f"Score: {score}", True, BLACK)
    level_text = font.render(f"Level: {level}", True, BLACK)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.flip()
    clock.tick(speed)

pygame.quit()
import pygame
import random

pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game with Coins")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)
RED = (200, 0, 0)
GRAY = (50, 50, 50)

# Player car
car_width = 50
car_height = 80
car_x = WIDTH // 2
car_y = HEIGHT - 120
car_speed = 7

# Coins
coin_radius = 15
coins = []

# Score
score = 0
font = pygame.font.SysFont("Arial", 28)

# Road lines (visual effect)
lines = []
for i in range(10):
    lines.append([WIDTH // 2 - 5, i * 70])

# Function to spawn coin
def spawn_coin():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-600, -50)
    coins.append([x, y])

# spawn initial coins
for _ in range(5):
    spawn_coin()

running = True
while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # KEY CONTROL
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    # ROAD MOVING LINES (animation effect)
    for line in lines:
        line[1] += 8
        if line[1] > HEIGHT:
            line[1] = -50

        pygame.draw.rect(screen, WHITE, (line[0], line[1], 10, 40))

    # CAR DRAW
    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    pygame.draw.rect(screen, RED, car_rect)

    # COINS LOGIC
    for coin in coins[:]:
        coin[1] += 6  # move down

        # draw coin
        pygame.draw.circle(screen, YELLOW, (coin[0], coin[1]), coin_radius)

        # collision with car
        coin_rect = pygame.Rect(coin[0]-15, coin[1]-15, 30, 30)

        if car_rect.colliderect(coin_rect):
            coins.remove(coin)
            score += 1
            spawn_coin()

        # remove if out of screen
        if coin[1] > HEIGHT:
            coins.remove(coin)
            spawn_coin()

    # SCORE DISPLAY (top right)
    text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(text, (WIDTH - 150, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
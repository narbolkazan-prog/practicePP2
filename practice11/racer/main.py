import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game with Coins")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
BLUE = (0, 150, 255)
RED = (255, 50, 50)
GRAY = (50, 50, 50)

car_width = 50
car_height = 80
car_x = WIDTH // 2
car_y = HEIGHT - 120
car_speed = 7

coins = []
coin_radius = 15

score = 0
font = pygame.font.SysFont("Arial", 28)

enemy_speed = 6

lines = []
for i in range(10):
    lines.append([WIDTH // 2 - 5, i * 70])

def spawn_coin():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(-600, -50)
    value = random.choice([1, 3, 5])

    if value == 1:
        color = YELLOW
    elif value == 3:
        color = BLUE
    else:
        color = RED

    coins.append([x, y, value, color])

for _ in range(5):
    spawn_coin()

running = True
while running:
    screen.fill(GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - car_width:
        car_x += car_speed

    for line in lines:
        line[1] += enemy_speed
        if line[1] > HEIGHT:
            line[1] = -50
        pygame.draw.rect(screen, WHITE, (line[0], line[1], 10, 40))

    car_rect = pygame.Rect(car_x, car_y, car_width, car_height)
    pygame.draw.rect(screen, (200, 0, 0), car_rect)

    for coin in coins[:]:
        coin[1] += enemy_speed
        x, y, value, color = coin

        pygame.draw.circle(screen, color, (x, y), coin_radius)

        coin_rect = pygame.Rect(x-15, y-15, 30, 30)

        if car_rect.colliderect(coin_rect):
            coins.remove(coin)
            score += value
            spawn_coin()

            if score % 5 == 0:
                enemy_speed += 1

        if y > HEIGHT:
            coins.remove(coin)
            spawn_coin()

    text = font.render(f"Coins: {score}", True, WHITE)
    screen.blit(text, (WIDTH - 170, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
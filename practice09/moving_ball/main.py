import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Control Ball Game")

clock = pygame.time.Clock()

# Player
x = 100
y = 300
radius = 25

vel_y = 0
gravity = 1
jump_power = -15

ground_y = 350

# obstacles
obstacles = []

def create_obstacle(x_pos):
    w = random.randint(30, 60)
    h = random.randint(40, 90)
    return pygame.Rect(x_pos, ground_y - h, w, h)

# start obstacles
for i in range(6):
    obstacles.append(create_obstacle(500 + i * 200))

running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if y >= ground_y - radius:
                    vel_y = jump_power

    # movement (PLAYER CONTROLLED)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= 7   # артқа
    if keys[pygame.K_RIGHT]:
        x += 7   # алға

    # gravity
    vel_y += gravity
    y += vel_y

    # ground collision
    if y > ground_y - radius:
        y = ground_y - radius
        vel_y = 0

    # move obstacles LEFT (world effect)
    for obs in obstacles:
        obs.x -= 4

    # remove old + add new
    if obstacles[0].right < 0:
        obstacles.pop(0)
        new_x = obstacles[-1].x + random.randint(150, 300)
        obstacles.append(create_obstacle(new_x))

    # draw ground
    pygame.draw.line(screen, (0, 0, 0), (0, ground_y), (WIDTH, ground_y), 3)

    # draw obstacles
    for obs in obstacles:
        pygame.draw.rect(screen, (0, 0, 0), obs)

    # player
    player_rect = pygame.Rect(x - radius, y - radius, radius*2, radius*2)
    pygame.draw.circle(screen, (255, 0, 0), (x, int(y)), radius)

    # collision
    for obs in obstacles:
        if player_rect.colliderect(obs):
            print("GAME OVER")
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
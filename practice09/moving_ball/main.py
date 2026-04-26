import pygame
from ball import Ball

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

clock = pygame.time.Clock()

ball = Ball(WIDTH, HEIGHT)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # keyboard input
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        ball.move(0, -20)
    if keys[pygame.K_DOWN]:
        ball.move(0, 20)
    if keys[pygame.K_LEFT]:
        ball.move(-20, 0)
    if keys[pygame.K_RIGHT]:
        ball.move(20, 0)

    screen.fill((255, 255, 255))

    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
import pygame
import os
from clock import MickeyClock

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey's Clock")

clock = pygame.time.Clock()


BASE_DIR = os.path.dirname(__file__)
image_path = os.path.join(BASE_DIR, "image", "mickey_hand.png")

mickey_clock = MickeyClock(screen, image_path)

running = True
while running:
    screen.fill((255, 255, 255))  # background

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    mickey_clock.draw()

    pygame.display.flip()
    clock.tick(1)  # update every second

pygame.quit()

import pygame
import os
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont("Arial", 24)

BASE_DIR = os.path.dirname(__file__)

playlist = [
    os.path.join(BASE_DIR, "music", "track1.mp3"),
    os.path.join(BASE_DIR, "music", "track2.mp3")
]

player = MusicPlayer(playlist)

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            if event.key == pygame.K_s:
                player.stop()

            if event.key == pygame.K_n:
                player.next()

            if event.key == pygame.K_b:
                player.prev()

            if event.key == pygame.K_q:
                running = False

    # UI TEXT
    title = font.render("Music Player", True, (255, 255, 255))
    track = font.render("Track: " + player.get_track_name(), True, (0, 255, 0))

    controls = font.render("P=Play S=Stop N=Next B=Prev Q=Quit", True, (200, 200, 200))

    screen.blit(title, (20, 20))
    screen.blit(track, (20, 80))
    screen.blit(controls, (20, 140))

    pygame.display.flip()

pygame.quit()
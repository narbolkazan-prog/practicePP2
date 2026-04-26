import pygame
from player import MusicPlayer
import os


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("K-Board Music Player")
font = pygame.font.SysFont("Arial", 24)
clock = pygame.time.Clock()


music_path = os.path.join(os.path.dirname(__file__), 'music')
player = MusicPlayer(music_path)

running = True
while running:
    screen.fill((30, 30, 30))
    
    # Отображение информации
    track_text = font.render(f"Now Playing: {player.get_current_track()}", True, (255, 255, 255))
    controls_text = font.render("P: Play | S: Stop | N: Next | B: Back | Q: Quit", True, (150, 150, 150))
    
    screen.blit(track_text, (50, 150))
    screen.blit(controls_text, (50, 250))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()
            elif event.key == pygame.K_s:
                player.stop()
            elif event.key == pygame.K_n:
                player.next_track()
            elif event.key == pygame.K_b:
                player.prev_track()
            elif event.key == pygame.K_q:
                running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
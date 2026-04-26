import pygame
import sys
import math

pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Paint")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

colors = [BLACK, RED, GREEN, BLUE]
current_color = BLACK


tool = "brush"

drawing = False
start_pos = (0, 0)

screen.fill(WHITE)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():

    
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
        if event.type == pygame.KEYDOWN:

        
            if event.key == pygame.K_b:
                tool = "brush"
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "triangle"
            elif event.key == pygame.K_e:
                tool = "equilateral"
            elif event.key == pygame.K_r:
                tool = "rhombus"

    
            elif event.key == pygame.K_1:
                current_color = colors[0]
            elif event.key == pygame.K_2:
                current_color = colors[1]
            elif event.key == pygame.K_3:
                current_color = colors[2]
            elif event.key == pygame.K_4:
                current_color = colors[3]

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            start_pos = event.pos

        
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            x1, y1 = start_pos
            x2, y2 = end_pos

            
            if tool == "square":
                side = min(abs(x2 - x1), abs(y2 - y1))
                rect = pygame.Rect(x1, y1, side, side)
                pygame.draw.rect(screen, current_color, rect, 2)

            
            elif tool == "triangle":
                points = [(x1, y1), (x2, y2), (x1, y2)]
                pygame.draw.polygon(screen, current_color, points, 2)

            
            elif tool == "equilateral":
                side = abs(x2 - x1)
                height = side * math.sqrt(3) / 2

                p1 = (x1, y1)
                p2 = (x1 + side, y1)
                p3 = (x1 + side // 2, y1 - height)

                pygame.draw.polygon(screen, current_color, [p1, p2, p3], 2)

    
            elif tool == "rhombus":
                center_x = (x1 + x2) // 2
                center_y = (y1 + y2) // 2

                dx = abs(x2 - x1) // 2
                dy = abs(y2 - y1) // 2

                points = [
                    (center_x, center_y - dy),
                    (center_x + dx, center_y),
                    (center_x, center_y + dy),
                    (center_x - dx, center_y)
                ]
                pygame.draw.polygon(screen, current_color, points, 2)

        
        if event.type == pygame.MOUSEMOTION and drawing:
            if tool == "brush":
                pygame.draw.circle(screen, current_color, event.pos, 3)

    pygame.display.flip()
    clock.tick(60)
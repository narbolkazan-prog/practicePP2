import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

clock = pygame.time.Clock()

# Canvas
canvas = pygame.Surface((WIDTH, HEIGHT))
canvas.fill((255, 255, 255))

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

current_color = BLACK
tool = "brush"

start_pos = None
drawing = False

font = pygame.font.SysFont("Arial", 20)

running = True
while running:
    screen.fill((200, 200, 200))
    screen.blit(canvas, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEY CONTROLS (tools)
        if event.type == pygame.KEYDOWN:

            # Tools
            if event.key == pygame.K_b:
                tool = "brush"
            if event.key == pygame.K_r:
                tool = "rectangle"
            if event.key == pygame.K_c:
                tool = "circle"
            if event.key == pygame.K_e:
                tool = "eraser"

            # Colors
            if event.key == pygame.K_1:
                current_color = BLACK
            if event.key == pygame.K_2:
                current_color = RED
            if event.key == pygame.K_3:
                current_color = GREEN
            if event.key == pygame.K_4:
                current_color = BLUE

        # Mouse press
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos
            drawing = True

        # Mouse release
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = event.pos
            drawing = False

            # RECTANGLE
            if tool == "rectangle":
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                w = abs(start_pos[0] - end_pos[0])
                h = abs(start_pos[1] - end_pos[1])
                pygame.draw.rect(canvas, current_color, (x, y, w, h), 2)

            # CIRCLE
            if tool == "circle":
                radius = int(((end_pos[0]-start_pos[0])**2 + (end_pos[1]-start_pos[1])**2) ** 0.5)
                pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

    # BRUSH / ERASER (hold mouse)
    if drawing:
        mouse = pygame.mouse.get_pos()

        if tool == "brush":
            pygame.draw.circle(canvas, current_color, mouse, 5)

        if tool == "eraser":
            pygame.draw.circle(canvas, WHITE, mouse, 20)

    # UI TEXT
    text = font.render(f"Tool: {tool} | Colors: 1-black 2-red 3-green 4-blue", True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
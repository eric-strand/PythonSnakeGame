import pygame

# Fönster höjd,bredd och färger

WINDOW_HEIGHT = 640
WINDOW_WIDTH = 640

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.draw.circle(screen,(255,0,0),(320,320),10)
    pygame.display.update()
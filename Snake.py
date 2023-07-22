import pygame

# Fönster höjd,bredd och färger

WINDOW_HEIGHT = 640
WINDOW_WIDTH = 640
BLOCK_SIZE = 32

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class Snake:
    def __init__(self):
        self.body = [(40,40),(40,60),(40,80)]
        self.size = (20,20)
        self.direction = 1
    
    def draw(self,screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0,255,0),(segment[0],segment[1], BLOCK_SIZE, BLOCK_SIZE))
    
    def move(self):
        for segment in self.body:


running = True
snake = Snake()
while running:
    # Close game window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    snake.draw(screen)
    pygame.display.update()
import pygame
import random


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
















class Food:
    def __init__(self):
        self.surface = screen

    def spawn_food(self):
        x = random.randint(10, WINDOW_WIDTH - 10)
        y = random.randint(10, WINDOW_HEIGHT - 10)
        
        position = (x,y) 
        
        pygame.draw.circle(self.surface, "WHITE", position, 10, 10)
   
    



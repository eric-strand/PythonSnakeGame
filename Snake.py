import pygame
import random


WINDOW_HEIGHT = 640
WINDOW_WIDTH = 640
BLOCK_SIZE = 32

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class Snake:
    def __init__(self):
        self.body = [(40,80),(40,60),(40,40)]
        self.size = (20,20)
        self.direction = 1
    
    def draw(self,screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0,255,0),(segment[0],segment[1], BLOCK_SIZE, BLOCK_SIZE))
    
    def move(self):
        temp_list = []
        for segment in self.body:
            temp_list.append((segment[0],segment[1]+BLOCK_SIZE))
        self.body = temp_list


class Food:
    def __init__(self):
        self.surface = screen

    def spawn_food(self, snake_head):
        if snake_head > 300:
            x = random.randint(10, WINDOW_WIDTH - 10)
            y = random.randint(10, WINDOW_HEIGHT - 10)
            
            position = (x,y) 
        else:
            position = (100,300)
        
        pygame.draw.circle(self.surface, "WHITE", position, 10, 10)


running = True
snake = Snake()
food = Food()

while running:
    # Close game window
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #pygame.draw.circle(screen,(255,0,0),(320,320),10)
    #food.spawn_food()
    screen.fill((0,0,0))
    food.spawn_food(snake.body[0][1])
    snake.draw(screen)
    snake.move()
    pygame.display.update()


   
    


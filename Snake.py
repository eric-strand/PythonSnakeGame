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
    def __init__(self, position):
        self.surface = screen
        self.position = position

    def spawn_food(self):
        pygame.draw.circle(self.surface, "WHITE", self.position, 10, 10)

    def get_position(self):
        return self.position
    



running = True
snake = Snake()
food = Food((100,100))

while running:
    # Close game window
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #pygame.draw.circle(screen,(255,0,0),(320,320),10)
    #food.spawn_food()
    screen.fill((0,0,0))
    
    snake_head_x = snake.body[0][0]
    snake_head_y = snake.body[0][1]
    
    food.spawn_food()
    food_position = food.get_position()
    snake.draw(screen)
    snake.move()

    if(snake_head_x == food_position[0] and snake_head_y == food_position[1]):
        food.position = (random.randint(0, WINDOW_WIDTH - 10), random.randint(0, WINDOW_HEIGHT - 10))
    pygame.display.update()


   
    


import pygame
import random


WINDOW_HEIGHT = 640
WINDOW_WIDTH = 640
BLOCK_SIZE = 32

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class Snake:
    def __init__(self):
        self.body = [(0,0),(32,0)]
        self.lenght = 1
        self.size = (20,20)
        self.direction = "Still"
    
    def add_tail(self):
        self.lenght += 1

    def draw(self,screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0,255,0),(segment[0],segment[1], BLOCK_SIZE, BLOCK_SIZE))
    
    def move(self):
        snake_head = self.body[0]
        if self.direction == "Left":
            self.body = [(snake_head[0]-BLOCK_SIZE, snake_head[1])] + self.body
        if self.direction == "Right":
            self.body = [(snake_head[0]+BLOCK_SIZE, snake_head[1])] + self.body
        if self.direction == "Up":
            self.body = [(snake_head[0],snake_head[1] - BLOCK_SIZE)] + self.body
        if self.direction == "Down":
            self.body = [(snake_head[0],snake_head[1] + BLOCK_SIZE)] + self.body
        if self.lenght < len(self.body):
            self.body.pop()
        



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
    #food.spawn_food(snake.body[0][1])
    snake.draw(screen)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        snake.direction = "Left"
    if key[pygame.K_RIGHT]:
        snake.direction = "Right"
    if key[pygame.K_UP]:
        snake.direction = "Up"
    if key[pygame.K_DOWN]:
        snake.direction = "Down"
    snake.move()
    pygame.display.update()


   
    


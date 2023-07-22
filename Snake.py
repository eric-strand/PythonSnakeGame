import pygame
import random


WINDOW_HEIGHT = 640
WINDOW_WIDTH = 640
BLOCK_SIZE = 32

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class Snake:
    def __init__(self):
        self.body = [(320,320)]
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
    
    screen.fill((0,0,0))
    
    snake_head_x = snake.body[0][0]
    snake_head_y = snake.body[0][1]
    
    food.spawn_food()
    food_position = food.get_position()
<<<<<<< HEAD
=======
    
    if(snake_head_x == food_position[0] and snake_head_y == food_position[1]):
        food.position = (random.randint(0, WINDOW_WIDTH - 10), random.randint(0, WINDOW_HEIGHT - 10))
    
>>>>>>> 19ff9d432283a0f5127cf57beff2745b7350ad43
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
    if key[pygame.K_l]:
        snake.lenght +=1
    snake.move()

    pygame.display.update()


   
    


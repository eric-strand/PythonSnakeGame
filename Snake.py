import pygame
import random

pygame.init()
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 800
BLOCK_SIZE = 40

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

class Snake:
    def __init__(self):
        self.body = [(400,120),(400,80)]
        self.lenght = 2
        self.direction = "Down"
    
    def add_tail(self):
        self.lenght += 1

    def draw(self,screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0,255,0),(segment[0],segment[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(screen, (255,0,0),(segment[0]+2,segment[1]+2, BLOCK_SIZE-4, BLOCK_SIZE-4))
    
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
        if self.body[0] in self.body[1:]:
            self.reset()
        if self.lenght < len(self.body):
            self.body.pop()
    
    
    def reset(self):
        self.body = [(400,120),(400,80)]
        self.lenght = 2
        self.direction = "Down"
        
class Mat:
    def __init__(self):
        self.position = [300,300]
        self.color = (255,0,0)
        self.y = []
        for i in range(20):
            self.y.append(i*40)

    def draw(self,screen):
        if self.position:
            pygame.draw.circle(screen, self.color,(self.position[0]+20,self.position[1]+20),20)

    def spawn_new(self, snake_body):
        x = random.choice(self.y)
        y = random.choice(self.y)
        if (x, y) in snake_body:
            self.spawn_new(snake_body)
        else:
            self.position = [x, y]



class Food:
    def __init__(self, position):
        self.surface = screen
        self.position = position

    def spawn_food(self):
        pygame.draw.circle(self.surface, "WHITE", self.position, 10, 10)

    def get_position(self):
        return self.position
    

text_font = pygame.font.SysFont("Arial", 50)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img,(x, y))

running = True
snake = Snake()
food = Food((100,100))
mat = Mat()
mat.spawn_new(snake.body)

while running:
    # Close game window
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,0,0))
    
    draw_text(f"Score: {snake.lenght-2}",text_font,(0,255,0),320,0)
    """
    snake_head_x = snake.body[0][0]
    snake_head_y = snake.body[0][1]
    
    food.spawn_food()
    food_position = food.get_position()
    
    if(snake_head_x == food_position[0] and snake_head_y == food_position[1]):
        food.position = (random.randint(0, WINDOW_WIDTH - 10), random.randint(0, WINDOW_HEIGHT - 10))"""
    
    snake.draw(screen)
    mat.draw(screen)
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and snake.direction != "Right":
        snake.direction = "Left"
    if key[pygame.K_RIGHT] and snake.direction != "Left":
        snake.direction = "Right"
    if key[pygame.K_UP] and snake.direction != "Down":
        snake.direction = "Up"
    if key[pygame.K_DOWN] and snake.direction != "Up":
        snake.direction = "Down"
    if (snake.body[0][0] == mat.position[0]) and (snake.body[0][1] == mat.position[1]):
        mat.spawn_new(snake.body)
        snake.lenght +=1
    
    if (snake.body[0][0] >= WINDOW_HEIGHT) or (snake.body[0][0] < 0) or (snake.body[0][1] >= WINDOW_WIDTH) or (snake.body[0][1] < 0) :
        snake.reset()
        mat.spawn_new(snake.body)
    snake.move()

    pygame.display.update()


   
    


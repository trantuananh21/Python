import pygame
import random

# KHOI TAO GAME
pygame.init()

# CAI DAT MAN HINH
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game tre con')

# MAU SAC
white = (255, 255, 255)
green = (0, 256, 0)
red = (255, 0, 0)

# TOC DO KHUNG HINH
clock = pygame.time.Clock()
fps =   10

# Khoi tao Snake
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Khoi tao thuc an
food_pos = [random.randrange(1, (width/10) * 10), random.randrange(1, (height/10) * 10)]
food_spawn = True

# Khoi tao huong di chuyen ban dau
direction = 'RIGHT'
change_to = direction

# Ham ve Snake
def draw_snake(screen, snake_body):
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

# Ham ve Thuc an
def draw_food(screen, food_pos):
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

# Vong lap chinh
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYDOWN:
            if event.type == pygame.K_UP:
                change_to == 'UP'
            if event.type == pygame.K_DOWN:
                change_to == 'DOWN'
            if event.type == pygame.K_LEFT:
                change_to == 'LEFT'
            if event.type == pygame.K_RIGHT:
                change_to == 'RIGHT'

# Dieu kien nguoc huong di chuyen
    if change_to == 'UP' and not direction == 'DOWN':
        direction == 'UP'
    if change_to == 'DOWN' and not direction == 'UP':
        direction == 'DOWN'
    if change_to == 'RIGHT' and not direction == 'LEFT':
        direction == 'RIGHT'
    if change_to == 'LEFT' and not direction == 'RIGHT':
        direction == 'LEFT'

    # Cap nhat vi tri snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    
    # Tao thuc an moi khi snake an thuc an
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        food_spawn = False
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_pos = [random.randrange(width/10) * 10, random.randrange(height/10) * 10]
    food_spawn = True

    # Ve man hinh choi
    screen.fill(white)
    draw_snake(screen, snake_body)
    draw_food(screen, food_pos)

    # Cap nhat man hinh
    pygame.display.update()
    clock.tick(fps)

# Dong cua so khi thoat vong lap
pygame.quit()
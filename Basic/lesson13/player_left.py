import constants
import pygame

position = [
    50,
    constants.WINDOW_HEIGHT // 2 - constants.WINDOW_HEIGHT // 2,
    constants.PADDLE_HEIGHT,
    constants.PADDLE_WIDTH,
]

velocity = 10

def move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        position[1] -= velocity
    elif keys[pygame.K_w]:
        position[1] += velocity

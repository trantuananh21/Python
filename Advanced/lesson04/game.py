import pygame
import random
import sys

pygame.init()
#RAN SAN MOI 
#MINDX_GV.TRANVIETTRUONG
# Cài Đặt màn hình
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Rắn săn mồi")
# Màu sắc
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Khởi tạo rắn và mồi
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_dir = "RIGHT"
change_to = snake_dir

food_pos = [random.randrange(1, (width//10)) * 10,
            random.randrange(1, (height//10)) * 10]
food_spawn = True

# Khởi tạo điểm
score = 0
# Thêm biến cho thông báo thua
game_over = False
# Vòng lặp chính
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
# Xử lý phím nhấn
        keys = pygame.key.get_pressed()
        for key in keys:
            if keys[pygame.K_UP]:
                change_to = "UP"
            if keys[pygame.K_DOWN]:
                change_to = "DOWN"
            if keys[pygame.K_LEFT]:
                change_to = "LEFT"
            if keys[pygame.K_RIGHT]:
                change_to = "RIGHT"
# Xác định hướng mới của rắn
    if change_to == "UP" and not snake_dir == "DOWN":
        snake_dir = "UP"
    if change_to == "DOWN" and not snake_dir == "UP":
        snake_dir = "DOWN"
    if change_to == "LEFT" and not snake_dir == "RIGHT":
        snake_dir = "LEFT"
    if change_to == "RIGHT" and not snake_dir == "LEFT":
        snake_dir = "RIGHT"
# Di chuyển rắn theo hướng
    if snake_dir == "UP":
        snake_pos[1] -= 10
    if snake_dir == "DOWN":
        snake_pos[1] += 10
    if snake_dir == "LEFT":
        snake_pos[0] -= 10
    if snake_dir == "RIGHT":
        snake_pos[0] += 10
# Tạo điều kiện thua
    if (
        snake_pos[0] < 0
        or snake_pos[0] >= width
        or snake_pos[1] < 0
        or snake_pos[1] >= height
    ):
        game_over = True
# Thêm phần tử đầu tiên của rắn vào snake_body
    snake_body.insert(0, list(snake_pos))
# Kiểm tra va chạm với mồi
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10,
                    random.randrange(1, (height//10)) * 10]
        food_spawn = True
# Cập nhật màn hình
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, white, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))
# Hiển thị điểm
    font = pygame.font.Font(None, 36)
    text = font.render("SCORE: " + str(score), True, white)
    screen.blit(text, (10, 10))

    pygame.display.update()

    pygame.time.Clock().tick(15)  # Điều chỉnh tốc độ của trò chơi
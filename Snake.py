import pygame
import random
import os
# import sys

def snake_move():
    for s in range(len(snake_segments)-1,0,-1):
        snake_segments[s][1] = snake_segments[s-1][1]
        snake_segments[s][2] = snake_segments[s-1][2]
    snake_segments[0][1] = snake_x
    snake_segments[0][2] = snake_y

def snake_add_segment(x, y):
    snake_segments.insert(0, snake_head.copy())
    snake_segments[0][1] = x
    snake_segments[0][2] = y
    snake_segments[1][0] = SEGMENT_COLOR

def display_snake():
    for segment in snake_segments:
                    #   -x-, RGFB-color,     X      ,    Y      ,  size,    size
        pygame.draw.rect(screen, segment[0], (segment[1], segment[2], SIZE_X, SIZE_Y))

def generate_food():
    generate = True
    while generate:
        x = random.randint(0 , BORDER_X // SIZE_X -1) * SIZE_X
        y = random.randint(0 , BORDER_Y // SIZE_Y - 1) * SIZE_Y
        for segment in snake_segments:
            if segment[1] != x and segment[2] != y: 
                generate = False
    return [FOOD_COLOR, x, y]

def dispaly_food():
    pygame.draw.rect(screen, food[0], (food[1], food[2], SIZE_X, SIZE_Y))

def check_arrea(direction):
    direction = direction.upper()
    if direction in "U":
        if snake_y - SIZE_Y >= 0: return True
    if direction in "D":
        if snake_y + SIZE_Y <= BORDER_Y - SIZE_Y: return True
    if direction in "L":
        if snake_x - SIZE_X >= 0: return True
    if direction in "R":
        if snake_x + SIZE_X <= BORDER_X - SIZE_X: return True
    return False        

def check_next_arrea(direction):
    global food
    global food_couter
    global snake_x
    global snake_y
    direction = direction.upper()
    if direction in "U":
        x = snake_x
        y = snake_y - SIZE_Y
    if direction in "D":
        x = snake_x
        y = snake_y + SIZE_Y
    if direction in "L":
        x = snake_x - SIZE_X
        y = snake_y
    if direction in "R":
        x = snake_x + SIZE_X
        y = snake_y
    if food[1] == x and food[2] == y:
        x = food[1]
        y = food[2]
        del food[:]
        food = generate_food().copy()
        food_couter += 1
        print(f"Your score is: {food_couter} point", end ="")
        if food_couter == 1:
            print()
        else:
            print("s")
        snake_add_segment(x, y)
        snake_x = x
        snake_y = y
        return False
    for i in range(len(snake_segments)-1):
        if snake_segments[i][1] == x and snake_segments[i][2] == y:
            return False
    return check_arrea(direction)

os.system("cls")

SEGMENT_SIZE = 15
SIZE_X = SIZE_Y = SEGMENT_SIZE    
HEAD_COLOR = (255, 0, 0)
SEGMENT_COLOR = (0, 0, 255)
FOOD_COLOR = (255,0,255)

LIGHT_GREEN = (199, 240, 216)
DARK_GREEN = (67, 82, 61)

BORDER_X = 500
BORDER_Y = 500

factor = BORDER_X // SIZE_X
DISPLAY_WIDTH = factor * SIZE_X
factor -= 1
snake_x = (random.randint(0 , factor) - 3) * SIZE_X

factor = BORDER_Y // SIZE_Y
DISPLAY_HIGHT = factor * SIZE_Y
factor -= 1
snake_y = (random.randint(0 , factor) - 3) * SIZE_Y    

DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HIGHT)

pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()

snake_head = [HEAD_COLOR, snake_x, snake_y]
snake_segment = [SEGMENT_COLOR, snake_x + SIZE_X, snake_y]
snake_tail = [LIGHT_GREEN, snake_x + 2 * SIZE_X, snake_y]

snake_segments = []
snake_segments.append(snake_head.copy())
snake_segments.append(snake_segment.copy())
snake_segments.append(snake_tail.copy())

screen.fill(LIGHT_GREEN)

food_couter = 0
food = []
food = generate_food().copy()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dispaly_food()
    display_snake()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if check_next_arrea("L"):                 # L - Left
            snake_x -= SIZE_X
            snake_move()
    elif keys[pygame.K_RIGHT]:
        if check_next_arrea("R"):                 # R - Right
            snake_x += SIZE_X
            snake_move()
    elif keys[pygame.K_UP]:
        if check_next_arrea("U"):                 # U - Up
            snake_y -= SIZE_Y
            snake_move()
    elif keys[pygame.K_DOWN]:
        if check_next_arrea("D"):                 # D - Down
            snake_y += SIZE_Y
            snake_move()
    elif keys[pygame.K_ESCAPE]:
        break

    pygame.display.flip()
    clock.tick(30)
pygame.quit()
# sys.exit()

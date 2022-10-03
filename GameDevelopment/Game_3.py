import pygame
pygame.init()

WIDTH = 1000
HEIGHT = 500
SIZE = WIDTH, HEIGHT
SCREEN = pygame.display.set_mode(SIZE)

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

rect_x = 0
rect_y = 0
rect_w = 50
rect_h = 50

SPEED = 0.5

moveX = 0
moveY = 0

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()       # will quit pygame
            quit()              # will quit python

        # if we are going to press a key
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = SPEED
                moveY = 0
            elif event.key == pygame.K_LEFT:
                moveX = -SPEED
                moveY = 0
            elif event.key == pygame.K_DOWN:
                moveY = SPEED
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -SPEED
                moveX = 0
        # else:
        #     moveX = 0

    SCREEN.fill(WHITE)

    # screen/surface, color, [x,y,w,h]
    pygame.draw.rect(SCREEN, RED, [rect_x, rect_y, rect_w, rect_h])
    rect_x += moveX
    rect_y += moveY

    # if rect_x > WIDTH - rect_w:
    #     moveX = -SPEED
    # elif rect_x < 0:
    #     moveX = SPEED
    #
    # if rect_y > HEIGHT - rect_h:
    #     moveY = -SPEED
    # elif rect_y < 0:
    #     moveY = SPEED

    if rect_x > WIDTH:
        rect_x = -50
    elif rect_x < -50:
        rect_x = WIDTH

    if rect_y > HEIGHT:
        rect_y = -50
    elif rect_y < -50:
        rect_y = HEIGHT

    # if rect_y > HEIGHT - rect_h:
    #     moveY = -SPEED
    # elif rect_y < 0:
    #     moveY = SPEED

    pygame.display.flip()
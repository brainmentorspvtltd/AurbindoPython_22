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

moveX = SPEED
moveY = SPEED

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()       # will quit pygame
            quit()              # will quit python

    SCREEN.fill(WHITE)

    # screen/surface, color, [x,y,w,h]
    pygame.draw.rect(SCREEN, RED, [rect_x, rect_y, rect_w, rect_h])
    rect_x += moveX
    # rect_y += moveY

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

    # if rect_y > HEIGHT - rect_h:
    #     moveY = -SPEED
    # elif rect_y < 0:
    #     moveY = SPEED

    pygame.display.flip()
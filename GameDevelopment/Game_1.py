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

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()       # will quit pygame
            quit()              # will quit python

    SCREEN.fill(WHITE)

    # screen/surface, color, [x,y,w,h]
    pygame.draw.rect(SCREEN, RED, [0, 0, 50, 50])
    pygame.draw.rect(SCREEN, RED, [100, 100, 50, 50])
    pygame.draw.rect(SCREEN, RED, [200, 200, 50, 50])

    # screen/surface, color, [x,y], radius
    pygame.draw.circle(SCREEN, BLUE, [400,100], 60)

    pygame.display.flip()
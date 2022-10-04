import pygame
import random
pygame.init()

WIDTH = 1200
HEIGHT = 600
SIZE = WIDTH, HEIGHT
SCREEN = pygame.display.set_mode(SIZE)

WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
BLACK = (0,0,0)

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        # self.SPEED = random.random()
        self.moveX = random.random()
        self.moveY = random.random()
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))

    def update(self):
        self.x += self.moveX
        self.y += self.moveY

        if self.x > WIDTH - 50:
            self.moveX = -random.random()
        elif self.x < 50:
            self.moveX = random.random()

        if self.y > HEIGHT - 50:
            self.moveY = -random.random()
        elif self.y < 50:
            self.moveY = random.random()


# ball_1 = Ball()
# ball_2 = Ball()

# print(ball_1.x)

num = 100
ballsList = []
for i in range(num):
    ball = Ball()
    ballsList.append(ball)

while True:

    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()       # will quit pygame
            quit()              # will quit python

    SCREEN.fill(WHITE)

    # screen/surface, color, [x,y,w,h]
    # pygame.draw.circle(SCREEN, RED, [ball_1.x, ball_1.y], 50)
    # pygame.draw.circle(SCREEN, RED, [ball_2.x, ball_2.y], 50)

    # ball_1.update()
    # ball_2.update()

    for i in range(len(ballsList)):
        pygame.draw.circle(SCREEN, ballsList[i].color, [ballsList[i].x, ballsList[i].y], 50)
        ballsList[i].update()

    pygame.display.flip()
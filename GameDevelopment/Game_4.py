import pygame
import random
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

rect_w = 50
rect_h = 50

bg_img = pygame.image.load("bg_img.jpg")
bg_img = pygame.transform.scale(bg_img, [WIDTH,HEIGHT])

bg_music = pygame.mixer.Sound("music_1.wav")
bg_music.play()

def homeScreen():
    font = pygame.font.SysFont(None, 100)
    text = font.render("Welcome to Snake Game", True, WHITE)

    font_2 = pygame.font.SysFont(None, 70)
    text_2 = font_2.render("Press SPACE to Start Game", True, WHITE)

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()  # will quit pygame
                quit()  # will quit python

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game()

        SCREEN.blit(bg_img, (0,0))

        SCREEN.blit(text, (100, 100))
        SCREEN.blit(text_2, (150, 200))
        pygame.display.flip()


def gameOver():
    font = pygame.font.SysFont(None, 100)
    text = font.render("Game Over...", True, BLACK)

    while True:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()  # will quit pygame
                quit()  # will quit python

        SCREEN.blit(text, (100,100))
        pygame.display.flip()

def score(counter):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score : {}".format(counter), True, BLACK)
    SCREEN.blit(text, (100, 10))

def drawSnake(snakeList):
    for i in range(len(snakeList)):
        pygame.draw.rect(SCREEN, RED, [snakeList[i][0], snakeList[i][1], rect_w, rect_h])

def game():
    counter = 0
    rect_x = 0
    rect_y = 0

    SPEED = 2

    moveX = 0
    moveY = 0

    frogImg = pygame.image.load("frog.png")
    frog_w = frogImg.get_width()
    frog_h = frogImg.get_height()

    frog_x = random.randint(0, WIDTH - frog_w)
    frog_y = random.randint(0, HEIGHT - frog_h)

    snakeLength = 1
    snakeList = []

    FPS = 100
    clock = pygame.time.Clock()

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

        SCREEN.fill(WHITE)
        # SCREEN.blit(bg_img, (0, 0))
        SCREEN.blit(frogImg, (frog_x, frog_y))
        frog_rect = pygame.Rect(frog_x, frog_y, frog_w, frog_w)
        snake_rect = pygame.draw.rect(SCREEN, RED, [rect_x, rect_y, rect_w, rect_h])
        rect_x += moveX
        rect_y += moveY

        if rect_x > WIDTH:
            rect_x = -50
        elif rect_x < -50:
            rect_x = WIDTH

        if rect_y > HEIGHT:
            rect_y = -50
        elif rect_y < -50:
            rect_y = HEIGHT

        snakeHead = []
        snakeHead.append(rect_x)
        snakeHead.append(rect_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        drawSnake(snakeList)

        if snake_rect.colliderect(frog_rect):
            frog_x = random.randint(0, WIDTH - frog_w)
            frog_y = random.randint(0, HEIGHT - frog_h)
            snakeLength += 10
            FPS += 20
            counter += 1

        for each in snakeList[:-1]:
            if each == snakeList[-1]:
                gameOver()

        score(counter)

        pygame.display.flip()
        clock.tick(FPS)

# game()
homeScreen()
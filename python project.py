
import pygame
import sys

pygame.init()

ROWS = 4
COLS = 4
CELL_SIZE = 100
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4x4 Grid Example")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW =
GREEN = 
BLUE = 
PURPLE = 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    for row in range(ROWS + 1):
        pygame.draw.line(screen, BLACK, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), 2)

    for col in range(COLS + 1):
        pygame.draw.line(screen, BLACK, (col * CELL_SIZE, 0), (col * CELL_SIZE, HEIGHT), 2)

    pygame.display.flip()

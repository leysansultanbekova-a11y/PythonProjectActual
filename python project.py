
import pygame
import sys

pygame.init()

ROWS = 4
COLS = 4
CELL_SIZE = 200
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Connecting 4x4")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

font = pygame.font.SysFont("Arial", 48)

categories = [
    ["aid", "responder", "nation", "lady"]
    ["popularity", "beauty", "staring", "contest"]
    ["Dre", "Oz", "Pepper", "Seuss"]
    ["Cope", "Wars", "Luxe", "Brat" ]
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    text = "hello", 

    screen.fill(WHITE)

    for row in range(ROWS + 1):
        pygame.draw.line(screen, BLACK, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), 2)

    for col in range(COLS + 1):
        pygame.draw.line(screen, BLACK, (col * CELL_SIZE, 0), (col * CELL_SIZE, HEIGHT), 2)

    pygame.display.flip()

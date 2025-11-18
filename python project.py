
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

font = pygame.font.SysFont("Arial", 36)

words = [
    ["aid", "responder", "lady", "nation"],
    ["staring", "beauty", "popularity", "talent"],
    ["Dre", "Oz", "Pepper", "Seuss"],
    ["Wars", "Luxe", "Brat", "Cope"]
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    text = "hello", 

    screen.fill(WHITE)

    for row in range(ROWS + 1):
        for col in range(COLS + 1):
            rectangle = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rectangle, 2)

            text_surface = font.render(words[row-1][col-1], True, BLACK)

            text_rectangle = text_surface.get_rect( 
            center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
            )
            screen.blit(text_surface, text_rectangle)

    pygame.display.flip()

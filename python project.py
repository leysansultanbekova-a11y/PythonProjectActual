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
GRAY = (128, 128, 128)

selected = []
for r in range(ROWS):
    selected.append([False] * COLS)

font = pygame.font.SysFont("NY Times", 36)

words = [
    ["Dre", "Talent", "Brat", "Beauty"],
    ["Oz", "Nation", "Aid", "Luxe"],
    ["Responder", "Cope", "Staring", "Seuss"],
    ["Pepper", "Lady", "Wars", "Popularity"]
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // CELL_SIZE
            row = y // CELL_SIZE
            selected[row][col] = not selected[row][col]
            

    screen.fill(WHITE)

    for row in range(ROWS):
        for col in range(COLS):
            rectangle = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rectangle, 2)

            text_surface = font.render(words[row][col], True, BLACK)

            text_rectangle = text_surface.get_rect( 
            center = (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2)
            )
            screen.blit(text_surface, text_rectangle)

            if selected[row][col]:
                highlight = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
                highlight.fill((128, 128, 128, 120))  # RGBA — last value is transparency (0–255)
                screen.blit(highlight, (col * CELL_SIZE, row * CELL_SIZE))


    pygame.display.flip()

#thoughts for further code:
#put a cap of choosing 4 so that player can only select 4 boxes
#do if/else functions that check if the selected boxes are correct/incorrect depending on the categories
#shuffle words so that theyre not in the caategorized rows

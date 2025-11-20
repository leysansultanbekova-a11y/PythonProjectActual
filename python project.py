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

first = ["Aid", "Responder", "Nation", "Lady"]
contests = ["Staring", "Beauty", "Popularity", "Talent"]
doctors = ["Oz", "Pepper", "Dre", "Seuss"]
first_four = ["Brat", "Luxe", "Wars", "Cope"]

categories = [first, contests, doctors, first_four]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                total_selected = sum(sum(row) for row in selected)
                if not selected[row][col] and total_selected >= 4:
                     continue
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
                highlight.fill((128, 128, 128, 120))  
                screen.blit(highlight, (col * CELL_SIZE, row * CELL_SIZE))


         


    pygame.display.flip()

#thoughts for further code:
#do if/else functions that check if the selected boxes are correct/incorrect depending on the categories
#after correct selection, change the selected boxes into different colors depending on difficulty of the category
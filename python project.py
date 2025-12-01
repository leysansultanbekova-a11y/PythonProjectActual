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
GRAY = (128, 128, 128)

CATEGORY_COLORS = {
    "first": (255, 255, 200),     
    "contests": (144, 244, 144), 
    "doctors": (135, 206, 235),   
    "first_four": (203, 195, 227)  
}

font = pygame.font.SysFont("NY Times", 36)

words = [
    ["Dre", "Talent", "Brat", "Beauty"],
    ["Oz", "Nation", "Aid", "Luxe"],
    ["Responder", "Cope", "Staring", "Seuss"],
    ["Pepper", "Lady", "Wars", "Popularity"]
]

categories = {
    "first": ["Aid", "Responder", "Nation", "Lady"],
    "contests": ["Staring", "Beauty", "Popularity", "Talent"],
    "doctors": ["Oz", "Pepper", "Dre", "Seuss"],
    "first_four": ["Brat", "Luxe", "Wars", "Cope"]
}

selected = []
for row in range(ROWS):
    selected.append([False] * COLS)

locked_colors = []
for row in range(ROWS):
    locked_colors.append([None] * COLS)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE

                if locked_colors[row][col] is not None:
                    continue

                total_selected = sum(sum(row) for row in selected)
                if not selected[row][col] and total_selected >= 4:
                    continue
                selected[row][col] = not selected[row][col]

                total_selected = sum(sum(row) for row in selected)
                if total_selected == 4: 
                    selected_words = []
                    selected_position = []
                    for row in range(ROWS):
                        for col in range(COLS):
                            if selected[row][col]:
                                selected_words.append(words[row][col])
                                selected_position.append((row, col))
                    
                    matched_category = None
                    for name, group in categories.items(): 
                        if all(word in group for word in selected_words):
                            matched_category = name
                            break
                    if matched_category:
                        color = CATEGORY_COLORS[matched_category]
                        for (row, col) in selected_position:
                            locked_colors[row][col] = color

                    for row in range(ROWS):
                        for col in range(COLS):
                            selected[row][col] = False
            

    screen.fill(WHITE)

    for row in range(ROWS):
        for col in range(COLS):
            rectangle = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, BLACK, rectangle, 2)

            if locked_colors[row][col] is not None: 
                pygame.draw.rect(screen, locked_colors[row][col], rectangle)
            elif selected[row][col]:
                pygame.draw.rect(screen, GRAY, rectangle)
            
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
#move the correctly selected boxes to the top of the screen in rows
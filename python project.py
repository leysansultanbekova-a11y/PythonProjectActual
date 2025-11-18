
import pygame
import sys

# Initialize pygame
pygame.init()

# Grid settings
ROWS = 4
COLS = 4
CELL_SIZE = 100
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4x4 Grid Example")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill background
    screen.fill(WHITE)

    # Draw grid lines
    for row in range(ROWS + 1):
        pygame.draw.line(screen, BLACK, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), 2)

    for col in range(COLS + 1):
        pygame.draw.line(screen, BLACK, (col * CELL_SIZE, 0), (col * CELL_SIZE, HEIGHT), 2)

    pygame.display.flip()

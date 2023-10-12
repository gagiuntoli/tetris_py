import pygame

from shapes import shapes, shape_colors
from colors import WHITE, BLACK, BLUE, GREY

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

GRID_WIDTH = 10
GRID_HEIGHT = 20

LINE_WIDTH = 1

SQUARE_SIZE = 20

FPS = 24

""" 
The `grid` object represent the current state of the TETRIS.
It is just a 2D array of colors.
"""

class Piece():
    def __init__(self, row, col, shape, color):
        self.row = row
        self.col = col
        self.shape = shape
        self.color = color

    def rotate(self, direction):
        pass

    def move_down(self):
        self.row += 1

    def move_left(self):
        self.col -= 1

    def move_right(self):
        self.col += 1

def draw_grid(screen, grid, offset_x = 0, offset_y = 0):
    for (i, row) in enumerate(grid):
        y = i * SQUARE_SIZE + offset_y
        for (j, color) in enumerate(row):
            x = j * SQUARE_SIZE + offset_x
            pygame.draw.rect(screen, color, (x, y, SQUARE_SIZE, SQUARE_SIZE))

    for i in range(len(grid) + 1):
        x1 = offset_x
        x2 = SQUARE_SIZE * GRID_WIDTH + x1
        y = i * SQUARE_SIZE + offset_y
        pygame.draw.line(screen, GREY, [x1, y], [x2, y], LINE_WIDTH)

    for i in range(len(grid[0]) + 1):
        y1 = offset_y
        y2 = SQUARE_SIZE * GRID_HEIGHT + y1
        x = offset_x + i * SQUARE_SIZE
        pygame.draw.line(screen, GREY, [x, y1], [x, y2], LINE_WIDTH)

def validate_configuration(grid, piece):
    return True

def update_grid(locked_grid, piece):
    if not validate_configuration(locked_grid, piece):
        return locked_grid, False

    grid = locked_grid.copy()

    x = piece.col
    y = piece.row
    for (i, shape_row) in enumerate(piece.shape):
        print(shape_row)
        for (j, symb) in enumerate(shape_row):
            if symb == '#':
                grid[y + i][x + j] = piece.color

    return grid, True

def clear_rows(grid):
    pass

def main():
    pygame.init()
    pygame.display.set_caption("TETRIS")

    font = pygame.font.SysFont('freemono', size=28, bold=True)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    """
    The grid consisted on 2 grids: `locked_grid` and `grid`, the first one does not
    contain the moving piece, while the second contains it
    """
    locked_grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

    piece = Piece(0, 2, shapes[1][0], shape_colors[0])

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    piece.move_right()
                    

        grid, updated = update_grid(locked_grid, piece)
       
        draw_grid(screen, grid, 70, 50)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

main()
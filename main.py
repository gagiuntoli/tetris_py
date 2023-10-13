import pygame
import random

from shapes import shapes, shape_colors
from colors import WHITE, BLACK, BLUE, GREY
from copy import deepcopy

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

GRID_WIDTH = 10
GRID_HEIGHT = 20

LINE_WIDTH = 1

SQUARE_SIZE = 20

TIME_LAPSE = 1 # Seconds

FPS = 24

LOOP_COUNTER = TIME_LAPSE * FPS

""" 
The `grid` object represent the current state of the TETRIS.
It is just a 2D array of colors.
"""

class Piece():
    def __init__(self, row, col, shape, current_shape = 0):
        self.row = row
        self.col = col
        self.shapes = shape
        self.color = shape_colors[shapes.index(shape)]
        self.current_shape = current_shape

    def rotate_left(self):
        self.current_shape = (self.current_shape - 1) % 4

    def rotate_right(self):
        self.current_shape = (self.current_shape + 1) % 4

    def get_shape(self):
        return self.shapes[self.current_shape]

    def move_up(self):
        self.row -= 1

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
    x = piece.col
    y = piece.row
    for (i, row) in enumerate(piece.get_shape()):
        for (j, symb) in enumerate(row):
            if symb == '#':
                if y + i < 0 or y + i >= GRID_HEIGHT or x + j < 0 or x + j >= GRID_WIDTH:
                    return False
                if grid[y + i][x + j] != BLACK:
                    return False
    return True

def update_grid(locked_grid, piece):
    grid = deepcopy(locked_grid)

    x = piece.col
    y = piece.row
    for (i, row) in enumerate(piece.get_shape()):
        for (j, symb) in enumerate(row):
            if symb == '#':
                grid[y + i][x + j] = piece.color
    return grid

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

    piece = Piece(0, 2, random.choice(shapes), 0)

    running = True
    counter = 1
    activate_lock = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if not activate_lock:
                    if event.key == pygame.K_RIGHT:
                        piece.move_right()
                        if not validate_configuration(locked_grid, piece):
                            piece.move_left()
                    elif event.key == pygame.K_LEFT:
                        piece.move_left()
                        if not validate_configuration(locked_grid, piece):
                            piece.move_right()
                    elif event.key == pygame.K_z:
                        piece.rotate_left()
                        if not validate_configuration(locked_grid, piece):
                            piece.rotate_right()
                    elif event.key == pygame.K_x:
                        piece.rotate_right()
                        if not validate_configuration(locked_grid, piece):
                            piece.rotate_left()
                    elif event.key == pygame.K_DOWN:
                        piece.move_down()
                        if not validate_configuration(locked_grid, piece):
                            piece.move_up()
                    
        if counter % LOOP_COUNTER == 0:
            if activate_lock:
                locked_grid = grid
                piece = Piece(0, 2, random.choice(shapes), 0)
                activate_lock = False
            piece.move_down()
            if not validate_configuration(locked_grid, piece):
                piece.move_up()
                activate_lock = True

        grid = update_grid(locked_grid, piece)
       
        draw_grid(screen, grid, 70, 50)

        counter += 1
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

main()
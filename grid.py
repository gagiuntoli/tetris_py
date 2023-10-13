
from colors import BLACK

def clear_rows(grid):
    height = len(grid)
    width = len(grid[0])
    deleted = True
    while deleted:
        deleted = False
        for row in range(height-1, 0, -1):
            if grid[row].count(BLACK) == 0:
                for j in range(row, 0, -1):
                    grid[j] = grid[j - 1].copy()
                grid[0] = [BLACK for _ in range(width)]
                deleted = True
    return grid
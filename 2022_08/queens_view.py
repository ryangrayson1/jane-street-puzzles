import sys
from itertools import product

def valid_indices(grid, row, col):
    return row in range(len(grid)) and col in range(len(grid[0]))

# Queen's view since it's the same as what a queen in chess can 'view'
def queens_view(grid, row, col, dr=0, dc=0):
    if dr or dc:
        yield (row, col)
        if valid_indices(grid, row+dr, col+dc):
            yield from queens_view(grid, row+dr, col+dc, dr, dc)
    else:
        for dr, dc in product([-1, 0, 1], [-1, 0, 1]):
            if (dr or dc) and valid_indices(grid, row+dr, col+dc):
                yield from queens_view(grid, row+dr, col+dc, dr, dc)

sys.modules['queens_view'] = queens_view
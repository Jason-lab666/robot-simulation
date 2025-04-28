import random
from color_defs import (
    COLOR_YELLOW, COLOR_CYAN, COLOR_GREEN,
    COLOR_BLUE, COLOR_MAGENTA, COLOR_WHITE
)

def init_floor_checkerboard(rowNum, colNum):
    floor = []
    for r in range(rowNum):
        row = []
        for c in range(colNum):
            block_row = r // 4
            block_col = c // 4
            if (block_row + block_col) % 2 == 0:
                row.append(COLOR_WHITE)
            else:
                row.append(COLOR_MAGENTA)
        floor.append(row)
    return floor

def init_floor_all_magenta(rowNum, colNum):
    return [[COLOR_MAGENTA for _ in range(colNum)] for _ in range(rowNum)]

def init_floor_random_stripes(rowNum, colNum, seed):
    random.seed(seed)
    first_row = [random.randint(1, 6) for _ in range(colNum)]
    floor = [first_row.copy() for _ in range(rowNum)]
    return floor
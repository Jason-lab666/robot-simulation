# board_init.py

import random

# Floor color codes
COLOR_YELLOW = 1
COLOR_CYAN = 2
COLOR_GREEN = 3
COLOR_BLUE = 4
COLOR_MAGENTA = 5
COLOR_WHITE = 6

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
    for r in range(1, rowNum):
        floor[r] = first_row.copy()
    return floor

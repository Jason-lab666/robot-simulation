# robot.py

from input_reader import read_file
from board_init import (
    init_floor_checkerboard,
    init_floor_all_magenta,
    init_floor_random_stripes,
    COLOR_YELLOW, COLOR_CYAN, COLOR_GREEN,
    COLOR_BLUE, COLOR_MAGENTA, COLOR_WHITE
)

if __name__ == "__main__":
   
    row, col, robots, initType, seed, iters, interval, outFile = read_file()

    
    if initType == 1:
        floor = init_floor_random_stripes(row, col, seed)
    elif initType == 2:
        floor = init_floor_checkerboard(row, col)
    elif initType == 3:
        floor = init_floor_all_magenta(row, col)
    else:
        print("ERROR: Unknown initType.")
        exit(1)

    
    print("\n=== Floor preview (first 5 rows) ===")
    for r in floor[:5]:
        print(r)



from input_reader import read_file

from board_init import (
    init_floor_checkerboard,
    init_floor_all_magenta,
    init_floor_random_stripes
)
from color_defs import (
    COLOR_YELLOW, COLOR_CYAN, COLOR_GREEN,
    COLOR_BLUE, COLOR_MAGENTA, COLOR_WHITE
)

import random

def init_robots(floor, robotNum, rowNum, colNum, seed):
    random.seed(seed)
    robots = []
    for _ in range(robotNum):
        x = random.randint(0, rowNum - 1)
        y = random.randint(0, colNum - 1)
        direction = random.randint(0, 3)
        paint_color = random.randint(1, 4)
        robot = {
            'x': x,
            'y': y,
            'dir': direction,
            'color': paint_color
        }
        robots.append(robot)
        floor[x][y] = paint_color
    return robots

def move_forward(x, y, dir, rowNum, colNum):
    if dir == 0:
        x = (x - 1) % rowNum
    elif dir == 1:
        y = (y + 1) % colNum
    elif dir == 2:
        x = (x + 1) % rowNum
    elif dir == 3:
        y = (y - 1) % colNum
    return x, y

def update_direction(dir, tile_color):
    if tile_color == COLOR_YELLOW:
        return (dir + 1) % 4
    elif tile_color == COLOR_CYAN:
        return (dir + 2) % 4
    elif tile_color == COLOR_GREEN:
        return (dir + 3) % 4
    elif tile_color in (COLOR_BLUE, COLOR_MAGENTA, COLOR_WHITE):
        return dir  
    else:
        return dir



def simulate_step(floor, robots, rowNum, colNum):
    for robot in robots:

        for _ in range(4):
            robot['x'], robot['y'] = move_forward(robot['x'], robot['y'], robot['dir'], rowNum, colNum)

        original_color = floor[robot['x']][robot['y']]

        # Paint the tile
        floor[robot['x']][robot['y']] = robot['color']

        # Update direction
        robot['dir'] = update_direction(robot['dir'], original_color)




def print_floor(floor, file=None):
    for row in floor:
        line = ''.join(str(cell) for cell in row)
        if file:
            print(line, file=file)
        else:
            print(line)

def run_simulation(floor, robots, rowNum, colNum, iterations, interval, outputFile):
    # Print Iteration 0
    print("Iteration 0: robots on floor with initial tile pattern")
    print_floor(floor)

    with open(outputFile, 'w') as f:
        print("Iteration 0: robots on floor with initial tile pattern", file=f)
        print_floor(floor, file=f)

        for step in range(1, iterations + 1):
            simulate_step(floor, robots, rowNum, colNum)
            if step % interval == 0:
                print(f"Iteration {step}")
                print_floor(floor)

                print(f"Iteration {step}", file=f)
                print_floor(floor, file=f)

    print(f"\n Simulation complete. Output written to: {outputFile}")



if __name__ == "__main__":
    row, col, robotNum, initType, seed, iterations, interval, outputFile = read_file()

    print(f"\n Loaded input parameters:")
    print("rowNum =", row)
    print("colNum =", col)
    print("robotNum =", robotNum)
    print("initType =", initType)
    print("seed =", seed)
    print("iterations =", iterations)
    print("interval =", interval)
    print("outputFilename =", outputFile)

    if initType == 1:
        floor = init_floor_random_stripes(row, col, seed)
    elif initType == 2:
        floor = init_floor_checkerboard(row, col)
    else:
        floor = init_floor_all_magenta(row, col)

    print("\n=== Floor Preview (first 5 rows) ===")
    for r in floor[:5]:
        print(r)

    robots = init_robots(floor, robotNum, row, col, seed)
    print("\n=== Robot Initial States ===")
    for i, r in enumerate(robots):
        print(f"Robot {i+1}: Pos=({r['x']},{r['y']}), Dir={r['dir']}, Color={r['color']}")

    run_simulation(floor, robots, row, col, iterations, interval, outputFile)

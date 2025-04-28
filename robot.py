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
    rotation = {
        COLOR_YELLOW: 1,    
        COLOR_CYAN: 2,     
        COLOR_GREEN: 3,     
        COLOR_MAGENTA: 1,  
        COLOR_WHITE: 2      
    }.get(tile_color, 0)
    return (dir + rotation) % 4

def simulate_step(floor, robots, rowNum, colNum):
    for robot in robots:
        for _ in range(4):
            robot['x'], robot['y'] = move_forward(robot['x'], robot['y'], robot['dir'], rowNum, colNum)
            floor[robot['x']][robot['y']] = robot['color']
        tile_color = floor[robot['x']][robot['y']]
        robot['dir'] = update_direction(robot['dir'], tile_color)

def print_floor(floor, file=None):
    for row in floor:
        line = ' '.join(map(str, row))
        if file:
            print(line, file=file)
        else:
            print(line)

def run_simulation(floor, robots, rowNum, colNum, iterations, interval, outputFile):
    with open(outputFile, 'w') as f:
        print("Iteration 0", file=f)
        print_floor(floor, file=f)
        
        for step in range(1, iterations + 1):
            simulate_step(floor, robots, rowNum, colNum)
            if step % interval == 0 or step == iterations:
                print(f"Iteration {step}", file=f)
                print_floor(floor, file=f)
    print(f"Simulation complete. Output written to: {outputFile}")

if __name__ == "__main__":
    row, col, robotNum, initType, seed, iterations, interval, outputFile = read_file()
    
    if initType == 1:
        floor = init_floor_random_stripes(row, col, seed)
    elif initType == 2:
        floor = init_floor_checkerboard(row, col)
    else:
        floor = init_floor_all_magenta(row, col)
    
    robots = init_robots(floor, robotNum, row, col, seed)
    run_simulation(floor, robots, row, col, iterations, interval, outputFile)
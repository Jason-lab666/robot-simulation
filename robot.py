def read_file(max_attempt=5):
    attempt = 0

    while attempt < max_attempt:
        filename = input("Enter input filename: ").strip()
        try:
            with open(filename, 'r') as file:
                lines = [line.strip() for line in file.readlines()]
                if len(lines) < 8:
                    print("ERROR: Input file must contain at least 8 lines.")
                    exit(1)

                rowNum = int(lines[0])
                if not (12 <= rowNum <= 100):
                    print("ERROR: rowNum must be between 12 and 100.")
                    exit(1)

                colNum = int(lines[1])
                if not (12 <= colNum <= 100):
                    print("ERROR: colNum must be between 12 and 100.")
                    exit(1)

                robotNum = int(lines[2])
                if not (1 <= robotNum <= 10):
                    print("ERROR: robotNum must be between 1 and 10.")
                    exit(1)

                initType = int(lines[3])
                if not (1 <= initType <= 3):
                    print("ERROR: initType must be between 1 and 3.")
                    exit(1)

                seed = int(lines[4])
                if not (10 <= seed <= 32767):
                    print("ERROR: seed must be between 10 and 32767.")
                    exit(1)

                iterations = int(lines[5])
                if not (5 <= iterations <= 2000):
                    print("ERROR: iterations must be between 5 and 2000.")
                    exit(1)

                interval = int(lines[6])
                if not (1 <= interval <= iterations):
                    print("ERROR: interval must be between 1 and iterations.")
                    exit(1)

                outputFile = lines[7]
                if outputFile == "":
                    print("ERROR: outputFile name cannot be empty.")
                    exit(1)

                return rowNum, colNum, robotNum, initType, seed, iterations, interval, outputFile

        except FileNotFoundError:
            print("ERROR: Open file unsuccessful.")
            attempt += 1

        except ValueError:
            print("ERROR: One or more lines in the file are not valid integers.")
            exit(1)

    print("ERROR: Too many failed attempts.")
    exit(1)

if __name__ == "__main__":
    row, col, robots, initType, seed, iters, interval, outFile = read_file()
    print("rowNum =", row)
    print("colNum =", col)
    print("robotNum =", robots)
    print("initType =", initType)
    print("seed =", seed)
    print("iterations =", iters)
    print("interval =", interval)
    print("outputFilename =", outFile)

import random

# Floor color：1 = yellow, 2 = cyan, 3 = green, 4 = blue, 5 = magenta, 6 = white
COLOR_YELLOW = 1
COLOR_CYAN = 2
COLOR_GREEN = 3
COLOR_BLUE = 4
COLOR_MAGENTA = 5
COLOR_WHITE = 6

# Initialize checkerboard 
def init_floor_checkerboard(rowNum, colNum):
    floor = []
    for r in range(rowNum):
        row = []
        for c in range(colNum):
            # 4x4 
            block_row = r // 4
            block_col = c // 4
            if (block_row + block_col) % 2 == 0:
                row.append(COLOR_WHITE)
            else:
                row.append(COLOR_MAGENTA)
        floor.append(row)
    return floor

# Initialize all-magenta
def init_floor_all_magenta(rowNum, colNum):
    return [[COLOR_MAGENTA for _ in range(colNum)] for _ in range(rowNum)]

# Initilaize the floor with random stripes
def init_floor_random_stripes(rowNum, colNum, seed):
    random.seed(seed)
    first_row = [random.randint(1, 6) for _ in range(colNum)]
    floor = [first_row.copy() for _ in range(rowNum)]
    for r in range(1, rowNum):
        floor[r] = first_row.copy()  
    return floor

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


# Ini robots
def init_robots(floor, robotNum, rowNum, colNum, seed):
    random.seed(seed)
    
    robots = []
    for _ in range(robotNum):
        x = random.randint(0, rowNum - 1)   # Random x
        y = random.randint(0, colNum - 1)   # Random y
        direction = random.randint(0, 3)  # 0=up 1=right 2=down 3=left
        paint_color = random.randint(1, 4)  # Random color


# Dictionary
        robot = {
            'x': x,
            'y': y,
            'dir': direction,
            'color': paint_color
        }
        robots.append(robot)

      
        floor[x][y] = paint_color

    return robots

# Ini robot move 
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
    if tile_color == 1:      # Yellow :Turn right
        return (dir + 1) % 4
    
    elif tile_color == 2:    # Cyan → Turn left
        return (dir - 1) % 4
    
    elif tile_color == 3:    # Green → Turn 180 
        return (dir + 2) % 4
    
    else:                    # Blue, Magenta, White → Not turning
        return dir

def simulate_step(floor, robots, rowNum, colNum):
    for robot in robots:
        for _ in range(4):
            robot['x'], robot['y'] = move_forward(robot['x'], robot['y'], robot['dir'], rowNum, colNum)
            floor[robot['x']][robot['y']] = robot['color']
        tile_color = floor[robot['x']][robot['y']]
        robot['dir'] = update_direction(robot['dir'], tile_color)
        floor[robot['x']][robot['y']] = robot['color']



if __name__ == "__main__":
    row, col, robotNum, initType, seed, iterations, interval, outputFile = read_file()

    # Ini floor test
    if initType == 1:
        floor = init_floor_random_stripes(row, col, seed)

    elif initType == 2:
        floor = init_floor_checkerboard(row, col)
        
    else:
        floor = init_floor_all_magenta(row, col)

def print_floor(floor, file=None):
    color_map = {  # Change the number into the first character of the color to make it clearer
        1: 'Y',  # Yellow
        2: 'C',  # Cyan
        3: 'G',  # Green
        4: 'B',  # Blue
        5: 'M',  # Magenta
        6: 'W'   # White
    }
    for row in floor:
        line = ''.join(color_map.get(cell, '?') for cell in row)
        if file:
            print(line, file=file)
        else:
            print(line)


def run_simulation(floor, robots, rowNum, colNum, iterations, interval, outputFile):
    for step in range(1, iterations + 1):
        simulate_step(floor, robots, rowNum, colNum)
        if step % interval == 0:
            print(f"\n--- Step {step} ---")
            print_floor(floor)

    # Write into the file
    with open(outputFile, 'w') as f:
        print(f"# Final floor after {iterations} iterations", file=f)
        print_floor(floor, file=f)
    print(f"\n Simulation complete. Output written to: {outputFile}")



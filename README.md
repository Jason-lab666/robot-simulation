# robot-simulation

# Robot Simulation Program Summary

## Problem Statement
Write a C program that simulates multiple robots moving and painting on a grid-based colored tile floor. The program must read input parameters, initialize the room and robots, simulate their movements, and record the results.

## Core Requirements

### Input Parameters (read from file)
1. Number of rows (12 ≤ numRows ≤ 100)
2. Number of columns (12 ≤ numCols ≤ 100)
3. Number of robots (1 ≤ numRobots ≤ 10)
4. Floor initialization type (1-3)
5. Random seed (10 ≤ initSeed ≤ 32767)
6. Number of iterations (5 ≤ numIterations ≤ 2000)
7. Output interval (1 ≤ interval ≤ numIterations)
8. Output filename

### Initialization
1. Dynamic memory allocation:
   - Array of robot structures
   - 2D array representing the floor tiles
2. Initialize floor pattern (three types):
   - All magenta tiles
   - Checkerboard (magenta and white)
   - Random colored vertical stripes
3. Initialize each robot with:
   - Random position (x,y)
   - Random facing direction
   - Random paint color (1-4)
   - Paint starting position with robot's color

### Robot Behavior
Each iteration, every robot executes:
1. Move forward 4 steps (painting each tile)
2. Rotate based on 4th step's tile color:
   - Yellow: 90° clockwise
   - Cyan: 180°
   - Green: 270°
   - Blue: 0°
   - Magenta: 90°
   - White: 180°
3. Paint current tile with robot's color

### Boundary Handling
Robots wrap around when moving past room edges.

### Output Requirements
1. Write results of all iterations to output file
2. Display on screen: initial state (iteration 0), iteration 1, every interval iterations, and final iteration

### Error Handling
Validate all input parameters and terminate with appropriate error messages if invalid.

### Additional Requirements
- Must use dynamic memory allocation with proper error checking
- Must follow specified coding standards
- Must use defined constants for parameter ranges
- Must clean up allocated memory before termination

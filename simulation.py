from robot import init_robots, simulate_step
from board_init import (
    init_floor_checkerboard,
    init_floor_all_magenta,
    init_floor_random_stripes
)

class RobotSimulation:
    def __init__(self, row, col, robot_num, init_type, seed):
        self.row = row
        self.col = col
        self.init_type = init_type
        self.seed = seed
        self.floor = self._init_floor()
        self.robots = init_robots(self.floor, robot_num, row, col, seed)

    def _init_floor(self):
        if self.init_type == 1:
            return init_floor_random_stripes(self.row, self.col, self.seed)
        elif self.init_type == 2:
            return init_floor_checkerboard(self.row, self.col)
        else:
            return init_floor_all_magenta(self.row, self.col)

    def run(self, iterations, interval, output_file):
        with open(output_file, 'w') as f:
            self._log_state(0, f)
            
            for step in range(1, iterations + 1):
                simulate_step(self.floor, self.robots, self.row, self.col)
                if step % interval == 0:
                    self._log_state(step, f)

    def _log_state(self, step, file=None):
        title = f"Iteration {step}: {'initial' if step == 0 else 'current'} state"
        print(title)
        self.print_floor(file)
        
        if file:
            print(title, file=file)
            self.print_floor(file)

    def print_floor(self, file=None):
        for row in self.floor:
            line = ''.join(str(cell) for cell in row)
            print(line, file=file)
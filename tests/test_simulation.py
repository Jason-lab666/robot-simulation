import unittest
from unittest.mock import patch, mock_open
from robot import move_forward, update_direction, init_robots, simulate_step
from simulation import RobotSimulation
import input_reader
from board_init import init_floor_all_magenta

class TestRobotSimulation(unittest.TestCase):
    # Test move_forward wrap around
    def test_move_forward_wrap(self):
        self.assertEqual(move_forward(0, 0, 0, 5, 5), (4, 0))  # Up
        self.assertEqual(move_forward(4, 4, 2, 5, 5), (0, 4))  # Down
        self.assertEqual(move_forward(2, 4, 1, 5, 5), (2, 0))  # Right
        self.assertEqual(move_forward(2, 0, 3, 5, 5), (2, 4))  # Left

        self.assertEqual(update_direction(0, 1), 1)  # facing 0 → 1
        self.assertEqual(update_direction(1, 1), 2)  # facing 1 → 2

        # CYAN (2) → turn 180°
        self.assertEqual(update_direction(0, 2), 2)  # facing 0 → 2
        self.assertEqual(update_direction(1, 2), 3)  # facing 1 → 3

        # GREEN (3) → turn left 90°
        self.assertEqual(update_direction(0, 3), 3)  # facing 0 → 3
        self.assertEqual(update_direction(1, 3), 0)  # facing 1 → 0

        # BLUE (4) → no turn
        self.assertEqual(update_direction(0, 4), 0)  # facing 0 → 0
        self.assertEqual(update_direction(2, 4), 2)  # facing 2 → 2

        # MAGENTA (5) → turn right 90°
        self.assertEqual(update_direction(0, 5), 1)  # facing 0 → 1
        self.assertEqual(update_direction(2, 5), 3)  # facing 2 → 3

        # WHITE (6) → turn 180°
        self.assertEqual(update_direction(0, 6), 2)  # facing 0 → 2
        self.assertEqual(update_direction(1, 6), 3)  # facing 1 → 3


    # Test robot initialization
    def test_init_robots_basic(self):
        floor = init_floor_all_magenta(5, 5)
        robots = init_robots(floor, 3, 5, 5, seed=123)
        self.assertEqual(len(robots), 3)
        for r in robots:
            self.assertIn(r['dir'], range(4))
            self.assertIn(r['color'], range(1, 5))

    # Test simulate step
    def test_simulate_step_behavior(self):
        floor = init_floor_all_magenta(6, 6)
        robots = [{'x': 2, 'y': 2, 'dir': 0, 'color': 3}]
        simulate_step(floor, robots, 6, 6)
        self.assertEqual(floor[robots[0]['x']][robots[0]['y']], 3)
        self.assertIn(robots[0]['dir'], range(4))

    # Test RobotSimulation full run
    def test_simulation_basic_run(self):
        sim = RobotSimulation(row=5, col=5, robot_num=2, init_type=3, seed=42)
        with patch("builtins.open", mock_open()) as mocked_file:
            sim.run(iterations=2, interval=1, output_file="dummy.txt")
            handle = mocked_file()
            content = "".join(call.args[0] for call in handle.write.call_args_list)
            self.assertIn("Iteration 1", content)
            self.assertIn("Iteration 2", content)

    def test_input_reader_validfile(self):
    # 修改为符合要求的测试数据（行数列数至少为12）
        mock_data = "12\n12\n3\n1\n1234\n5\n1\nout.txt\n"
    expected = (12, 12, 3, 1, 1234, 5, 1, 'out.txt')
    
    with patch("builtins.open", mock_open(read_data=mock_data)):
        with patch("builtins.input", return_value="input_1.txt"):
            params = input_reader.read_file()
            self.assertEqual(params, expected)

    # Test input_reader: invalid file
    def test_input_reader_invalid(self):
        with patch("builtins.input", return_value="nonexistent.txt"):
            with self.assertRaises(SystemExit):
                input_reader.read_file()

if __name__ == "__main__":
    unittest.main()

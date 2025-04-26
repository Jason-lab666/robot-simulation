import unittest
from unittest.mock import mock_open, patch
from robot import (
    init_robots, move_forward, update_direction,
    simulate_step, run_simulation, print_floor
)
from board_init import init_floor_all_magenta


class TestRobotSimulation(unittest.TestCase):
    def test_init_robots(self):
        floor = init_floor_all_magenta(10, 10)
        robots = init_robots(floor, 3, 10, 10, seed=42)
        self.assertEqual(len(robots), 3)
        for r in robots:
            self.assertIn(r['dir'], range(4))
            self.assertIn(r['color'], range(1, 5))
            self.assertEqual(floor[r['x']][r['y']], r['color'])  # painted on init

    def test_move_forward_wrap(self):
        self.assertEqual(move_forward(0, 0, 0, 5, 5), (4, 0))  # up
        self.assertEqual(move_forward(4, 4, 2, 5, 5), (0, 4))  # down
        self.assertEqual(move_forward(2, 4, 1, 5, 5), (2, 0))  # right
        self.assertEqual(move_forward(2, 0, 3, 5, 5), (2, 4))  # left

    def test_turning(self):
    # YELLOW (1) → turn right 90°
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


    def test_simulate_step_logic(self):
        floor = init_floor_all_magenta(6, 6)
        robots = [{'x': 2, 'y': 2, 'dir': 0, 'color': 3}]
        simulate_step(floor, robots, 6, 6)

        # Robot moved 4 times and painted
        self.assertEqual(floor[robots[0]['x']][robots[0]['y']], 3)
        self.assertIn(robots[0]['dir'], range(4))  # new direction

    def test_run_simulation_output(self):
        floor = init_floor_all_magenta(5, 5)
        robots = init_robots(floor, 1, 5, 5, seed=123)

        mock_file = mock_open()
        with patch("builtins.open", mock_file):
            run_simulation(floor, robots, 5, 5, iterations=3, interval=1, outputFile="dummy.txt")

        # Check if file.write was called (indirectly via print with file=)
        handle = mock_file()
        written = "".join(call.args[0] for call in handle.write.call_args_list)
        self.assertIn("Iteration 1", written)
        self.assertIn("Iteration 2", written)

    def test_print_floor_console(self):
        floor = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        # Capture print to console
        with patch("builtins.print") as mocked_print:
            print_floor(floor)
        mocked_print.assert_any_call("123")
        mocked_print.assert_any_call("456")


if __name__ == "__main__":
    unittest.main()

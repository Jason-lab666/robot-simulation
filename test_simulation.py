import unittest
from simulation import init_robots, move_forward, update_direction
from board_init import init_floor_all_magenta

class TestSimulation(unittest.TestCase):
    def test_robot_init(self):
        floor = init_floor_all_magenta(10, 10)
        robots = init_robots(floor, 3, 10, 10, seed=42)
        self.assertEqual(len(robots), 3)
        for r in robots:
            self.assertIn(r['dir'], range(4))
            self.assertIn(r['color'], range(1, 5))

    def test_wrap_around(self):
        self.assertEqual(move_forward(0, 0, 0, 10, 10), (9, 0))  # up
        self.assertEqual(move_forward(9, 9, 2, 10, 10), (0, 9))  # down
        self.assertEqual(move_forward(5, 9, 1, 10, 10), (5, 0))  # right
        self.assertEqual(move_forward(5, 0, 3, 10, 10), (5, 9))  # left

    def test_turning(self):
        self.assertEqual(update_direction(0, 1), 1)  # turn right
        self.assertEqual(update_direction(0, 2), 3)  # turn left
        self.assertEqual(update_direction(0, 3), 2)  # 180 turn
        self.assertEqual(update_direction(1, 4), 1)  # not turn


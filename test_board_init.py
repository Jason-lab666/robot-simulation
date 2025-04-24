import unittest
from board_init import init_floor_checkerboard, init_floor_all_magenta, init_floor_random_stripes

class TestBoardInit(unittest.TestCase):
    def test_checkerboard(self):
        floor = init_floor_checkerboard(8, 8)
        self.assertEqual(len(floor), 8)
        self.assertEqual(len(floor[0]), 8)
        self.assertTrue(all(cell in [5, 6] for row in floor for cell in row)) 

    def test_all_magenta(self):
        floor = init_floor_all_magenta(5, 5)
        for row in floor:
            self.assertTrue(all(cell == 5 for cell in row))  

    def test_random_stripes(self):
        floor = init_floor_random_stripes(10, 5, seed=123)
        self.assertEqual(len(floor), 10)
        for row in floor:
            self.assertEqual(len(row), 5)


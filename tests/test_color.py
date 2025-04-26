import unittest
from color_defs import get_color_char, get_color_name, COLOR_MAP

class TestColorDefs(unittest.TestCase):
    def test_color_name(self):
        self.assertEqual(get_color_name(1), 'Yellow')
        self.assertEqual(get_color_name(6), 'White')

    def test_color_char(self):
        self.assertEqual(get_color_char(1), 'Y')
        self.assertEqual(get_color_char(4), 'B')

    def test_invalid_code(self):
        self.assertEqual(get_color_char(99), '?')
        self.assertEqual(get_color_name(0), 'Unknown')

if __name__ == "__main__":
    unittest.main()
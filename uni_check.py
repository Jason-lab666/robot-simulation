import unittest

class TestFileContents(unittest.TestCase):
    def test_files_equal(self):
        with open('out300.txt', 'r') as f1, open('t3.txt', 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
            self.assertEqual(content1, content2, "Not the same")

if __name__ == '__main__':
    unittest.main()
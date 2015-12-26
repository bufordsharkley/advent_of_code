import unittest

import day25


class DayTwentyFourTests(unittest.TestCase):

    def test_grid(self):
        self.assertEqual(day25.code_number((1, 1)), 1)
        self.assertEqual(day25.code_number((6, 1)), 16)
        self.assertEqual(day25.code_number((1, 6)), 21)

    def test_code(self):
        self.assertEqual(day25.code(2), 31916031)

if __name__ == "__main__":
    unittest.main()

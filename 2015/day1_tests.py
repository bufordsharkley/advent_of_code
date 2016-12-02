import unittest

import day1


class FloorTests(unittest.TestCase):

    def test_expected_floor_reached(self):
        self.assertEqual(day1.elevator('(())'), 0)
        self.assertEqual(day1.elevator('()()'), 0)
        self.assertEqual(day1.elevator('((('), 3)
        self.assertEqual(day1.elevator('(()(()('), 3)
        self.assertEqual(day1.elevator('))((((('), 3)
        self.assertEqual(day1.elevator('())'), -1)
        self.assertEqual(day1.elevator('))('), -1)
        self.assertEqual(day1.elevator(')))'), -3)
        self.assertEqual(day1.elevator(')())())'), -3)

    def test_first_to_basement_agrees(self):
        self.assertEqual(day1.first_to_basement(')'), 1)
        self.assertEqual(day1.first_to_basement('()())'), 5)

if __name__ == "__main__":
    unittest.main()

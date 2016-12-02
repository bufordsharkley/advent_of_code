import unittest

import day15


class DayFifteenTests(unittest.TestCase):

    def test_seats(self):
        b = day15.Recipe(capacity=-1, durability=-2, flavor=6, texture=3, calories=8)
        c = day15.Recipe(capacity=2, durability=3, flavor=-2, texture=-1, calories=3)
        all_ = b * 44 + c * 56
        self.assertEqual(all_.capacity, 68)
        self.assertEqual(all_.durability, 80)
        self.assertEqual(all_.flavor, 152)
        self.assertEqual(all_.texture, 76)
        self.assertEqual(all_.score(), 62842880)


if __name__ == "__main__":
    unittest.main()

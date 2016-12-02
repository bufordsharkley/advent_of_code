import unittest

import day18


class DayEighteenTests(unittest.TestCase):

    def test_init(self):
        init = day18.raw()
        self.assertEqual(len(init), 10000)
        self.assertEqual(init[34, 54], 0)

    def test_neighbors(self):
        neigh = day18.neighbors((34, 54))
        self.assertEqual(len(neigh), 8)


if __name__ == "__main__":
    unittest.main()

import unittest

import day17


class DaySeventeenTests(unittest.TestCase):

    def test_seats(self):
        resp = day17.find_ways(25, [20, 15, 10, 5, 5])
        self.assertEqual(len(resp), 4)


if __name__ == "__main__":
    unittest.main()

import unittest

import day14

class DayThirteenTests(unittest.TestCase):

    def test_seats(self):
        comet = day14.Reindeer(fly=14, duration=10, rest=127)
        dancer = day14.Reindeer(fly=16, duration=11, rest=162)
        comet.plus(1)
        dancer.plus(1)
        self.assertEqual(comet.position, 14)
        self.assertEqual(dancer.position, 16)
        self.assertEqual(dancer.time, 1)
        comet.plus(9)
        dancer.plus(9)
        self.assertEqual(comet.position, 140)
        self.assertEqual(dancer.position, 160)
        comet.plus(2)
        dancer.plus(2)
        self.assertEqual(dancer.time, 12)
        comet.goto(138)
        dancer.goto(138)
        self.assertEqual(dancer.time, 138)
        comet.goto(1000)
        dancer.goto(1000)
        self.assertEqual(comet.position, 1120)
        self.assertEqual(dancer.position, 1056)
                         #330)

if __name__ == "__main__":
    unittest.main()

import unittest

import day14

class DayThirteenTests(unittest.TestCase):

    def test_seats(self):
        comet = day14.Reindeer(name='Comet', speed=14, stamina=10, rest=127)
        dancer = day14.Reindeer(name='Dancer', speed=16, stamina=11, rest=162)
        comet.plus(1)
        dancer.plus(1)
        self.assertEqual(comet.position, 14)
        self.assertEqual(dancer.position, 16)
        comet.plus(9)
        dancer.plus(9)
        self.assertEqual(comet.position, 140)
        self.assertEqual(dancer.position, 160)
        comet.plus(2)
        dancer.plus(2)
        comet.plus(138 - 12)
        dancer.plus(138 - 12)
        comet.plus(1000 - 138)
        dancer.plus(1000 - 138)
        self.assertEqual(comet.position, 1120)
        self.assertEqual(dancer.position, 1056)

if __name__ == "__main__":
    unittest.main()

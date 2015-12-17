import unittest

import day14

class DayThirteenTests(unittest.TestCase):

    def test_seats(self):
        comet = day14.Reindeer(name='Comet', speed=14, stamina=10, rest=127)
        dancer = day14.Reindeer(name='Dancer', speed=16, stamina=11, rest=162)
        comet.move()
        dancer.move()
        self.assertEqual(comet.position, 14)
        self.assertEqual(dancer.position, 16)
        for ii in range(9):
          comet.move()
          dancer.move()
        self.assertEqual(comet.position, 140)
        self.assertEqual(dancer.position, 160)
        for ii in range(2):
          comet.move()
          dancer.move()
        for ii in range(1000 - 12):
          comet.move()
          dancer.move()
        self.assertEqual(comet.position, 1120)
        self.assertEqual(dancer.position, 1056)

if __name__ == "__main__":
    unittest.main()

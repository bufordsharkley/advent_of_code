import unittest

import day24


class DayTwentyFourTests(unittest.TestCase):

    def test_data(self):
        self.assertEqual(day24.quantum_entanglement([10, 9, 1]), 90)
        weights = range(1, 6) + range(7, 12)
        compartments = day24.optimize_sleigh(weights)
        self.assertEqual(compartments['1'], (9, 11))

    def test_can_divide(self):
        self.assertEqual(day24.can_divide([5, 5], 5, 2), True)




if __name__ == "__main__":
    unittest.main()

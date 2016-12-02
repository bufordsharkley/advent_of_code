import unittest

import day20


class DayTwentyTests(unittest.TestCase):

    def test_deliveries(self):
        self.assertEqual(day20.deliveries(1), 10)
        self.assertEqual(day20.deliveries(2), 30)
        self.assertEqual(day20.deliveries(3), 40)
        self.assertEqual(day20.deliveries(4), 70)
        self.assertEqual(day20.deliveries(5), 60)
        self.assertEqual(day20.deliveries(6), 120)
        self.assertEqual(day20.deliveries(7), 80)
        self.assertEqual(day20.deliveries(8), 150)
        self.assertEqual(day20.deliveries(9), 130)

    def test_stop_at_50(self):
        self.assertEqual(day20.deliveries(50), 930)
        self.assertEqual(day20.deliveries(50, lazy_elf=True), 720 * 11 / 10)
        self.assertEqual(day20.deliveries(51), 720)
        self.assertEqual(day20.deliveries(51, lazy_elf=True), 720 * 11 / 10 - 11)


if __name__ == "__main__":
    unittest.main()

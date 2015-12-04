import unittest

import day3


class DeliveringPresentsTests(unittest.TestCase):

    def test_expected_santa_houses(self):
        self.assertEqual(day3.num_houses('>'), 2)
        self.assertEqual(day3.num_houses('^>v<'), 4)
        self.assertEqual(day3.num_houses('^v^v^v^v^v'), 2)

    def test_expected_santa_and_robo_houses(self):
        self.assertEqual(day3.num_houses_with_robo('^v'), 3)
        self.assertEqual(day3.num_houses_with_robo('^>v<'), 3)
        self.assertEqual(day3.num_houses_with_robo('^v^v^v^v^v'), 11)


if __name__ == "__main__":
    unittest.main()

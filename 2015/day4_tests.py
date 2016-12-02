import unittest

import day4


class DeliveringPresentsTests(unittest.TestCase):

    def test_lowest_hash_numbers(self):
        self.assertEqual(day4.find_lowest_hash('abcdef'), 609043)
        self.assertEqual(day4.find_lowest_hash('pqrstuv'), 1048970)

    def test_combine_string_num(self):
        self.assertEqual(day4.combine('text', 1), 'text1')
        self.assertEqual(day4.combine('text', 100), 'text100')


if __name__ == "__main__":
    unittest.main()

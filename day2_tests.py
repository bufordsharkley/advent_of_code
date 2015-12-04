import unittest

import day2


class WrappingTests(unittest.TestCase):

    def test_parser(self):
        self.assertEqual(day2.dims_from_box('12x14x03'), (12, 14, 3))

    def test_expected_surface_area(self):
        self.assertEqual(day2.surface_area(2, 3, 4), 58)
        self.assertEqual(day2.surface_area(1, 1, 10), 43)

    def test_expected_ribbon(self):
        self.assertEqual(day2.ribbon(2, 3, 4), 34)
        self.assertEqual(day2.ribbon(1, 1, 10), 14)

if __name__ == "__main__":
    unittest.main()

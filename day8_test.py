import unittest

import day8


class DayEightTests(unittest.TestCase):

    def test_through_resolve(self):
        self.assertEqual(day8.charlen(r'""'), 2)
        self.assertEqual(day8.actuallen(r'""'), 0)
        self.assertEqual(day8.charlen(r'"abc"'), 5)
        self.assertEqual(day8.actuallen(r'"abc"'), 3)
        self.assertEqual(day8.charlen(r'"aaa\"aaa"'), 10)
        self.assertEqual(day8.actuallen(r'"aaa\"aaa"'), 7)
        self.assertEqual(day8.charlen(r'"\x27"'), 6)
        self.assertEqual(day8.actuallen(r'"\x27"'), 1)

    def test_encode(self):
        self.assertEqual(day8.charlen(r'""'), 2)
        self.assertEqual(day8.encodedlen(r'""'), 6)
        self.assertEqual(day8.encodedlen(r'"abc"'), 9)
        self.assertEqual(day8.encodedlen(r'"aaa\"aaa"'), 16)
        self.assertEqual(day8.encodedlen(r'"\x27"'), 11)


if __name__ == "__main__":
    unittest.main()

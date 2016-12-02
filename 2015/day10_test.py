import unittest

import day10


class DayTenTests(unittest.TestCase):

    def test_look(self):
        self.assertEqual(day10.looknsay('1'), '11')
        self.assertEqual(day10.looknsay('11'), '21')
        self.assertEqual(day10.looknsay('21'), '1211')
        self.assertEqual(day10.looknsay('1211'), '111221')
        self.assertEqual(day10.looknsay('111221'), '312211')


if __name__ == "__main__":
    unittest.main()

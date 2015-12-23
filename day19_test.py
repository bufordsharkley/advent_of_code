import unittest

import day19

REPLACER = """\
H => HO
H => OH
O => HH
"""

REPLACER2 = """\
e => H
e => O
H => HO
H => OH
O => HH
"""

class DayNineteenTests(unittest.TestCase):

    def test_init(self):
        replacer = day19.parse_replacer(REPLACER)
        print replacer
        possibilities = set(day19.find_possibilities(replacer, 'HOH'))
        print possibilities
        self.assertEqual(len(set(possibilities)), 4)
        possibilities = set(day19.find_possibilities(replacer, 'HOHOHO'))
        self.assertEqual(len(set(possibilities)), 7)
        possibilities = set(day19.find_possibilities([('H', 'OO')], 'H2O'))
        self.assertEqual(possibilities, set(['OO2O']))
        possibilities = set(day19.find_possibilities([('H2', 'X')], 'H2O'))
        self.assertEqual(possibilities, set(['XO']))

    def test_part_b(self):
        replacer = day19.backwards(day19.parse_replacer(REPLACER2))
        steps  = day19.steps_to_reach(replacer, 'HOH', 'HOH')
        self.assertEqual(steps, 0)
        steps  = day19.steps_to_reach(replacer, 'O', 'e')
        self.assertEqual(steps, 1)
        steps  = day19.steps_to_reach(replacer, 'HOH', 'e')
        self.assertEqual(steps, 3)
        steps  = day19.steps_to_reach(replacer, 'HOHOHO', 'e')
        self.assertEqual(steps, 6)


if __name__ == "__main__":
    unittest.main()

import unittest

import day23

PGM = """\
inc a
jio a, +2
tpl a
inc a
"""


class DayTwentyThreeTests(unittest.TestCase):

    def test_look(self):
        registers = day23.fresh_registers()
        registers = day23.run_program(registers, PGM)
        self.assertEqual(registers['a'], 2)
        self.assertEqual(registers['b'], 0)


if __name__ == "__main__":
    unittest.main()

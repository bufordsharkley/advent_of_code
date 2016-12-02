import unittest

import day6


class Day6Tests(unittest.TestCase):

    def test_through_resolve(self):
        nine = set((ii, jj) for ii in range(0, 3) for jj in range(0, 3))
        self.assertEqual(day6.resolve_xy('0,0'), (0, 0))
        self.assertEqual(set(day6.resolve_through('0,0 through 2,2')), nine)

    def test_init(self):
        self.assertEqual(len(day6.raw()), 1000000)

    def test_instruction(self):
        grid = day6.raw()
        day6.process_instruct(grid, 'toggle', (4, 4))
        self.assertEqual(grid[(4, 4)], 1)
        day6.process_instruct(grid, 'toggle', (4, 4))
        self.assertEqual(grid[(4, 4)], 0)
        day6.process_instruct(grid, 'turn on', (4, 4))
        self.assertEqual(grid[(4, 4)], 1)
        day6.process_instruct(grid, 'turn on', (4, 4))
        self.assertEqual(grid[(4, 4)], 1)
        day6.process_instruct(grid, 'turn off', (4, 4))
        self.assertEqual(grid[(4, 4)], 0)
        day6.process_instruct(grid, 'turn off', (4, 4))
        self.assertEqual(grid[(4, 4)], 0)

    def test_line_instruct(self):
        grid = day6.raw()
        day6.process_instruct_line(grid, 'turn on 0,0 through 999,999')
        self.assertEqual(grid[(38, 493)], 1)
        day6.process_instruct_line(grid, 'turn off 499,499 through 500,500')
        self.assertEqual(grid[(499, 499)], 0)


if __name__ == "__main__":
    unittest.main()

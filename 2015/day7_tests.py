import unittest

import day7


class CircuitTests(unittest.TestCase):

    def test_arrows(self):
        self.assertEqual(day7.parse_arrow('blippy -> bloppy'),
                         ('blippy', 'bloppy'))

    def test_parse_sigs(self):
        self.assertEqual(day7.parse_sig('123'), 123)
        vals = {'x': 4, 'y': 2}
        x = 4
        y = 2
        self.assertEqual(day7.parse_sig('x AND y', vals), x & y)
        self.assertEqual(day7.parse_sig('x OR y', vals), x | y)
        self.assertEqual(day7.parse_sig('x LSHIFT 2', vals), x << 2)
        self.assertEqual(day7.parse_sig('x RSHIFT 2', vals), x >> 2)
        # I'll be honest, I don't see why this is what passes:
        x = 0b1010101010101010
        self.assertEqual(day7.parse_sig('NOT x', vals), 0b1111111111111011)

    def test_parse_lint(self):
        line = '123 -> x'
        vals = {}
        day7.parse_line(line, vals)
        self.assertEqual(vals, {'x': 123})
        day7.parse_line('456 -> y', vals)
        self.assertEqual(vals, {'x': 123, 'y': 456})
        day7.parse_line('x AND y -> d', vals)
        self.assertEqual(vals, {'x': 123, 'y': 456, 'd': 72})
        day7.parse_line('x OR y -> e', vals)
        self.assertEqual(vals, {'x': 123, 'y': 456, 'd': 72, 'e': 507})
        day7.parse_line('x LSHIFT 2 -> f', vals)
        self.assertEqual(vals, {'x': 123, 'y': 456, 'd': 72,
                                'f': 492, 'e': 507})
        day7.parse_line('y RSHIFT 2 -> g', vals)
        self.assertEqual(vals, {'x': 123, 'g': 114, 'y': 456,
                                'd': 72, 'f': 492, 'e': 507})
        day7.parse_line('NOT x -> h', vals)
        self.assertEqual(vals, {'x': 123, 'h': 65412, 'g': 114,
                                'y': 456, 'd': 72, 'f': 492, 'e': 507})
        day7.parse_line('NOT y -> i', vals)
        self.assertEqual(vals, {'i': 65079, 'x': 123, 'h': 65412, 'g': 114,
                                'y': 456, 'd': 72, 'f': 492, 'e': 507})

if __name__ == "__main__":
    unittest.main()

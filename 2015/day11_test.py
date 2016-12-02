import unittest

import day11


class DayElevenTests(unittest.TestCase):

    def test_look(self):
        self.assertEqual(day11.increment_char('y'), ('z', False))
        self.assertEqual(day11.increment_char('z'), ('a', True))
        self.assertEqual(day11.increment('y'), 'z')
        self.assertEqual(day11.increment('bzzz'), 'caaa')
        self.assertEqual(day11.increment('wyz'), 'wza')
        self.assertEqual(day11.increment('abcdefgz'), 'abcdefha')
        self.assertEqual(day11.increment('hellox'), 'helloy')
        self.assertEqual(day11.is_increasing_straight('helloabcx'), True)
        self.assertEqual(day11.is_increasing_straight('helloabdx'), False)
        self.assertEqual(day11.is_clean_of_forbidden('mollineaux'), False)
        self.assertEqual(day11.is_clean_of_forbidden('mneaux'), True)
        self.assertEqual(day11.is_two_pair('baabsdzz'), True)
        self.assertEqual(day11.is_two_pair('babsdzz'), False)
        self.assertEqual(day11.is_valid('hijklmn'), False)
        self.assertEqual(day11.is_valid('abbceffg'), False)
        self.assertEqual(day11.is_valid('abbcegjk'), False)
        self.assertEqual(day11.is_valid('abcdffaa'), True)
        self.assertEqual(day11.next_valid('abcdefgh'), 'abcdffaa')
        self.assertEqual(day11.next_valid('ghijklmn'), 'ghjaabcc')


if __name__ == "__main__":
    unittest.main()

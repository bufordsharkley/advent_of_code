import unittest

import day5b


class Niceness2Tests(unittest.TestCase):

    def test_pairs_of_two_letters(self):
        self.assertEqual(day5b.is_twice_2('xyxy'), True)
        self.assertEqual(day5b.is_twice_2('aabcdefgaa'), True)
        self.assertEqual(day5b.is_twice_2('aaa'), False)
        self.assertEqual(day5b.is_twice_2('rxexcbwhiywwwwnu'), True)
        self.assertEqual(day5b.is_sandwich('xyx'), True)
        self.assertEqual(day5b.is_sandwich('xyyx'), False)
        self.assertEqual(day5b.is_sandwich('abcdefeghi'), True)
        self.assertEqual(day5b.is_sandwich('efe'), True)
        self.assertEqual(day5b.is_sandwich('aaa'), True)
        self.assertEqual(day5b.is_super_nice('qjhvhtzxzqqjkmpb'), True)
        self.assertEqual(day5b.is_super_nice('xxyxx'), True)
        self.assertEqual(day5b.is_super_nice('uurcxstgmygtbstg'), False)
        self.assertEqual(day5b.is_super_nice('ieodomkazucvgmuy'), False)


if __name__ == "__main__":
    unittest.main()

import unittest

import day5


class Day5Tests(unittest.TestCase):

    def test_is_nice(self):
        self.assertEqual(day5.is_vowel('aei'), True)
        self.assertEqual(day5.is_vowel('ei'), False)
        self.assertEqual(day5.is_vowel('xazegov'), True)
        self.assertEqual(day5.is_vowel('xazgov'), False)
        self.assertEqual(day5.is_vowel('zeiouaeiouaeiou'), True)
        self.assertEqual(day5.is_twice('xx'), True)
        self.assertEqual(day5.is_twice('abcdde'), True)
        self.assertEqual(day5.is_twice('abcde'), False)
        self.assertEqual(day5.not_those('ab'), False)
        self.assertEqual(day5.not_those('cd'), False)
        self.assertEqual(day5.not_those('pq'), False)
        self.assertEqual(day5.not_those('xy'), False)
        self.assertEqual(day5.not_those('acpx'), True)
        self.assertEqual(day5.is_nice('ugknbfddgicrmopn'), True)
        self.assertEqual(day5.is_nice('aaa'), True)
        self.assertEqual(day5.is_nice('jchzalrnumimnmhp'), False)
        self.assertEqual(day5.is_nice('haegwjzuvuyypxyu'), False)
        self.assertEqual(day5.is_nice('dvszwmarrgswjxmb'), False)

    def test_is_supernice(self):
        self.assertEqual(day5.is_two_letters_twice('xyxy'), True)
        self.assertEqual(day5.is_two_letters_twice('aabcdefgaa'), True)
        self.assertEqual(day5.is_two_letters_twice('aaa'), False)
        self.assertEqual(day5.is_two_letters_twice('rxexcbwhiywwwwnu'), True)
        self.assertEqual(day5.is_sandwich('xyx'), True)
        self.assertEqual(day5.is_sandwich('xyyx'), False)
        self.assertEqual(day5.is_sandwich('abcdefeghi'), True)
        self.assertEqual(day5.is_sandwich('efe'), True)
        self.assertEqual(day5.is_sandwich('aaa'), True)
        self.assertEqual(day5.is_super_nice('qjhvhtzxzqqjkmpb'), True)
        self.assertEqual(day5.is_super_nice('xxyxx'), True)
        self.assertEqual(day5.is_super_nice('uurcxstgmygtbstg'), False)
        self.assertEqual(day5.is_super_nice('ieodomkazucvgmuy'), False)

if __name__ == "__main__":
    unittest.main()

import unittest

import day5


class Tests(unittest.TestCase):

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

    def test_is_nice_2(self):
        self.assertEqual(day5.is_twice_again('xyxy'), True)
        self.assertEqual(day5.is_twice_again('aabcdefgaa'), True)
        self.assertEqual(day5.is_twice_again('aaa'), False)
        #Jself.assertEqual(day5.is_vowel('aei'), True)
        #sJelf.assertEqual(day5.not_those('acpx'), True)
        #self.assertEqual(day5.is_nice('dvszwmarrgswjxmb'), False)



if __name__ == "__main__":
    unittest.main()

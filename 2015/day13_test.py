import unittest

import day13

test_text = """\
Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
"""


class DayThirteenTests(unittest.TestCase):

    def test_seats(self):
        parsed = day13.parse_text(test_text)
        self.assertEqual(parsed['Alice']['Bob'], 54)
        self.assertEqual(parsed['Bob']['Alice'], 83)
        self.assertEqual(parsed['Bob']['Carol'], -7)
        total_people = day13.total_people(parsed)
        self.assertEqual(set(total_people),
                         set(['Alice', 'Bob', 'Carol', 'David']))
        total_perms = day13.total_perms(total_people)
        self.assertEqual(len(list(total_perms)), 4 * 3 * 2)
        self.assertEqual(day13.rightneighbor((1, 2, 3), 0), 2)
        self.assertEqual(day13.rightneighbor((1, 2, 3), 2), 1)
        self.assertEqual(day13.leftneighbor((1, 2, 3), 0), 3)
        self.assertEqual(day13.leftneighbor((1, 2, 3), 2), 2)
        self.assertEqual(max(day13.score_perm(x, parsed) for x in total_perms),
                         330)

if __name__ == "__main__":
    unittest.main()

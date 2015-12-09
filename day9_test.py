import unittest

import day9


class DayNineTests(unittest.TestCase):

    def test_to(self):
        self.assertEqual(day9.to_parse('London to Dublin = 464'),
                         {('London', 'Dublin'): 464})

    def test_find_min(self):
        in_text = """\
London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141"""
        route = day9.route_from_text(in_text)
        self.assertEqual(route, {('London',  'Dublin'): 464,
                                 ('London',  'Belfast'): 518,
                                 ('Dublin', 'Belfast'): 141})
        cities = day9.cities_from_route(route)
        self.assertEqual(cities, set(['London', 'Dublin', 'Belfast']))
        self.assertEqual(len(list(day9.all_routes(cities))), 3*2*1)
        self.assertEqual(day9.score_route(
            ['Dublin', 'London', 'Belfast'],
            route), 982)


if __name__ == "__main__":
    unittest.main()

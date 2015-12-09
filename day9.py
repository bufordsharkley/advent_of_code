import itertools


def to_parse(string):
    from_stuff, dist = string.split(' = ')
    from_, to = from_stuff.split(' to ')
    return {(from_, to): int(dist)}


def route_from_text(text):
    resp = {}
    for line in text.splitlines():
        resp.update(to_parse(line))
    return resp


def cities_from_route(route):
    resp = set()
    for cities in route.keys():
        resp.add(cities[0])
        resp.add(cities[1])
    return resp


def all_routes(cities):
    return itertools.permutations(cities, len(cities))


def score_route(route, routes):
    total = 0
    for ii, _ in enumerate(route[:-1]):
        from_, to = route[ii: ii+2]
        try:
            total += routes[(from_, to)]
        except KeyError:
            total += routes[(to, from_)]
    return total


if __name__ == "__main__":
    # this isn't very good, but this is NP-hard, anyway, right?
    route = route_from_text(open('input/input9.txt').read())
    cities = cities_from_route(route)
    resp = []
    for rout in all_routes(cities):
        resp.append(score_route(rout, route))
    print min(resp)
    print max(resp)

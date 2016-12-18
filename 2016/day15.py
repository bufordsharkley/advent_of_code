import itertools


def process_disc(line):
    _, num, _, positions, _, _, _, _, _, _, _, zeropoz = line.split()
    return (int(num[1:]), (int(positions), int(zeropoz[:-1])))


def at_time(time, positions, zeropoz):
    return (time + zeropoz) % positions


def find_shortest_time_til_drop(discs):
    return next(x for x in itertools.count() if is_good_time(x, discs))


def is_good_time(time, discs):
    return not any(at_time(time + x, *discs[x]) for x in sorted(discs.keys()))


def main():
    assert find_shortest_time_til_drop({1: (5, 4), 2: (2, 1)}) == 5
    discs = dict(process_disc(x) for x in (line.strip() for line in open('input/15.txt')))
    print find_shortest_time_til_drop(discs)
    discs[max(discs.keys()) + 1] = (11, 0)
    print find_shortest_time_til_drop(discs)


if __name__ == "__main__":
    main()

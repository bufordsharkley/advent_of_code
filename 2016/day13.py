import itertools

MAX_DRAW = 60


def ones(num):
    return sum(1 for x in bin(num)[2:] if x=='1')


def print_walls(walls, marks):
    max_x = max(x[0] for x in walls.keys())
    max_y = max(x[1] for x in walls.keys())
    for y in range(max_y):
        for x in range(max_x):
            if (x, y) in marks:
                print '0',
                continue
            if walls[(x, y)]:
                print '#',
            else:
                print '.',
        print



def get_walls(fave):
    return {(x, y): is_wall(x, y, fave)
            for x in range(MAX_DRAW) for y in range(MAX_DRAW)}


def is_wall(x, y, fave):
    num = x * x + 3 * x + 2 * x * y + y + y * y + fave
    return bool(ones(num) % 2)


def get_possibilities(x, y):
    for i, j in ((-1, 0), (1, 0), (0, 1), (0, -1)):
        xp, yp = x + i, y + j
        if xp < 0 or yp < 0:
            continue
        yield (xp, yp)


def solve_maze(walls, target):
    tracker = {}
    tracker[0] = [((1,1),) ]
    for ii in itertools.count():
        paths = tracker[ii]
        tracker[ii + 1] = []
        for path in paths:
            for pos in get_possibilities(*path[-1]):
                if walls[pos] or pos in path:
                    continue
                if pos == target:
                    # before finishing, show possibilities:
                    total_up_to(50, walls, tracker)
                    return len(path)
                tracker[ii + 1].append(path + (pos,))


def total_up_to(num, walls, tracker):
    total = set()
    if num not in tracker:  # Don't have the data, sorry.
        return
    total = set(y for ii in range(num + 1) for x in tracker[ii] for y in x)
                #total.add(y)
                #pass
    print_walls(walls, marks=total)
    print 'total number of possible paths: {}'.format(len(total))


if __name__ == "__main__":
    fave = 10
    walls = get_walls(fave)
    print_walls(walls, marks=[(7,4)])
    test_ans = solve_maze(walls, (7, 4))

    print
    fave = 1350
    walls = get_walls(fave)
    print_walls(walls, marks=[(31, 39)])
    print
    part_one = solve_maze(walls, (31, 39))
    print part_one

    assert test_ans == 11
    assert part_one == 92

import copy


def raw():
    return {(ii, jj): 0 for ii in range(0, 100) for jj in range(0, 100)}


def neighbors((x, y)):
    return [(x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x, y - 1),
            (x, y + 1),
            (x + 1, y - 1),
            (x + 1, y),
            (x + 1, y + 1)]


def is_on(grid, point):
    try:
        return grid[point]
    except KeyError:
        return 0


def turn_on_corners(grid):
    for light in ((0, 0), (0, 99), (99, 0), (99, 99)):
        grid[light] = 1


def advance(grid):
    newgrid = copy.deepcopy(grid)
    for light, status in grid.items():
        count = sum(is_on(grid, x) for x in neighbors(light))
        if status and count in (2, 3):
            newgrid[light] = 1
        elif not status and count == 3:
            newgrid[light] = 1
        else:
            newgrid[light] = 0
    return newgrid


if __name__ == "__main__":
    grid = raw()
    for ii, line in enumerate(open('input/input18.txt')):
        for jj, token in enumerate(line):
            if token == '#':
              grid[ii, jj] = 1
    orig_grid = copy.deepcopy(grid)
    for ii in range(100):
        grid = advance(grid)
    print sum(grid.values())
    grid = orig_grid
    turn_on_corners(grid)
    for ii in range(100):
        grid = advance(grid)
        turn_on_corners(grid)
    print sum(grid.values())

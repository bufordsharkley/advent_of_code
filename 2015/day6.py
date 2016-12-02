def resolve_through(string):
    first, second = string.split(' through ')
    x1, y1 = resolve_xy(first)
    x2, y2 = resolve_xy(second)
    return [(ii, jj) for ii in range(x1, x2 + 1) for jj in range(y1, y2 + 1)]


def resolve_xy(string):
    return tuple(int(x) for x in string.split(','))


def raw():
    return {(ii, jj): 0 for ii in range(0, 1000) for jj in range(0, 1000)}


def process_instruct(grid, command, light, elvish=False):
    if elvish:
        if command == 'toggle':
            grid[light] += 2
        elif command == 'turn on':
            grid[light] += 1
        elif command == 'turn off':
            if grid[light]:
                grid[light] -= 1
        return grid
    else:
        if command == 'toggle':
            if grid[light]:
                grid[light] = 0
            else:
                grid[light] = 1
        elif command == 'turn on':
            if not grid[light]:
                grid[light] = 1
        elif command == 'turn off':
            if grid[light]:
                grid[light] = 0
        return grid


def process_instruct_line(grid, line, elvish=False):
    command, a, b, c = line.rsplit(' ', 3)
    through = ' '.join([a, b, c])
    for light in resolve_through(through):
        process_instruct(grid, command, light, elvish=elvish)


if __name__ == "__main__":
    grid = raw()
    for line in open('input/day6.txt'):
        process_instruct_line(grid, line)
    print sum(grid.values())
    grid = raw()
    for line in open('input/day6.txt'):
        process_instruct_line(grid, line, elvish=True)
    print sum(grid.values())

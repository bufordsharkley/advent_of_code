
def grud(x, y, fave):
    return x*x + 3*x + 2 *x *y + y + y*y + fave

def ones(num):
    return sum(1 for x in bin(num)[2:] if x=='1')

def print_grid(grid):
    max_row = max(x[0] for x in grid.keys())
    max_column = max(x[1] for x in grid.keys())
    for column in range(max_row):
        for row in range(max_column):
            if column == 31 and row == 31:
                print '0',
                continue
            if grid[(row, column)]:
                print '#',
            else:
                print '.',
        print

def print_seen(grid, seen):
    max_row = max(x[0] for x in grid.keys())
    max_column = max(x[1] for x in grid.keys())
    for column in range(max_row):
        for row in range(max_column):
            if grid[(row, column)]:
                print '#  ',
            else:
                if (row, column) in seen:
                    print '{:3}'.format(seen[(row, column)]),
                else:
                    print '.  ',
        print


def get_grid(maxi, fave):
    resp = {}
    for ii in range(maxi):
        for jj in range(maxi):
            if is_wall(ii, jj, fave):
                resp[(ii, jj)] = True
            else:
                resp[(ii, jj)] = False
    return resp


def is_wall(x, y, fave):
    g = grud(x, y, fave)
    on = ones(g)
    if sum([x, y]) == 1:
        print x, y, g, on, bool(on % 2)
    return bool(ones(g) % 2)


def get_possibilities(loc):
    for ii, jj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        trial = loc[0] + ii, loc[1] + jj
        if trial[0] < 0 or trial[1] < 0:
            continue
        yield trial


def solve_maze(grid, loc, count=0, seen=None, solution={1: 13}, history=None):
    if seen is None:
        seen = {}
    counts = []
    if count > solution[1]:
        return None, seen
    if history is None:
        history = tuple()
    print count, solution[1], loc, history
    if loc in seen and seen[loc] <= count:
        return None, seen
    #print loc, count, seen[loc] if loc in seen else None
    #print len(seen)
    seen[loc] = count
    for pos in get_possibilities(loc):
        if not grid[pos]:
            #if pos == (1, 1):
            if pos == (34, 45):
                solution[1] = count + 1
                return count + 1, seen
            else:
                if pos in seen and seen[pos] + 1 >= count:
                    continue
                history += pos
                counts.append(solve_maze(grid, pos, count=count+1, seen=seen, solution=solution, history=history))
    counts = [x[0] for x in counts if x[0] is not None]
    if not counts:
        return None, seen
    return min(counts), seen



if __name__ == "__main__":
    fave = 10
    maxi = 50
    grid = {(x, y): False for x in range(maxi) for y in range(maxi)}
    grid = get_grid(maxi, fave)
    print_grid(grid)

    ans, seen = solve_maze(grid, (7, 4))
    print print_seen(grid, seen)
    fave = 1350
    maxi = 55
    grid = get_grid(maxi, fave)
    print_grid(grid)
    ans, seen = solve_maze(grid, (31, 39))
    #ans, seen = solve_maze(grid, (31, 39))
    print print_seen(grid, seen)
    print ans
    import sys
    sys.exit(0)
    #print_grid(


import itertools

LOWEST = 62
LOWEST = 38
seen = {}

def process_input(lines):
    if lines == 1:
        #return set([('E', 1), ('HM', 1), ('LM', 1), ('HG', 2), ('LG', 3),
        #            ('XG', 1), ('XM', 1), ('DG', 1), ('DM', 1)])
        return set([('E', 1), ('SG', 1), ('SM', 1), ('PG', 1), ('PM', 1),
                    ('TG', 2), ('RG', 2), ('RM', 2), ('CG', 2), ('CM', 2),
                    ('TM', 3)])
        return set([('E', 1), ('SG', 1), ('SM', 1), ('PG', 1), ('PM', 1),
                    ('TG', 2), ('RG', 2), ('RM', 2), ('CG', 2), ('CM', 2),
                    ('TM', 3), ('XG', 1), ('XM', 1), ('DG', 1), ('DM', 1)])
        return set([('E', 1), ('HM', 1), ('LM', 1), ('HG', 2), ('LG', 3)])
        return set([('E', 4), ('HM', 3), ('LM', 4), ('HG', 4), ('LG', 4)])
        return set([('E', 3), ('HM', 3), ('LM', 3), ('HG', 4), ('LG', 4)])
    for line in lines:
        line = line[:-1]
        floor, contents = line.split(' floor contains ')
        if floor == 'The first':
            floor = 1
        elif floor == 'The second':
            floor = 2
        elif floor == 'The third':
            floor = 3
        elif floor == 'The fourth':
            floor = 4
        else:
            raise Exception(floor)
        print floor
        print contents.split(', ')

        print contents.split(' and ')


def group_into_floors(state):
    floors = {k: set() for k in range(1, 5)}
    for item, floor in state:
        floors[floor].add(item)
    return floors


def is_safe(state):
    # unsafe if microchip on floor with wrong generator
    floors = group_into_floors(state)
    for stuff in floors.values():
        chips = [x[:-1] for x in stuff if x.endswith('M')]
        gens = [x[:-1] for x in stuff if x.endswith('G')]
        for chip in chips:
            if not chip in gens and gens:
                return False
    return True


def turn_into_goal(state):
    resp = set()
    for item, _ in state:
        resp.add((item, 4))
    return resp


def find_possible_moves(state):
    elevator_floor = [x[1] for x in state if x[0] == 'E'][0]
    directions = [1, -1]
    if elevator_floor == 4:
        directions.remove(1)
    if elevator_floor == 1:
        directions.remove(-1)
    others = [x for x in group_into_floors(state)[elevator_floor] if x != 'E']
    resp = []
    for direction in directions:
        if direction > 0:
            for size in (2, 1):
                for combination in itertools.combinations(others, size):
                    resp.append((direction, combination))
        else:
            for size in (1, 2):
                for combination in itertools.combinations(others, size):
                    resp.append((direction, combination))
    return resp


def find_minimum(state, count=None):
    if count is None:
        count = 0
    global LOWEST
    if count - 1 >= LOWEST:
        return LOWEST
    goal = turn_into_goal(state)
    possibilities = []
    for move in find_possible_moves(state):
        new_state = transform(state, move)
        if new_state == goal:
            print 'FOUND ONE'
            LOWEST = count + 1
            return count + 1
        if not is_safe(new_state):
            continue
        # Check to see if worth pursuing
        if tuple(new_state) in seen:
            if count >= (seen[tuple(new_state)] - 1):
                continue
            else:
                #print count, seen[tuple(new_state)]
                seen[tuple(new_state)] = count
        possibilities.append(new_state)
    if tuple(state) not in seen or count < seen[tuple(state)]:
        seen[tuple(state)] = count
    if not len(seen) % 1000:
        print len(seen), LOWEST
    #for possibility in possibilities:
    if not possibilities:
        return 99999
    if count > LOWEST:
        return 99999
    return min(find_minimum(possibility, count + 1) for possibility in possibilities)


def transform(state, move):
    resp = set()
    for item, floor in state:
        if item == 'E' or item in move[1]:
            resp.add((item, floor + move[0]))
        else:
            resp.add((item, floor))
    return resp

def is_valid(state):
    stuff = [x[0] for x in state]
    assert 'E' in stuff
    chips = [x[:-1] for x in stuff if x.endswith('M')]
    gens = [x[:-1] for x in stuff if x.endswith('G')]
    assert set(chips) == set(gens)

if __name__ == "__main__":
    import sys
    #sys.setrecursionlimit(90000)
    test = """\
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""
    #text_input = [x.strip() for x in test.splitlines()]
    #text_input = [x.strip() for x in open('input/11.txt').readlines()]
    state = process_input(1)
    is_valid(state)
    #seen = set([tuple(state)])
    print find_minimum(state)
    possible_moves = find_possible_moves(state)
    #is_safe(goal)

import itertools

def parse_floors(lines):
    resp = set()
    used = {}
    for ii, line in enumerate(lines):
        if 'contains nothing relevant' in line:
            continue
        floor = ii + 1
        for chip in find_microchips(line):
            if chip not in used:
                used[chip] = str(len(used))
            resp.add((used[chip] + 'M', floor))
        for gen in find_generators(line):
            if gen not in used:
                used[gen] = str(len(used))
            resp.add((used[gen] + 'G', floor))
    resp.add(('E', 1))
    return resp


def find_microchips(line):
    return [chip.split()[-1]
            for chip in line.split('-compatible microchip')[:-1]]


def find_generators(line):
    return [chip.split()[-1]
            for chip in line.split(' generator')[:-1]]


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


def is_goal(state):
    for thing in state:
        if thing[1] != 4:
            return False
    return True


def find_minimum(state, seen=None):
    if seen is None:
        seen = set()
    possibilities = {0: [state]}
    count = 1
    while True:
        if not possibilities[count - 1]:
            raise Exception('Not possible')
        possibilities[count] = []
        for state in possibilities[count - 1]:
            for move in find_possible_moves(state):
                new_state = transform(state, move)
                if is_goal(new_state):
                    return count
                if not is_safe(new_state):
                    continue
                new_state = rebalance(new_state)
                if serialize(new_state) in seen:
                    continue
                seen.add(serialize(new_state))
                possibilities[count].append(new_state)
        count += 1


def serialize(state):
    return tuple(sorted(state))


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


def rebalance(state):
    # sort by floor, rename accordingly
    floors = {}
    for thing, floor in state:
        thing = thing[:-1]
        if not thing:
            continue
        if thing in floors:
            floors[thing] += floor
        else:
            floors[thing] = floor
    replacements = {}
    for ii, token in enumerate(sorted(floors.items(), key=lambda x: x[1])):
        if int(token[0]) != ii:
            replacements[token[0]] = str(ii)
    resp = set()
    for thing, floor in state:
        if not thing[:-1] in replacements:
            resp.add((thing, floor))
        else:
            resp.add((thing.replace(thing[:-1], replacements[thing[:-1]]), floor))
    return resp


if __name__ == "__main__":
    test = """\
The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
The second floor contains a hydrogen generator.
The third floor contains a lithium generator.
The fourth floor contains nothing relevant."""
    state = parse_floors([x.strip() for x in test.splitlines()])
    is_valid(state)
    print 'succesfully solved in ', find_minimum(state)
    state = parse_floors([x.strip() for x in open('input/11.txt').readlines()])
    is_valid(state)
    print 'successfully solved in ', find_minimum(state)
    # part b
    state = parse_floors([x.strip() for x in open('input/11.txt').readlines()])
    max_element = max(int(x[0][:-1]) for x in state if x[0] != 'E')
    state.add(('{}G'.format(max_element + 1), 1))
    state.add(('{}M'.format(max_element + 1), 1))
    state.add(('{}G'.format(max_element + 2), 1))
    state.add(('{}M'.format(max_element + 2), 1))
    print 'successfully solved in ', find_minimum(state)

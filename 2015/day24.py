import copy
import itertools
import operator


def optimize_sleigh(weights, divisions=3):
    goal_for_each = sum(weights) / divisions
    smallest = 1
    possibilities = []
    while smallest < len(weights) and not possibilities:
        for combo in itertools.combinations(weights, smallest):
            if sum(combo) != goal_for_each:
                continue
            remainder = get_remainder(weights, combo)
            if can_divide(remainder, goal_for_each, groups=divisions - 1):
                possibilities.append(combo)
        smallest += 1
    qes = {combo: quantum_entanglement(combo) for combo in possibilities}
    best = sorted(qes.items(), key=lambda x: x[1])[0][0]
    return {'1': best}


def get_remainder(full_list, substract_list):
    resp = copy.deepcopy(full_list)
    for x in substract_list:
        resp.remove(x)
    return resp


def can_divide(weights, goal, groups):
    if sum(weights) == goal and groups == 1:
        return True
    for ii in range(len(weights)):
        for combo in itertools.combinations(weights, ii):
            if sum(combo) != goal:
                continue
            return can_divide(get_remainder(weights, combo), goal, groups - 1)
    return False


def quantum_entanglement(weights):
    return reduce(operator.mul, weights, 1)

if __name__ == "__main__":
    weights = """\
1
3
5
11
13
17
19
23
29
31
41
43
47
53
59
61
67
71
73
79
83
89
97
101
103
107
109
113
"""
    weights = [int(x) for x in weights.splitlines()]
    compartments = optimize_sleigh(weights)
    winner = compartments['1']
    print winner
    print quantum_entanglement(winner)
    compartments = optimize_sleigh(weights, divisions=4)
    winner = compartments['1']
    print winner
    print quantum_entanglement(winner)



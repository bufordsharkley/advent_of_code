import copy
import random


def parse_arrow(string):
    return tuple(string.split(' -> '))


def parse_sig(string, vals=None):
    parts = string.split()
    if len(parts) == 1:
        return resolve(parts[0], vals)
    elif parts[1] == 'AND':
        return resolve(parts[0], vals) & resolve(parts[2], vals)
    elif parts[1] == 'OR':
        return resolve(parts[0], vals) | resolve(parts[2], vals)
    elif parts[1] == 'LSHIFT':
        return resolve(parts[0], vals) << int(parts[2])
    elif parts[1] == 'RSHIFT':
        return resolve(parts[0], vals) >> int(parts[2])
    elif parts[0] == 'NOT':
        return 2 ** 16 + ~ resolve(parts[1], vals)
    else:
        raise NotImplementedError


def resolve(string, vals):
    try:
        return int(string)
    except ValueError:
        pass
    try:
        return vals[string]
    except KeyError:
        raise NotReady


class NotReady(Exception):
    pass


def parse_line(line, vals):
    left, dest = parse_arrow(line)
    sig = parse_sig(left, vals)
    vals[dest] = sig


def clean(set_of_lines):
    # all assignments with ints at the left should be excluded
    return set(line for line in set_of_lines
               if not isinstance(parse_arrow(line)[0], int)
               and not line.endswith('-> b'))


def run_it(stored_lines, vals):
    while stored_lines:
        line = random.sample(stored_lines, 1)[0]
        try:
            parse_line(line, vals)
            stored_lines.remove(line)
        except NotReady:
            pass


if __name__ == "__main__":
    # this is apparently non-deterministic.
    # I get different answers at different times.
    # luckily, it worked for me the first time I ran it...
    lines = set([x.strip() for x in open('input/input7.txt').readlines()])
    vals = {}
    stored_lines = copy.deepcopy(lines)
    run_it(stored_lines, vals)
    answer = vals['a']
    print answer
    vals = {'b': answer}
    stored_lines = clean(lines)
    run_it(stored_lines, vals)
    print vals['a']

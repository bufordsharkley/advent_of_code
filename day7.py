def parse_arrow(string):
    return tuple(string.split(' -> '))

def parse_sig(string, vals=None):
    print string
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
        return 2 ** 16 +  ~ resolve(parts[1], vals)
        #return ~ resolve(parts[1], vals)
    else:
        raise NotImplementedError

def resolve(string, vals):
    try:
        return int(string)
    except ValueError:
        pass
    try:
        return vals[string]
    except:
        print string
        raise NotReady

class NotReady(Exception):
    pass

def parse_line(line, vals):
    left, dest = parse_arrow(line)
    sig = parse_sig(left, vals)
    vals[dest] = sig

def clean(set_of_lines):
    resp = set()
    for line in set_of_lines:
        left, right = parse_arrow(line)
        if isinstance(left, int):
            pass
        resp.add(line)
    return resp


if __name__ == "__main__":
    import random

    vals = {}
    stored_lines = set([x.strip() for x in open('input/input7.txt').readlines()])
    while stored_lines:
        line = random.sample(stored_lines, 1)[0]
        try:
            parse_line(line, vals)
            stored_lines.remove(line)
        except NotReady:
            stored_lines.add(line)
    print vals
    answer = vals['a']
    print vals['a']
    stored_lines = set([x.strip() for x in open('input/input7.txt').readlines()])
    stored_lines = clean(stored_lines)
    vals = {'b': answer}
    while stored_lines:
        line = random.sample(stored_lines, 1)[0]
        try:
            parse_line(line, vals)
            stored_lines.remove(line)
        except NotReady:
            stored_lines.add(line)

    print vals
    answer = vals['a']
    print vals['a']

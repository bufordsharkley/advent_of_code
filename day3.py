import collections


def main():
    print num_houses('>')
    print num_houses('^>v<')
    print num_houses('^v^v^v^v^v')
    print num_houses(open('/tmp/input3.txt').read())
    print num_houses_with_robo('^v')
    print num_houses_with_robo('^>v<')
    print num_houses_with_robo('^v^v^v^v^v')
    print num_houses_with_robo(open('/tmp/input3.txt').read())


def num_houses_with_robo(string):
    resp = collections.defaultdict(int)
    santa_x = santa_y = robo_x = robo_y = 0
    resp[(santa_x, santa_y)] += 1
    for ii, char in enumerate(string):
        if ii % 2:
            santa_x, santa_y = advance(santa_x, santa_y, char)
            resp[(santa_x, santa_y)] += 1
        else:
            robo_x, robo_y = advance(robo_x, robo_y, char)
            resp[(robo_x, robo_y)] += 1
    return len(resp)


def advance(x, y, char):
    if char == '>':
        x += 1
    elif char == 'v':
        y -= 1
    elif char == '<':
        x -= 1
    elif char == '^':
        y += 1
    return x, y


def num_houses(string):
    resp = collections.defaultdict(int)
    x = y = 0
    resp[(x, y)] += 1
    for char in string:
        x, y = advance(x, y, char)
        resp[(x, y)] += 1
    return len(resp)

if __name__ == "__main__":
    main()

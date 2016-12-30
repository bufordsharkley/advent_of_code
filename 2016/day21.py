def move(args, stuff, reverse=False):
    assert args[0] == 'position' and args[3] == 'position'
    gulp = list(stuff)
    src_poz = int(args[1])
    dst_poz = int(args[4])
    if reverse:
        src_poz, dst_poz = dst_poz, src_poz
    let = stuff[src_poz]
    del gulp[src_poz]
    gulp.insert(dst_poz, let)
    return ''.join(gulp)


def rotate(args, stuff, reverse=False):
    if args[0] == 'based':
        let = args[-1]
        shift = stuff.find(let)
        if reverse:
            if len(stuff) == 5:
                shift = {0: 1, 3: 2}[shift]
            elif len(stuff) == 8:
                print 'shift', shift
                shift = {3: 2, 4: 7, 6: 0, 7: 4, 5: 3, 1: 1, 2: 6}[shift]
            else:
                raise Exception(len(stuff))
        else:
            additional = 2 if shift >= 4 else 1
            shift += additional
        direction = 'right'
    else:
        shift = int(args[1])
        direction = args[0]
    shift = shift % len(stuff)
    if reverse:
        direction = 'right' if direction == 'left' else 'left'
    if direction == 'left':
        return stuff[shift:] + stuff[:shift]
    elif direction == 'right':
        return stuff[-shift:] + stuff[:-shift]
    else:
        raise Exception


def swap(args, stuff):
    if args[0] == 'position' and args[3] == 'position':
        poz1 = int(args[1])
        poz2 = int(args[4])
        let1 = stuff[poz1]
        let2 = stuff[poz2]
    else:
        let1 = args[1]
        let2 = args[4]
        poz1 = stuff.find(let1)
        poz2 = stuff.find(let2)
    gulp = list(stuff)
    gulp[poz2] = let1
    gulp[poz1] = let2
    return ''.join(gulp)


def reverse(args, stuff):
    assert args[0] == 'positions'
    assert args[2] == 'through'
    poz1 = int(args[1])
    poz2 = int(args[3])
    start = stuff[:poz1]
    resp = start + ''.join(reversed(stuff[poz1:poz2+1])) + stuff[poz2 + 1:]
    if len(resp) != len(stuff):
        raise Exception(args, stuff, start, resp)
    return resp


def parse(line, stuff):
    line = line.split()
    assert line[0] in ('move', 'rotate', 'swap', 'reverse')
    if line[0] == 'move':
        return move(line[1:], stuff)
    elif line[0] == 'rotate':
        return rotate(line[1:], stuff)
    elif line[0] == 'swap':
        return swap(line[1:], stuff)
    elif line[0] == 'reverse':
        return reverse(line[1:], stuff)
    else:
        raise Exception


def rev_parse(line, stuff):
    line = line.split()
    assert line[0] in ('move', 'rotate', 'swap', 'reverse')
    if line[0] == 'move':
        return move(line[1:], stuff, reverse=True)
    elif line[0] == 'rotate':
        return rotate(line[1:], stuff, reverse=True)
    elif line[0] == 'swap':
        return swap(line[1:], stuff)
    elif line[0] == 'reverse':
        return reverse(line[1:], stuff)
    else:
        raise Exception


TEST_INPUT = [
    'swap position 4 with position 0',
    'swap letter d with letter b',
    'reverse positions 0 through 4',
    'rotate left 1 step',
    'move position 1 to position 4',
    'move position 3 to position 0',
    'rotate based on position of letter b',
    'rotate based on position of letter d',
]

TEST_ANSWERS = {
    0: 'abcde',
    1: 'ebcda',
    2: 'edcba',
    3: 'abcde',
    4: 'bcdea',
    5: 'bdeac',
    6: 'abdec',
    7: 'ecabd',
    8: 'decab',
}

def main():
    stuff = 'abcde'
    results = {}
    for ii, instruction in enumerate(TEST_INPUT):
        results[ii] = stuff
        stuff = parse(instruction, stuff)
    results[ii + 1] = stuff
    total = len(TEST_INPUT)
    assert results == TEST_ANSWERS
    for ii, instruction in enumerate(reversed(TEST_INPUT)):
        stuff = rev_parse(instruction, stuff)
        idx = total - ii - 1
        print idx
        print stuff
        if stuff != results[idx]:
            print instruction, idx, stuff, results[idx]
            raise Exception

    bb = [x.strip() for x in open('input/21.txt').readlines()]
    results = {}
    stuff = 'abcdefgh'
    for ii, b in enumerate(bb):
        results[ii] = stuff
        stuff = parse(b, stuff)
    results[ii + 1] = stuff

    assert stuff == 'bfheacgd'
    stuff = 'fbgdceah'
    count = ii + 1
    total = len(bb)
    for ii, instruction in enumerate(reversed(bb)):
        print instruction, ii
        stuff = rev_parse(instruction, stuff)
        idx = total - ii - 1
        print idx
        print stuff
        if stuff != results[idx]:
            print instruction, idx, stuff, results[idx], [results[x] for x in (idx, idx + 1)]
            #raise Exception
    print stuff

if __name__ == "__main__":
    main()

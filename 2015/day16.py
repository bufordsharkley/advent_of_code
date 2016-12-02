import copy


def get_sues():
    sues = {}
    for line in open('input/input16.txt'):
        sue, rest = line.split(':', 1)
        suenum = int(sue.split()[1])
        sues[suenum] = {}
        for component in rest.strip().split(', '):
            item, num = component.split(': ')
            sues[suenum][item] = int(num)
    return sues


def filter_sues(sues, text, part_b=False):
    sues = copy.deepcopy(sues)
    for line in text.splitlines():
        item, num = line.split(': ')
        num = int(num)
        for sue, info in sues.items():
            if part_b:
                if item in info:
                    if item in ('cats', 'trees'):
                        if num >= sues[sue][item]:
                            del sues[sue]
                    elif item in ('pomeranians', 'goldfish'):
                        if num <= sues[sue][item]:
                            del sues[sue]
                    else:
                        if num != sues[sue][item]:
                            del sues[sue]
            else:
                if item in info and num != sues[sue][item]:
                    del sues[sue]
    return sues


if __name__ == "__main__":
    text = """\
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""
    orig_sues = get_sues()
    sues = filter_sues(orig_sues, text)
    assert len(sues.keys()) == 1
    print sues.keys()[0]
    sues = filter_sues(orig_sues, text, part_b=True)
    assert len(sues.keys()) == 1
    print sues.keys()[0]

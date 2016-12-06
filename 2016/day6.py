import collections

TEST = """\
eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""


def part_one(rows):
    return ''.join(collections.Counter(x).most_common(1)[0][0]
                   for x in zip(*rows))


def part_two(rows):
    return ''.join(collections.Counter(x).most_common()[-1][0]
                   for x in zip(*rows))


if __name__ == "__main__":
    test_input = [x.strip() for x in TEST.splitlines()]
    assert part_one(test_input) == 'easter'
    actual_input = [x.strip() for x in open('input/6.txt').readlines()]
    answer_part_one = part_one(actual_input)
    print(answer_part_one)

    assert part_two(test_input) == 'advent'
    answer_part_two = part_two(actual_input)
    print(answer_part_two)

    assert answer_part_one == 'ygjzvzib'
    assert answer_part_two == 'pdesmnoz'

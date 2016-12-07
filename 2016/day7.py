def separate(string):
    outsides = []
    insides = []
    while '[' in string:
        before, inside_bracket = string.split('[', 1)
        outsides.append(before)
        inside_bracket, string = inside_bracket.split(']', 1)
        insides.append(inside_bracket)
    outsides.append(string)
    return outsides, insides


def has_abba(string):
    return True if any((string[ii + 3] == x and string[ii + 1] == string[ii + 2]
                        and x != string[ii + 1])
                        for ii, x in enumerate(string[:-3])) else False


def find_all_abas(string):
    return [string[ii:ii + 3] for ii, x in enumerate(string[:-2])
            if string[ii + 2] == x and x != string[ii + 1]]


def is_valid_one(string):
    outsides, insides = separate(string)
    if any(has_abba(x) for x in insides):
        return False
    return True if any(has_abba(x) for x in outsides) else False


def is_valid_two(string):
    outsides, insides = separate(string)
    all_abas, all_babs = set(), set()
    for outside in outsides:
        all_abas.update(find_all_abas(outside))
    for inside in insides:
        all_babs.update(find_all_abas(inside))
    return True if set(reverse(x) for x in all_abas) & all_babs else False


def reverse(x):
    return ''.join([x[1], x[0], x[1]])


def main():
    input_text = [x.strip() for x in open('input/7.txt').readlines()]
    assert is_valid_one('abba[mnop]qrst')
    assert not is_valid_one('abcd[bddb]xyyx')
    assert not is_valid_one('aaaa[qwer]tyui')
    answer_part_one = sum(1 for x in input_text if is_valid_one(x))
    print(answer_part_one)
    assert is_valid_two('aba[bab]xyz')
    assert not is_valid_two('xyx[xyx]xyx')
    assert is_valid_two('aaa[kek]eke')
    assert is_valid_two('zazbz[bzb]cdb')
    answer_part_two = sum(1 for x in input_text if is_valid_two(x))
    print(answer_part_two)
    assert answer_part_one == 110
    assert answer_part_two == 242

if __name__ == "__main__":
    main()

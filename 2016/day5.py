from __future__ import print_function

import hashlib
import itertools


def md5(string):
    return hashlib.md5(string).hexdigest()


def first_interesting_index(text, starting_index):
    return next(itertools.islice((x for x in itertools.count(starting_index)
                                  if md5(text + str(x))[:5] == '00000'), 1))


def resolve_password(text):
    chars = 8
    index = 0
    resp = []
    while chars:
        index = first_interesting_index(text, index)
        hashed = md5(text + str(index))
        resp.append(hashed[5])
        chars -= 1
        index += 1
    return ''.join(resp)


def resolve_better_password(text):
    index = 0
    resp = []
    positions = {k: None for k in range(8)}
    while None in positions.values():
        index = first_interesting_index(text, index)
        hashed = md5(text + str(index))
        chunk = hashed[6]
        index += 1
        try:
            position = int(hashed[5])
            if positions[position] is None:
                positions[position] = chunk
        except (KeyError, ValueError):
            continue
    return ''.join(positions[ii] for ii in range(8))


def main():
    test_input = 'abc'
    real_input = 'ffykfhsq'
    assert first_interesting_index(test_input, 0) == 3231929
    assert first_interesting_index(test_input, 3231930) == 5017308
    assert resolve_password(test_input) == '18f47a30'
    answer_part_one = resolve_password(real_input)
    print(answer_part_one)
    assert answer_part_one == 'c6697b55'
    assert resolve_better_password(test_input) == '05ace8e3'
    answer_part_two = resolve_better_password(real_input)
    print(answer_part_two)
    assert answer_part_two == '8c35d1ab'


if __name__ == "__main__":
    main()

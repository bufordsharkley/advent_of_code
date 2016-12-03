def resolve_direction(direction):
    return {'U': (-1, 0),
            'L': (0, -1),
            'R': (0, 1),
            'D': (1, 0)}[direction]


def resolve_keypad_one(position):
    return str(position[0] * 3 + position[1] + 1)


def resolve_keypad_two(position):
    return {(0, 2): '1',
            (1, 1): '2',
            (1, 2): '3',
            (1, 3): '4',
            (2, 0): '5',
            (2, 1): '6',
            (2, 2): '7',
            (2, 3): '8',
            (2, 4): '9',
            (3, 1): 'A',
            (3, 2): 'B',
            (3, 3): 'C',
            (4, 2): 'D',}[position]


def resolve_string_to_new_position(string, position, is_valid_position):
    for direction in string:
        movement = resolve_direction(direction)
        trial_position = tuple(sum(x) for x in zip(position, movement))
        if is_valid_position(trial_position):
            position = trial_position
    return position


def is_valid_keypad_one_position(position):
    return not any(x < 0 or x > 2 for x in position)


def is_valid_keypad_two_position(position):
    return not sum(abs(2 - x) for x in position) > 2


def resolve_code(strings, initial, valid_position_test):
    position = initial
    resp = []
    for string in strings:
        position = resolve_string_to_new_position(string, position,
                                                  valid_position_test)
        resp.append(position)
    return resp


def resolve_code_one(strings):
    positions = resolve_code(strings,
                             initial=(1, 1),
                             valid_position_test=is_valid_keypad_one_position)
    return ''.join(resolve_keypad_one(x) for x in positions)


def resolve_code_two(strings):
    positions =  resolve_code(strings,
                              initial=(2, 0),
                              valid_position_test=is_valid_keypad_two_position)
    return ''.join(resolve_keypad_two(x) for x in positions)


def main():
    TEST_INPUT = ['ULL', 'RRDDD', 'LURDL', 'UUUUD']
    assert resolve_code_one(TEST_INPUT) == '1985'
    assert resolve_code_two(TEST_INPUT) == '5DB3'
    input_strings = open('input/2.txt').read().splitlines()
    code_part_one = resolve_code_one(input_strings)
    print(code_part_one)
    code_part_two = resolve_code_two(input_strings)
    print(code_part_two)
    assert code_part_one == '78985'
    assert code_part_two == '57DD8'

if __name__ == "__main__":
    main()

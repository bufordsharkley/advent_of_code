# For reference-- not actually used in code:
CARDINALS = {'NORTH': 0, 'SOUTH': 2, 'EAST': 1, 'WEST': 3}


def parse_move(move):
    return move[0], int(move[1:])


def update_direction(direction, turn):
    assert turn in 'RL'
    return (direction + (1 if turn == 'R' else -1)) % 4


def calculate_grid_offset(string):
    direction = 0  # North
    direction_sums = {k: 0 for k in range(4)}
    for move in string.split(', '):
        direction = update_direction(direction, move[0])
        direction_sums[direction] += int(move[1:])
    up = direction_sums[0] - direction_sums[2]
    right = direction_sums[1] - direction_sums[3]
    return abs(up) + abs(right)


def find_first_location_visited_twice(string):
    direction = 0  # North
    location = (0, 0)
    visited_locations = set()
    for move in string.split(', '):
        direction = update_direction(direction, move[0])
        sign = 1 if direction < 2 else -1
        length = int(move[1:])
        while length:
            if direction % 2:  # i.e. East or West
                location = location[0], location[1] + sign
            else:
                location = location[0] + sign, location[1]
            if location in visited_locations:
                return location
            visited_locations.add(location)
            length -= 1
    raise Exception("No location visited twice")


def main():
    assert calculate_grid_offset('R2, L3') == 5
    assert calculate_grid_offset('R2, R2, R2') == 2
    assert calculate_grid_offset('R5, L5, R5, R3') == 12
    assert find_first_location_visited_twice('R8, R4, R4, R8') == (0, 4)
    input_data = open('input/1.txt').read()
    answer_part_one = calculate_grid_offset(input_data)
    answer_part_two = sum(find_first_location_visited_twice(input_data))
    print(answer_part_one)
    print(answer_part_two)
    # Allow for refactoring with continued correct answers.
    assert answer_part_one == 353
    assert answer_part_two == 152

if __name__ == '__main__':
    main()

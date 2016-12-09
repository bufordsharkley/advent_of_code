def find_length_one(text):
    length = 0
    while text:
        try:
            token, marker = text.split('(', 1)
        except ValueError:  # It's final token.
            break
        length += len(token)
        marker, remaining = marker.split(')', 1)
        span, multiplier = tuple(int(x) for x in marker.split('x'))
        length += span * multiplier
        text = remaining[span:]
    length += len(text)
    return length


def find_length_two(text):
    length = 0
    while text:
        try:
            token, marker = text.split('(', 1)
        except ValueError:  # It's final token.
            break
        length += len(token)
        marker, remaining = marker.split(')', 1)
        span, multiplier = tuple(int(x) for x in marker.split('x'))
        length += find_length_two(remaining[:span]) * multiplier
        text = remaining[span:]
    length += len(text)
    return length


def main():
    assert find_length_one('ADVENT') == 6
    assert find_length_one('A(1x5)BC') == 7
    assert find_length_one('(3x3)XYZ') == 9
    input_text = open('input/9.txt').read().strip()
    answer_part_one = find_length_one(input_text)
    print(answer_part_one)
    assert answer_part_one == 107035
    assert find_length_two('ADVENT') == 6
    answer_part_two = find_length_two(input_text)
    print(answer_part_two)
    assert answer_part_two == 11451628995

if __name__ == "__main__":
    main()

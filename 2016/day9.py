def find_length(text, version=1):
    length = 0
    while text:
        try:
            token, marker = text.split('(', 1)
        except ValueError:  # It's final token.
            break
        length += len(token)
        marker, remaining = marker.split(')', 1)
        span, multiplier = tuple(int(x) for x in marker.split('x'))
        if version == 1:
            length += span * multiplier
        elif version == 2:
            length += find_length(remaining[:span], version=2) * multiplier
        text = remaining[span:]
    length += len(text)
    return length


if __name__ == "__main__":
    input_text = open('input/9.txt').read().strip()
    answer_part_one = find_length(input_text)
    print(answer_part_one)
    answer_part_two = find_length(input_text, version=2)
    print(answer_part_two)
    assert answer_part_one == 107035
    assert answer_part_two == 11451628995

def is_vowel(string):
    if sum(string.count(vowel) for vowel in 'aeiou') >= 3:
        return True
    return False


def is_twice(string):
    last = string[0]
    for char in string[1:]:
        if char == last:
            return True
        last = char
    return False


def not_those(string):
    for seq in ('ab', 'cd', 'pq', 'xy'):
        if seq in string:
            return False
    return True


def is_nice(string):
    return is_vowel(string) and is_twice(string) and not_those(string)


def is_two_letters_twice(string):
    tokens = (string[ii:ii+2] for ii, _ in enumerate(string[:-1]))
    tokens = tuple(_take_out_two_in_a_row(tokens))
    if len(set(tokens)) != len(tokens):
        return True
    return False


def _take_out_two_in_a_row(tokens):
    last = None
    for token in tokens:
        if token != last:
            yield token
            last = token
        else:
            last = None


def is_sandwich(string):
    for ii, _ in enumerate(string[:-2]):
        if string[ii] == string[ii + 2]:
            return True
    return False


def is_super_nice(string):
    return is_two_letters_twice(string) and is_sandwich(string)

if __name__ == "__main__":
    print sum(1 for line in open('input/input5.txt') if is_nice(line))
    print sum(1 for line in open('input/input5.txt') if is_super_nice(line))

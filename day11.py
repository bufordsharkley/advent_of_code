ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

STRAIGHTS = []
for ii, _ in enumerate(ALPHABET[:-2]):
    STRAIGHTS.append(ALPHABET[ii:ii+3])


def increment(string):
    length = len(string)
    resp = []
    index = 1
    carry = True
    while True:
        new_char, carry = increment_char(string[-index])
        resp.append(new_char)
        if not carry:
            break
        index += 1
    for ii in range(length - index):
        resp.append(string[length - index - ii - 1])
    return ''.join(reversed(resp))


def increment_char(char):
    if char == 'z':
        return ('a', True)
    return (chr(ord(char) + 1), False)


def is_increasing_straight(string):
    for straight in STRAIGHTS:
        if straight in string:
            return True
    return False


def is_clean_of_forbidden(string):
    for char in 'iol':
        if char in string:
            return False
    return True


def is_two_pair(string):
    # let's do this dumb
    last = None
    count = 0
    for ii, char in enumerate(string):
        if char == last:
            count += 1
            last = None
        else:
            last = char
    if count >= 2:
        return True
    return False


def is_valid(string):
    return (is_increasing_straight(string) and is_clean_of_forbidden(string) and
        is_two_pair(string))


def next_valid(string):
    while True:
        string = increment(string)
        if is_valid(string):
            return string

if __name__ == "__main__":
    newpassword = next_valid('hepxcrrq')
    print newpassword
    print next_valid(newpassword)

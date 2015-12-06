def main():
    total = 0
    for string in open('input/input5.txt'):
        if is_nice(string):
            total += 1
    print total


def is_vowel(string):
    total = 0
    for vowel in 'aeiou':
        total += string.count(vowel)
    if total >= 3:
        return True
    return False

def is_twice(string):
    last = string[0]
    for char in string[1:]:
        if char == last:
            return True
        last = char
    return False

def is_twice_again(string):
    bag = set()
    all_ = []
    for ii, _ in enumerate(string[:-1]):
        bag.add(string[ii:ii+2])
        all_.append(string[ii:ii+2])
    #if len(bag) != len(all_):
    #Jkj    print bag, all_
    #return True
    last = sorted(all_)[0]
    for spec in sorted(all_)[1:]:
        print spec, last
        if spec == last and spec[0] != spec[1]:
            return True
        last = spec
    return False
    print string
    return False
    raise Exception(bag, string)
    raise Exception(len(bag), len(string))


def not_those(string):
    for seq in ['ab', 'cd', 'pq', 'xy']:
        if seq in string:
            return False
    return True

def is_nice(string):
    return is_vowel(string) and is_twice(string) and not_those(string)


if __name__ == "__main__":
    main()

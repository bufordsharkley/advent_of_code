import hashlib
import itertools


def md5(string):
    return hashlib.md5(string).hexdigest()


def stretch_hash(string):
    for _ in range(2017):
        string = md5(string)
    return string


def find_first_triple_char(string):
    for ii, x in enumerate(string[:-2]):
        if x == string[ii + 1] == string[ii + 2]:
            return x
    return None


def has_quint(string, char):
    return (char * 5) in string


def triples(salt, part):
    hashbuffer = []
    for ii in itertools.count():
        saltii = '{}{}'.format(salt, ii)
        hash_ = md5(saltii) if part == 1 else stretch_hash(saltii)
        hashbuffer.append(hash_)
        if len(hashbuffer) < 1001:
            continue
        char = find_first_triple_char(hashbuffer.pop(0))
        if char is None:
            continue
        for hash_ in hashbuffer:
            if has_quint(hash_, char):
                yield ii - 1000
                break


def main():
    salt = 'cuanljph'

    test_one = triples('abc', 1)
    part_one = triples(salt, 1)
    test_two = triples('abc', 2)
    part_two = triples(salt, 2)
    for ii in range(64):
        a = next(test_one)
        b = next(part_one)
        c = next(test_two)
        d = next(part_two)
        print a, b, c, d
    assert a == 22728
    assert c == 22551


if __name__ == "__main__":
    main()

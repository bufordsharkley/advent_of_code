import itertools


def main():
    text = open('input/input13.txt').read()
    parsed = parse_text(text)
    totalpeople = total_people(parsed)
    totalperms = total_perms(totalpeople)
    print max((score_perm(x, parsed) for x in totalperms))

    totalpeople.add('me')
    parsed['me'] = {}
    for person in totalpeople:
        parsed['me'][person] = 0
        parsed[person]['me'] = 0
    totalperms = total_perms(totalpeople)
    print max((score_perm(x, parsed) for x in totalperms))


def parse_text(text):
    resp = {}
    for line in text.splitlines():
        words = line.split()
        person1 = words[0]
        person2 = words[-1][:-1]  # period
        gain = 1 if words[2] == 'gain' else -1
        gain = int(words[3]) * gain
        if person1 not in resp:
            resp[person1] = {}
        resp[person1][person2] = gain
    return resp


def total_people(parsed):
    return set(parsed.keys())  # trust it's well-formed


def total_perms(people):
    return list(itertools.permutations(people, len(people)))


def score_perm(perm, parsed):
    total = 0
    for ii, person in enumerate(perm):
        total += parsed[person][rightneighbor(perm, ii)]
        total += parsed[person][leftneighbor(perm, ii)]
    return total


def rightneighbor(perm, index):
    try:
        return perm[index + 1]
    except IndexError:
        return perm[0]


def leftneighbor(perm, index):
    try:
        return perm[index - 1]
    except IndexError:
        return perm[-1]

if __name__ == "__main__":
    main()

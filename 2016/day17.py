import hashlib
import itertools


def md5(string):
    return hashlib.md5(string).hexdigest()


def neighbor_rooms(x, y, path, code):
    walls = dict(zip('UDLR', md5(code + ''.join(path))[:4]))
    walls = {k: v not in 'bcdef' for k, v in walls.items()}
    for i, j, d in ((1, 0, 'D'), (0, 1, 'R'), (-1, 0, 'U'), (0, -1, 'L')):
        if not (0 <= x + i < 4 and 0 <= y + j < 4):
            continue
        if walls[d]:
            continue
        yield  ((x + i, y + j), d)


def main():
    code = 'ihgpwlah'
    code = 'dmypynyp'
    winners = []
    room = (0, 0)
    path = ()
    paths = {0: [((0, 0), '')]}
    for count in itertools.count():
        print count, len(paths[count])
        resp = []
        if not paths[count]:
            raise Exception(max(len(x) for x in winners))
        for room, path in paths[count]:
            for newroom, dir in neighbor_rooms(*room, path=path, code=code):
                #print newroom, path + dir
                if newroom == (3, 3):
                    winners.append(path + dir)
                    #raise Exception(path + dir)
                else:
                    resp.append((newroom, path + dir))
        paths[count + 1] = resp
    return


if __name__ == "__main__":
    main()

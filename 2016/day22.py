def parse_df(df):
    resp = {}
    for line in df[2:]:
        node, size, used, avail, percentage = line.split()
        assert size[-1] == 'T'
        assert avail[-1] == 'T'
        assert used[-1] == 'T'
        size = int(size[:-1])
        avail = int(avail[:-1])
        used = int(used[:-1])
        percentage = int(percentage[:-1])
        _, x, y = node.rsplit('/', 1)[1].split('-')
        x, y = (int(u[1:]) for u in (x, y))
        if (x, y) in resp:
            raise Exception
        resp[(x, y)] = {'size': size,
                        'avail': avail,
                        'used': used,
                        '%': percentage}
    return resp


def all_viable_pairs(dict_):
    seen = set()
    print len(dict_)
    for k1, v1 in dict_.items():
        for k2, v2 in dict_.items():
            #if (k1, k2) in seen or (k2, k1) in seen:
            #    continue
            if k1 == k2:
                continue
            if not v1['used']:
                continue
            if v1['used'] > v2['avail']:
                continue
            yield (k1, k2)
            seen.add((k1, k2))

def main():
    df = [x.strip() for x in open('input/22.txt').readlines()]
    df = parse_df(df)
    all_ = []
    for pair in all_viable_pairs(df):
        all_.append(pair)
    print len(all_)


if __name__ == "__main__":
    main()

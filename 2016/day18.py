def is_trap(*x):
    assert len(x) == 3
    return ''.join(x) in ('^^.', '.^^', '^..', '..^')


def next_row(row):
    resp = []
    for ii, x in enumerate(row):
        a = row[ii - 1] if ii > 0 else '.'
        b = x
        c = row[ii + 1] if ii < len(row) - 1 else '.'
        resp.append('^' if is_trap(a, b, c) else '.')
    return ''.join(resp)


def safe_tiles_for_rows(numrows, row, count=0):
    for _ in range(numrows):
        count += sum(1 for x in row if x == '.')
        row = next_row(row)
    return count


def main():
    x = open('input/18.txt').read().strip()
    assert safe_tiles_for_rows(3, '..^^.') == 6
    assert safe_tiles_for_rows(10, '.^^.^.^^^^') == 38
    assert safe_tiles_for_rows(10, '.^^.^.^^^^') == 38
    part_one = safe_tiles_for_rows(40, x)
    assert part_one == 1989
    return
    print part_one
    print safe_tiles_for_rows(400000, x)

if __name__ == "__main__":
    main()

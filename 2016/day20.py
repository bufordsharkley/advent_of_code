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

def compress(d):
  resp = []
  cur = None
  for x in d:
    if cur is not None:
      if x[0] < cur[1]:
        cur = cur[0], x[1]
      else:
        resp.append(cur)
        cur = x
    else:
      cur = x
  resp.append(cur)
  return resp


def main():
    d = [x.strip() for x in open('input/20.txt').readlines()]
    d = [x.split('-') for x in d]
    ranges = []
    d  = sorted((int(x[0]), int(x[1])) for x in d)
    lowest = 0
    all_ = set()
    for ii in d:
      print len(all_)
      for x in all_:
        if ii[0] <= x <= ii[1]:
          all_.remove(x)
      if lowest < ii[0]:
        for x in range(lowest, ii[0]):
          all_.add(x)
      lowest = ii[1] + 1

    print all_
    #ranges.append(range(int(x[0]), int(x[1])))
    #Jkfor x in ranges:

    return
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

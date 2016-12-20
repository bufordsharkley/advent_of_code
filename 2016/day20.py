def compressed(ranges):
  current = ranges[0]
  for first, last in ranges[1:]:
    if first < current[1]:
      current = current[0], max(last, current[1])
    else:
      yield current
      current = first, last
  yield current

if __name__ == "__main__":
    ranges = (x.strip() for x in open('input/20.txt').readlines())
    ranges = sorted([tuple(int(y) for y in x.split('-')) for x in ranges])
    lowest = 0
    valid_ips = []
    ranges = list(compressed(ranges))
    for first, last in compressed(ranges):
      if lowest < first:
        valid_ips.extend(range(lowest, first))
      lowest = last + 1
    print valid_ips[0]
    print len(valid_ips)

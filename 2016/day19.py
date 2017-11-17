num = 5

def last_elf(num):
  elfs = [x + 1 for x in range(num)]
  position = 1
  while len(elfs) > 1:
    if position == 0:
      position = len(elfs) % 2
      elfs = [x for ii, x in enumerate(elfs) if ii % 2]
    else:
      position = (1 + len(elfs)) % 2
      elfs = [x for ii, x in enumerate(elfs) if not ii % 2]
  return elfs[0]


def last_middle_old(num):
  elfs = [x + 1 for x in range(num)]
  while len(elfs) > 1:
    print elfs[len(elfs) // 2]
    del elfs[len(elfs) // 2]
    elfs.append(elfs.pop(0))


def moves(elfs):
  lenn = len(elfs)
  count = lenn
  ii = lenn // 2
  jump = 1 if lenn % 2 else 0
  while count > 1:
    if elfs[ii] is not None:
      print elfs[ii]
      elfs[ii] = None
      ii += jump
      jump = 0 if jump == 1 else 1
      count -= 1
    ii += 1
    if ii > (lenn - 1):
      ii = ii % lenn
    yield ii


def last_middle(num):
  elfs = {x: x + 1 for x in range(num)}
  for move in moves(elfs):
    pass
  print [x for x in elfs.values() if x is not None][0]


def main():
  assert last_elf(5) == 3
  num = 3001330
  num = 12
  last_middle_old(num)
  print
  last_middle(num)
  return
  last_middle(12)
  last_middle(num)


if __name__ == "__main__":
  main()

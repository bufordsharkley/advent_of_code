class Screen(object):

  def __init__(self):
    self._width = 50
    self._height = 6
    self._screen = {(ii, jj): False for ii in range(6) for jj in range(50)}

  def rect(self, a, b):
    for ii in range(b):
      for jj in range(a):
        self._screen[(ii, jj)] = True

  def rotate(self, by, row=None, column=None):
    if row is not None:
      row_copy = {k:v for k,v in self._screen.items() if k[0] == row}
      for jj in range(self._width):
        self._screen[(row, jj)] = row_copy[(row, (jj - by) % self._width)]
    if column is not None:
      column_copy = {k:v for k,v in self._screen.items() if k[1] == column}
      for ii in range(self._height):
        self._screen[(ii, column)] = column_copy[((ii - by) % self._height, column)]

  def display(self):
    for ii in range(6):
      for jj in range(50):
        print ' ' if not self._screen[(ii, jj)] else '*',
      print


def main():
    input_text = [x.strip() for x in open('input/8.txt').readlines()]
    screen = Screen()
    for line in input_text:
      if line.startswith('rect'):
        a, b = [int(x) for x in line.split()[1].split('x')]
        screen.rect(a=a, b=b)
      elif line.startswith('rotate'):
        rowcol, ii, by, num = line.split()[1:]
        assert by == 'by'
        num = int(num)
        ii = int(ii.split('=')[1])
        if rowcol == 'column':
          screen.rotate(column=ii, by=num)
        elif rowcol == 'row':
          screen.rotate(row=ii, by=num)
        else:
          raise Exception
      else:
        raise Exception(line)
    answer_part_one = sum(1 for x in screen._screen.values() if x)
    print(answer_part_one)
    assert answer_part_one == 128
    screen.display()

if __name__ == "__main__":
    main()

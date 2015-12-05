def is_twice_2(string):
  tokens = []
  for ii, _ in enumerate(string[:-1]):
    tokens.append(string[ii:ii+2])
  # process out two-in-a-row
  last = tokens[0]
  parsed = []
  parsed.append(last)
  for token in tokens[1:]:
    if token != last:
      parsed.append(token)
      last = token
    else:
      last = None
  if len(set(parsed)) != len(parsed):
    return True
  return False


def is_sandwich(string):
  for ii, _ in enumerate(string[:-2]):
    if string[ii] == string[ii + 2]:
      return True
  return False


def is_super_nice(string):
  return is_twice_2(string) and is_sandwich(string)


def main():
  print sum(1 for line in open('input/input5.txt') if is_super_nice(line))
    

if __name__ == "__main__":
  main()

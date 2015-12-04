def elevator(string):
    ups = string.count('(')
    downs = string.count(')')
    return ups - downs

inputtext = open('/tmp/input1.txt').read()


def first_to_basement(string):
    for ii, _ in enumerate(string):
        current = elevator(string[:ii+1])
        if current == -1:
            return ii + 1


def main():
    print elevator(inputtext)
    print first_to_basement(inputtext)

if __name__ == "__main__":
    main()

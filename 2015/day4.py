import hashlib


def find_lowest_hash(string, zeros=5):
    num = 0
    while True:
        hash = md5(combine(string, num))
        if hash[:zeros] == '0' * zeros:
            break
        num += 1
    return num


def md5(string):
    return hashlib.md5(string).hexdigest()


def combine(text, num):
    return '{}{}'.format(text, num)


def main():
    print find_lowest_hash('iwrupvqb')
    print find_lowest_hash('iwrupvqb', zeros=6)

if __name__ == "__main__":
    main()

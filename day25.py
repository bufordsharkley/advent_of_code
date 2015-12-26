def code_number((row, column)):
    n = row + column - 2
    return n * (n + 1) // 2 + column

def code(index):
    n = 1
    d = 20151125
    while n < index:
        d *= 252533
        d %= 33554393
        n += 1
    return d

if __name__ == "__main__":
    print code(code_number((2981, 3075)))




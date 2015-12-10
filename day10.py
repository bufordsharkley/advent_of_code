def looknsay(num):
    sofar = ''
    remainder = num
    while remainder:
        n, count, remainder = inarow(remainder)
        starter = str(count) + n
        sofar += starter
    return sofar

def inarow(num):
    first = num[0]
    count = 1
    for next_ in num[1:]:
        if next_ == first:
            count += 1
        else:
            break
    return first, count, num[count:]

if __name__ == "__main__":
    start = '1113222113'
    for ii in range(50):
        start = looknsay(int(start))
    print len(start)


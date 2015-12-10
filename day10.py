def looknsay(numstring):
    sofar = ''
    remainder = numstring
    parts = []
    total = 0
    index = 0
    length = len(numstring)
    while index < length:
        first = numstring[index]
        count = 1
        while index + count < length:
            next_ = numstring[index + count]
            if next_ != first:
                break
            count += 1
        parts.append(str(count))
        parts.append(first)
        index += count
    return ''.join(parts)


if __name__ == "__main__":
    numstring = '1113222113'
    for ii in range(50):
        numstring = looknsay(numstring)
        print ii + 1, len(numstring)


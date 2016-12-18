def translate(char):
    if char == '1':
        return '0'
    elif char == '0':
        return '1'
    else:
        return char

def checksum(text):
    resp = []
    for ii in range(0, len(text), 2):
        if text[ii] == text[ii + 1]:
            resp.append('1')
        else:
            resp.append('0')
    resp = ''.join(resp)
    if not len(resp) % 2:
        return checksum(resp)
    return resp


def dragon(text):
    a = text
    b = ''.join(reversed(a))
    b = ''.join(translate(x) for x in b)
    return '{}0{}'.format(a, b)


def fill_disk(length, text):
    while len(text) < length:
        text = dragon(text)
    return checksum(text[:length])


def main():
    assert dragon('1') == '100'
    assert dragon('0') == '001'
    assert dragon('11111') == '11111000000'
    assert dragon('111100001010') == '1111000010100101011110000'
    assert checksum('110010110100') == '100'
    disk = fill_disk(length=20, text='10000')
    print disk
    print fill_disk(length=272, text='11101000110010100')
    print fill_disk(length=35651584, text='11101000110010100')

if __name__ == "__main__":
    main()

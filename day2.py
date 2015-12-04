def surface_area(length, width, height):
    sides = (length * width, width * height, height * length)
    return 2 * sum(sides) + min(sides)


def ribbon(length, width, height):
    shortest = min(2 * length + 2 * width,
                   2 * width + 2 * height,
                   2 * height + 2 * length)
    bow = length * width * height
    return shortest + bow


def main():
    print surface_area(2, 3, 4)
    print surface_area(1, 1, 10)
    total = 0
    for line in open('/tmp/input2.txt'):
        dims = [int(x) for x in line.split('x')]
        total += surface_area(*dims)
    print total
    print ribbon(2, 3, 4)
    print ribbon(1, 1, 10)
    total = 0
    for line in open('/tmp/input2.txt'):
        dims = [int(x) for x in line.split('x')]
        total += ribbon(*dims)
    print total

if __name__ == "__main__":
    main()

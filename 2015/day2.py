def surface_area(length, width, height):
    sides = (length * width, width * height, height * length)
    return 2 * sum(sides) + min(sides)


def ribbon(length, width, height):
    shortest = min(2 * length + 2 * width,
                   2 * width + 2 * height,
                   2 * height + 2 * length)
    bow = length * width * height
    return shortest + bow


def sum_all_boxes(boxes, func):
    return sum(func(*dims_from_box(box)) for box in boxes)


def dims_from_box(boxline):
    return tuple(int(x) for x in boxline.split('x'))


def main():
    print sum_all_boxes(open('input/input2.txt').readlines(), surface_area)
    print sum_all_boxes(open('input/input2.txt').readlines(), ribbon)

if __name__ == "__main__":
    main()

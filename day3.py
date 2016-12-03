def is_triangle(trio):
    a, b, c = sorted(trio)
    return True if a + b > c else False


def group_into_trios(data):
    return (data[ii:ii + 3] for ii in range(0, len(data), 3))

if __name__ == '__main__':
    rows = [[int(x) for x in row.split()]
            for row in open('input/3.txt').read().splitlines()]
    count_part_one = sum(1 for trio in rows if is_triangle(trio))
    print(count_part_one)
    # Flatten all the columns from the original input into one list, and group
    trios = group_into_trios([x for column in zip(*rows) for x in column])
    count_part_two = sum(1 for trio in trios if is_triangle(trio))
    print(count_part_two)
    # Ensure answers still correct for refactoring
    assert count_part_one == 982
    assert count_part_two == 1826

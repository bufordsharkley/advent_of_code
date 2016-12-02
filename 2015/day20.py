import math

STOP_AT = 1000000
VERBOSE = True

def deliveries(house_num, lazy_elf=False):
    if lazy_elf:
        return 11 * sum(_get_divisors(house_num, stop_at_50=True))
    else:
        return 10 * sum(_get_divisors(house_num))


def _get_divisors(num, stop_at_50=False):
    for ii in range(1, int(math.floor(math.sqrt(num))) + 1):
        if not num % ii:
            mirror = num / ii
            if not stop_at_50 or mirror <= 50:
                yield ii
            if mirror != ii:
                if not stop_at_50 or ii <= 50:
                    yield mirror


def solve_min(goal, lazy_elf=False, verbose=VERBOSE):
    house_num = 1
    while True:
        if deliveries(house_num, lazy_elf=lazy_elf) >= goal:
            return house_num
        if not house_num % 1000:
            print house_num
        house_num += 1


if __name__ == "__main__":
    print solve_min(36000000)
    print solve_min(36000000, lazy_elf=True)

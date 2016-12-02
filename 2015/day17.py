import itertools

def main():
    containers = [int(line) for line in open('input/input17.txt')]
    ways = find_ways(150, containers)
    print len(ways)
    minimum = min([len(x) for x in ways])
    print len([x for x in ways if len(x) == minimum])


def find_ways(goal, containers):
    return [comb for ii in range(1, len(containers) + 1)
            for comb in itertools.combinations(containers, ii)
            if sum(comb) == goal]

if __name__ == "__main__":
    main()

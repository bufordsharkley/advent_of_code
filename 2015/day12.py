import json


def get_total_num(data, ignore_red=False):
    if isinstance(data, basestring):
        return 0
    elif isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(get_total_num(item, ignore_red=ignore_red) for item in data)
    elif isinstance(data, dict):
        if ignore_red and ('red' in data or 'red' in data.values()):
            return 0
        return sum(get_total_num(v, ignore_red=ignore_red)
                   for v in data.values())
    else:
        raise NotImplementedError(data)


def main():
    data = json.loads(open('input/input12.txt').read())
    print get_total_num(data)
    print get_total_num(data, ignore_red=True)


if __name__ == "__main__":
    main()

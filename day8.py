import ast
import re


def charlen(string):
    return len(string)


def actuallen(string):
    return len(ast.literal_eval(string))


def encodedlen(string):
    return len(re.escape(string)) + 2


if __name__ == "__main__":
    encoded_total = 0
    char_total = 0
    actual_total = 0
    for line in open('input/day8.txt', 'r'):
        line = line.strip()
        encoded_total += encodedlen(line)
        char_total += charlen(line)
        actual_total += actuallen(line)
    print char_total - actual_total
    print encoded_total - char_total

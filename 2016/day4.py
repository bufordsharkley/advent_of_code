from __future__ import print_function
import collections
import itertools


def is_real(string):
    payload, checksum = string.split('[')
    checksum = checksum[:-1]
    just_alpha = ''.join(x.lower() for x in payload if x.isalpha())
    # Maximum would be a 26-way tie, need to account for:
    counter = collections.Counter(just_alpha).most_common(26)
    groups = itertools.groupby(counter, lambda x: x[1])
    all_letters = (''.join(sorted([x[0] for x in group]))
                   for _, group in groups)
    return checksum == ''.join(all_letters)[:5]


def caesar(text):
    shift = get_sector_id(text) % 26
    # Filter out all non-letters, because why not
    return ''.join(chr(ord(letter) + shift if ord(letter) + shift <= ord('z')
                   else ord(letter) + shift - 26)
                   for letter in text if letter.isalpha())


def get_sector_id(string):
    return int(string.rsplit('-', 1)[1].split('[')[0])


def main():
    assert is_real('aaaaa-bbb-z-y-x-123[abxyz]') == True
    assert is_real('a-b-c-d-e-f-g-h-987[abcde]') == True
    assert is_real('not-a-real-room-404[oarel]') == True
    assert is_real('totally-real-room-200[decoy]') == False
    assert get_sector_id('totally-real-room-200[decoy]') == 200

    input_text = [x.strip() for x in open('input/4.txt').readlines()]
    answer_part_one = sum(get_sector_id(string) for string in input_text
                          if is_real(string))
    print(answer_part_one)
    assert caesar('qzmt-zixmtkozy-ivhz-343') == 'veryencryptedname'
    room = [x for x in input_text if 'north' in caesar(x)]
    assert len(room) == 1
    answer_part_two = get_sector_id(room[0])
    print(answer_part_two)
    assert answer_part_one == 245102
    assert answer_part_two == 324

if __name__ == '__main__':
    main()

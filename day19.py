import re

def backwards(replacer):
    resp = []
    for k, v in replacer:
        resp.append((v, k))
    return resp


def parse_replacer(text):
    return [line.split(' => ') for line in text.splitlines()]


def find_possibilities(replacer, inp):
    random.shuffle(replacer)
    for k, v in replacer:
        if k not in inp:
            continue
        for m in re.finditer(k, inp):
            yield inp[:m.start()] + v + inp[m.end():]

GLOBAL = {}

import random
from collections import deque
def steps_to_reach(replacer, inp, out, depth=0):
    if depth == 0:
        GLOBAL['visited'] = set()
        GLOBAL['smallest'] = 600
        GLOBAL['best'] = 99999
    if random.random() < .00001:
        print len(GLOBAL['visited']), len(inp), GLOBAL['smallest'], depth, GLOBAL['best']
    if inp == out:
        return depth
    if depth > GLOBAL['best']:
        return GLOBAL['best']
    if len(inp) < GLOBAL['smallest']:
        GLOBAL['smallest'] = len(inp)
    if inp in GLOBAL['visited']:
        return GLOBAL['best']
    GLOBAL['visited'].add(inp)
    steps = []
    for x in find_possibilities(replacer, inp):
        if depth == 0:
            print 'ANOTHER TOP PATH'
        answer = steps_to_reach(replacer, x, out, depth=depth+1)
        if answer < GLOBAL['best']:
            GLOBAL['best'] = answer
    if not steps:
        return GLOBAL['best']
    if min(steps) < GLOBAL['best']:
        GLOBAL['best'] = min(steps)
    return min(steps)
    raise Exception
    while mydeque:
        if random.random() < .001:
            print newest[1]
            #print CURRENT_BUCKET, len(buckets[CURRENT_BUCKET])
        #lowest_bucket = buckets[CURRENT_BUCKET]
        newest = mydeque.pop()
        #if len(newest) < min_len:
            #print 'NEW MIN: {}'.format(len(newest))
            #min_len = len(newest)
        #if len(newest) > max_len:
            #print 'NEW MAX: {}'.format(len(newest))
            #max_len = len(newest)
        if newest[0] in visited:
            continue
        if newest[0] == out:
            return newest[1]
        visited.add(newest[0])
        #if CURRENT_BUCKET + 1 not in buckets:
        #    buckets[CURRENT_BUCKET + 1] = set()
        mydeque.extendleft((x, newest[1] +1) for x in find_possibilities(replacer, newest[0]))
        #buckets[CURRENT_BUCKET + 1] |= set(find_possibilities(replacer, newest))

"""
import random
def steps_to_reach(replacer, inp, out):
    visited = set()
    buckets = {0: set([inp])}
    CURRENT_BUCKET = 0
    min_len = 500
    max_len = 500
    while buckets:
        if random.random() < .001:
            print CURRENT_BUCKET, len(buckets[CURRENT_BUCKET])
        lowest_bucket = buckets[CURRENT_BUCKET]
        try:
            newest = lowest_bucket.pop()
        except KeyError:
            CURRENT_BUCKET += 1
        if len(newest) < min_len:
            print 'NEW MIN: {}'.format(len(newest))
            min_len = len(newest)
        if len(newest) > max_len:
            print 'NEW MAX: {}'.format(len(newest))
            max_len = len(newest)
        if newest in visited:
            continue
        if newest == out:
            return CURRENT_BUCKET
        visited.add(newest)
        if CURRENT_BUCKET + 1 not in buckets:
            buckets[CURRENT_BUCKET + 1] = set()
        buckets[CURRENT_BUCKET + 1] |= set(find_possibilities(replacer, newest))
"""





"""
import random
def steps_to_reach(replacer, inp, out, depth=0):
    visited = set()
    queue = [(inp, 0)]
    from collections import defaultdict
    buckets = defaultdict(set)
    while queue:
        if random.random() < .001:
            print len(queue)
            print queue[0][1]

        newest = queue.pop(0)
        if newest[0] not in visited:
            if newest[0] == out:
                return newest[1]
            visited.add(newest[0])
            to_add = (x for x in find_possibilities(replacer, newest[0])
                      if x not in visited)
            queue.extend([(x, newest[1] + 1) for x in to_add])
        else:
            pass
            """




if __name__ == "__main__":
    inputtext = open('input/input19.txt').readlines()
    replacer = parse_replacer(''.join(inputtext[:-2]))
    inp = inputtext[-1].strip()
    print inp
    print len(set(find_possibilities(replacer, inp)))
    steps = steps_to_reach(backwards(replacer), inp, 'e')
    steps = steps_to_reach(replacer, 'e', inp)
    print steps

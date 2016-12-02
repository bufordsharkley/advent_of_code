import itertools

def fetch_itemshop():
    raw = """/
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5
null     0     0       0

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
null     0     0       0
"""
    raw = raw.splitlines()
    return {'weapons': _parse_table(raw[2:7]),
            'armor': _parse_table(raw[9:15]),
            'rings': _parse_table(raw[17:])}


def _parse_table(tablelines):
    resp = {}
    for line in tablelines:
        data = line.rsplit(None, 3)
        resp[data[0]] = {'cost': data[1], 'damage': data[2], 'armor': data[3]}
    return resp


class Player(object):

    def __init__(self, name, damage, armor, hit):
        self.name = name
        self.damage = damage
        self.armor = armor
        self.hit = hit


def run_turn(players):
    player1, player2 = players
    player2.hit -= player1.damage - player2.armor
    player1.hit -= player2.damage - player1.armor


def who_wins(players):
    while all(player.hit > 0 for player in players):
        run_turn(players)
    for player in players:
        if player.hit > 0:
            return player.name


def possibilities(itemshop):
    for weapon in itemshop['weapons']:
        for armor in itemshop['armor']:
            for ii in range(3):
                for rings in itertools.combinations(itemshop['rings'], ii):
                    yield {'weapon': weapon, 'armor': armor, 'rings': rings}


def get_gold_upgrade(possibility, itemshop):
    cost = 0
    player = Player('you', damage=0, armor=0, hit=100)
    player, cost = upgrade(player, cost,
                           itemshop['weapons'][possibility['weapon']])
    player, cost = upgrade(player, cost,
                           itemshop['armor'][possibility['armor']])
    for ring in possibility['rings']:
        player, cost = upgrade(player, cost, itemshop['rings'][ring])
    return player, cost


def upgrade(player, cost, stats):
    cost += int(stats['cost'])
    player.armor += int(stats['armor'])
    player.damage += int(stats['damage'])
    return player, cost


def main():
    itemshop = fetch_itemshop()
    cost_of_winning = []
    cost_of_losing = []
    for possibility in possibilities(itemshop):
        player, gold = get_gold_upgrade(possibility, itemshop)
        boss = Player('boss', hit=104, damage=8, armor=1)
        if who_wins([player, boss]) != 'boss':
            cost_of_winning.append(gold)
        if who_wins([player, boss]) == 'boss':
            cost_of_losing.append(gold)
    print len(cost_of_winning)
    print len(cost_of_losing)
    print min(cost_of_winning)
    print max(cost_of_losing)

if __name__ == "__main__":
    main()

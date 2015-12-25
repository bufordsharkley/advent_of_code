import copy
import random

SPELLS = {'poison': 173,
          'magic missile': 53,
          'recharge': 229,
          'shield': 113,
          'drain': 73}


class Wizard(object):

    @property
    def armor(self):
        if self.timers['shield']:
            return 7
        return 0

    def __init__(self, name, hit, mana, verbose=False):
        self.name = name
        self.damage = 0
        self.hit = hit
        self.mana = mana
        self.verbose = verbose
        self.timers = {'shield': 0, 'poison': 0, 'recharge': 0}

    @property
    def status(self):
        return '{} has {} hit points, {} armor, {} mana'.format(
            self.name, self.hit, self.armor, self.mana)

    def cast(self, spell):
        if spell in self.timers and self.timers[spell]:
            raise Exception('already running timer on {}'.format(spell))
        self.mana -= SPELLS[spell]
        if spell == 'poison':
            self.timers['poison'] = 6
        elif spell == 'magic missile':
            self.opponent.hit -= 4
        elif spell == 'recharge':
            self.timers['recharge'] = 5
        elif spell == 'shield':
            self.timers['shield'] = 6
        elif spell == 'drain':
            self.hit += 2
            self.opponent.hit -= 2
        else:
            raise NotImplementedError(spell)
        if self.verbose:
            print '{} casts {}.'.format(self.name, spell)

    def take_turn(self):
        self.process_timers()

    def process_timers(self):
        for spell, timer in self.timers.items():
            if not timer:
                continue
            self.timers[spell] -= 1
            if spell == 'poison':
                self.opponent.hit -= 3
                if self.verbose:
                    print 'Poison deals 3 damage; its ',
            elif spell == 'recharge':
                self.mana += 101
                if self.verbose:
                    print 'Recharge provides 101 mana; its ',
            elif spell == 'shield':
                if self.verbose:
                    print 'Shields ',
            else:
                raise NotImplementedError(spell)
            if self.verbose:
                print 'timer is now {}.'.format(self.timers[spell])

    def doable_spells(self):
        affordable = [x for x in SPELLS if SPELLS[x] <= self.mana]
        return [x for x in affordable if not  self.timers.get(x, 0)]


class Player(object):

    def __init__(self, name, damage, armor, hit, verbose=False):
        self.name = name
        self.damage = damage
        self.armor = armor
        self.hit = hit
        self.verbose = verbose

    @property
    def status(self):
        return '{} has {} hit points'.format(self.name, self.hit)

    def take_turn(self):
        self.opponent.process_timers()
        if self.hit <= 0:
            return
        damage = self.damage - self.opponent.armor
        if damage < 1:
            raise Exception
        if self.verbose:
            print '{} attacks for {} damage.'.format(self.name, damage)
        self.opponent.hit -= damage

def main():
    demo()
    #you = Wizard(name='Player', hit=10, mana=250)
    you = Wizard(name='Player', hit=50, mana=500)
    #boss = Player('Boss', damage=8, armor=0, hit=14)
    boss = Player('Boss', damage=9, armor=0, hit=51)
    spells = generate_winning_spells(you, boss)
    for x in spells:
        #print _score_spells(x)
        if _score_spells(x) == 847:
            print x
    print min(_score_spells(x) for x in spells)

def _score_spells(spells):
    return sum(SPELLS[x] for x in spells)

def generate_winning_spells(orig_wizard, orig_boss):
    wizard = copy.deepcopy(orig_wizard)
    boss = copy.deepcopy(orig_boss)
    spells = set()
    latest_min = 9999
    while True:
        try:
            random_spells = _generate_random_spell(wizard, boss)
            if random_spells not in spells:
                spells.add(random_spells)
        except Loss:
            pass
        print len(spells), latest_min
        if spells and not len(spells) % 1000:
            latest_min = sorted(list(set(sorted(_score_spells(x) for x in spells))))[:5]
        if len(spells) == 1000:
            break
    return spells


def _generate_random_spell(wizard, boss):
    wizard = copy.deepcopy(wizard)
    boss = copy.deepcopy(boss)
    wizard.opponent = boss
    boss.opponent = wizard
    current = []
    verbose = False
    while wizard.hit > 0 and boss.hit > 0:
        if verbose:
            print wizard.status, boss.status, wizard.timers
        if verbose:
            print '-player turn-'
        wizard.hit -= 1
        if boss.hit <=0:
            break
        wizard.take_turn()
        spells = wizard.doable_spells()
        if not spells:
            raise Loss
        random.shuffle(spells)
        spell = spells[0]
        wizard.cast(spell)
        current.append(spell)
        if verbose:
            print '-boss turn-'
        if boss.hit <=0:
            break
        boss.take_turn()
        if verbose:
            print wizard.status, boss.status, wizard.timers
    if wizard.hit > 0:
        return tuple(current)
    raise Loss


class Loss(Exception):
    pass


def fight(you, boss, spells, verbose=False):
    count = 0
    while you.hit > 0 and boss.hit > 0:
        if verbose:
            print you.status
            print boss.status
            print '- PLAYER TURN -'
        you.take_turn()
        if boss.hit <=0:
            break
        print count, you.hit, boss.hit
        try:
            spell = (spells.next())
            print count, spell
            you.cast(spell)
        except StopIteration:
            pass
        if verbose:
            print
            print you.status
            print boss.status
            print '- BOSS TURN -'
        boss.take_turn()
        if verbose:
            print
        count += 1

def demo():
    spells = (x for x in ['poison', 'magic missile', 'recharge', 'poison', 'magic missile', 'shield', 'magic missile'])
    you = Wizard(name='Player', hit=50, mana=500, verbose=True)
    boss = Player('Boss', damage=9, armor=0, hit=51, verbose=True)

    you.opponent = boss
    boss.opponent = you

    fight(you, boss, spells, verbose=True)
    print you.status
    print boss.status

    you = Wizard(name='Player', hit=10, mana=250)
    boss = Player('Boss', damage=8, armor=0, hit=13)

    you.opponent = boss
    boss.opponent = you
    spells = (x for x in ['poison', 'magic missile'])
    fight(you, boss, spells)

    print you.status
    print boss.status

    you = Wizard(name='Player', hit=10, mana=250)
    boss = Player('Boss', damage=8, armor=0, hit=14)
    you.opponent = boss
    boss.opponent = you
    spells = (x for x in ['recharge', 'shield', 'drain', 'poison', 'magic missile'])
    fight(you, boss, spells)

    print you.status
    print boss.status
    return



if __name__ == "__main__":
    main()

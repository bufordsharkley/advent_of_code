class Bot(object):

    def __init__(self, num):
        self.num = num
        self.high = None
        self.low = None

    def receive(self, value):
        if self.high is None and self.low is None:
            self.low = value
            return
        elif self.high is not None and self.low is not None:
            raise Exception('too many')
        elif self.low is not None:
            existing = self.low
        else:
            existing = self.high
        if sorted([value, existing]) == [17, 61]:
            print(self.num)
        if value > existing:
            self.high = value
            self.low = existing
        else:
            self.low = value
            self.high = existing

    def __repr__(self):
        return '<Bot, high: {} low: {}>'.format(self.high, self.low)

    def disperse(self, instruction, bots, outs):
        def _dispense(index, botornot, bots, outs, value):
            if botornot == 'bot':
                if index not in bots:
                    bot = Bot(index)
                    bots[index] = bot
                bots[index].receive(value)
            else:
                outs[index] = value


        highins = instruction['high']
        lowins = instruction['low']
        _dispense(highins[1], highins[0], bots, outs, self.high)
        _dispense(lowins[1], lowins[0], bots, outs, self.low)

        self.high = None
        self.low = None


def initially_distribute(vals):
    bots = {}
    for val, botnum in vals:
        if botnum not in bots:
            bot = Bot(botnum)
            bots[botnum] = bot
        else:
            bot = bots[botnum]
        bot.receive(val)
    return bots


def parse_input(text_input):
    vals = []
    instructions = {}
    for inp in text_input:
        assert inp.startswith('bot') or inp.startswith('value')
        if inp.startswith('bot'):
            blah = inp.split()
            _, botnum, _, _, _, lowbotorout, lowbot, _, _, _, highbotorout, highbot = blah
            instructions[int(botnum)] = {'low': (lowbotorout, int(lowbot)),
                                  'high': (highbotorout, int(highbot))}
        else:
            blah = inp.split()
            _, valnum, _, _, _, botnum = blah
            vals.append((int(valnum), int(botnum)))
    return vals, instructions


if __name__ == "__main__":
    text_input = [x.strip() for x in open('input/10.txt').readlines()]
    vals, instructions = parse_input(text_input)
    bots = initially_distribute(vals)
    outs = {}
    while True:
        for bot in bots.values():
            if bot.high is not None and bot.low is not None:
                bot.disperse(instructions[bot.num], bots, outs)
                break
        else:
            break
    print(outs[0] * outs[1] * outs[2])

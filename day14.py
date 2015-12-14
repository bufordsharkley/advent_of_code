class Reindeer(object):

    def __init__(self, fly, duration, rest):
        self.fly = fly
        self.duration = duration
        self.rest = rest
        self.position = 0
        self.tank = duration
        self.wait = rest
        self.time = 0

    def plus(self, seconds):
        while seconds:
            if self.tank:
                self.position += self.fly
                self.tank -= 1
                self.wait = self.rest
            else:
                self.wait -= 1
                if self.wait == 0:
                    self.tank = self.duration
            seconds -= 1
            self.time += 1

    def goto(self, seconds):  # used only for tests
        if self.time > seconds:
            raise Exception
        else:
            self.plus(seconds - self.time)

if __name__ == "__main__":
    reindeer = {
        'vixen': Reindeer(19, 7, 124),
        'rudolph': Reindeer(3, 15, 28),
        'donner': Reindeer(19, 9, 164),
        'blitzen': Reindeer(19, 9, 158),
        'comet': Reindeer(13, 7, 82),
        'cupid': Reindeer(25, 6, 145),
        'dasher': Reindeer(14, 3, 38),
        'dancer': Reindeer(3, 16, 37),
        'prancer': Reindeer(25, 6, 143),
        }
    points = {x: 0 for x in reindeer}
    for ii in range(2503):
        for rein in reindeer.values():
            rein.plus(1)
        maxpos = max(x.position for x in reindeer.values())
        for name, rein in reindeer.items():
            if rein.position == maxpos:
                points[name] += 1
    print max(x.position for x in reindeer.values())
    print max(points.values())

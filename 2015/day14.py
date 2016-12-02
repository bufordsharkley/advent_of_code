import operator


class Reindeer(object):

    def __init__(self, name, speed, stamina, rest):
        self.name = name
        self.speed = speed
        self.tank = self.stamina = stamina
        self.wait = self.rest = rest
        self.position = 0

    def move(self):
        if self.tank:
            self.position += self.speed
            self.tank -= 1
            self.wait = self.rest
        else:
            self.wait -= 1
            if not self.wait:
                self.tank = self.stamina

if __name__ == "__main__":
    reindeers = []
    for ln in open('input/input14.txt'):
        name, _, _, speed, _, _, stamina, _, _, _, _, _, _, rest, _ = ln.split()
        reindeers.append(Reindeer(name, int(speed), int(stamina), int(rest)))
    points = {x.name: 0 for x in reindeers}
    for ii in range(2503):
        for reindeer in reindeers:
            reindeer.move()
        current = sorted(reindeers, key=lambda x: x.position)[-1].name
        points[current] += 1
    print max(x.position for x in reindeers)
    print max(points.values())

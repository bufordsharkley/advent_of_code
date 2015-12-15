class Recipe(object):

    def __init__(self, capacity, durability, flavor, texture, calories):
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __mul__(self, n):
        return Recipe(self.capacity * n,
                      self.durability * n,
                      self.flavor * n,
                      self.texture * n,
                      self.calories * n)

    def __add__(self, other):
        return Recipe(self.capacity + other.capacity,
                      self.durability + other.durability,
                      self.flavor + other.flavor,
                      self.texture + other.texture,
                      self.calories + other.calories)

    def score(self):
        return self.capacity * self.durability * self.flavor * self.texture


def all_nonnegative_4tuples_that_sum_to_100():
    for ii in range(100):
        for jj in range(ii, 100):
            for kk in range(jj, 100):
                ll = 100 - ii - jj - kk
                if ll >= 0:
                    yield ii, jj, kk, ll


if __name__ == "__main__":
    all_ingredients = []
    for line in open('input/input15.txt'):
        name, _, capacity, _, durability, _, flavor, _, texture, _, calories = \
            line.split()
        all_ingredients.append(Recipe(int(capacity[:-1]),
                           int(durability[:-1]),
                           int(flavor[:-1]),
                           int(texture[:-1]),
                           int(calories)))
    assert len(all_ingredients) == 4  # not very robust, hmmm
    scores = []
    scores_500 = []
    frosting, candy, butterscotch, sugar = all_ingredients
    for a, b, c, d in all_nonnegative_4tuples_that_sum_to_100():
        r = frosting * a + candy * b + butterscotch * c + sugar * d
        if r.calories == 500:
            scores_500.append(r.score())
        scores.append(r.score())
    print max(scores)
    print max(scores_500)

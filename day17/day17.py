with open("input") as file:
    data = [line.rstrip() for line in file.readlines()][0]
    rules = data.split(" ")[2:]

area = []
for rule in rules:
    coords = rule.replace(',','').split("..")
    area.append((int(coords[0][2:]), int(coords[1])))

print(area)


class Probe:

    def __init__(self, v_x, v_y, target):
        self.x = 0
        self.y = 0
        self.v_x = v_x
        self.v_y = v_y
        self.target_x = target[0]
        self.target_y = target[1]

    def hit_target(self):
        return self.target_x[0] <= self.x <= self.target_x[1] and self.target_y[0] <= self.y <= self.target_y[1]

    def missed_target(self):
        return self.x > self.target_x[1] or self.y < self.target_y[0]

    def move(self):
        self.x += self.v_x
        self.y += self.v_y

        if self.v_x < 0:
            self.v_x += 1
        elif self.v_x > 0:
            self.v_x -= 1

        self.v_y -= 1

        return self.x, self.y

    def fire_probe(self):
        points = []

        while not (self.hit_target() or self.missed_target()):
            points.append(self.move())

        if self.missed_target():
            points.append((-1, -1))

        return points


maxes = []
options = set()
for x in range(1, area[0][1] + 1):
    for y in range(area[1][0] - 1, area[0][1]):
        p = Probe(x, y, area)
        points = p.fire_probe()
        if points[-1] != (-1, -1):
            maxes.append(max([b for a, b in points]))
            options.add((x, y))

# A: 5995
print("A:", max(maxes))
# B: 3202
print("B:", len(options))

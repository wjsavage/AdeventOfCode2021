with open("input") as file:
    lines = [line.rstrip() for line in file.readlines()]

points, folds = set(), []
gap = [i for i, x in enumerate(lines) if not x][0]

for line in lines[:gap]:
    split = line.split(',')
    points.add((int(split[0]), int(split[1])))

for line in lines[gap + 1:]:
    split = line.split(" ")[2].split('=')
    folds.append((split[0], int(split[1])))


def fold_points(points, fold):
    new_points = set()
    for point in points:
        if fold[0] == 'x' and point[0] > fold[1]:
            new_points.add((fold[1] - (point[0] - fold[1]), point[1]))
        elif fold[0] == 'y' and point[1] > fold[1]:
            new_points.add((point[0], fold[1] - (point[1] - fold[1])))
        else:
            new_points.add(point)
    return new_points


for i, fold in enumerate(folds):
    points = fold_points(points, fold)
    if i == 0:
        # A: 710
        print("A:", len(points))

height = max([y for x, y in points])
width = max([x for x, y in points])
plot = [[' ' for _ in range(width + 1)] for _ in range(height + 1)]

for point in points:
    plot[point[1]][point[0]] = "█"
# B: EPLGRULR
print(*plot, sep='\n')

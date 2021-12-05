import numpy as np

with open("input") as file:
    lines = [str(line.rstrip()).split(" ") for line in file.readlines()]


def is_hoz_or_vert_line(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]


def gen_points_on_line(a, b, use_diags=False):
    if a[0] == b[0]:
        return [(a[0], p) for p in range(a[1], b[1] + 1)]
    elif a[1] == b[1]:
        return [(p, a[1]) for p in range(a[0], b[0] + 1)]
    if use_diags:
        return [(a[0] + p, a[1] + p) for p in range(b[0] - a[0] + 1)] if a[1] < b[1]\
            else [(a[0] + p, a[1] - p) for p in range(b[0] - a[0] + 1)]
    return []


def add_points_to_grid_with_count(grid, points):
    for point in points:
        grid[point[1], point[0]] += 1
    return np.bincount(grid.copy().flatten())


lines = [(line[0].split(','), line[2].split(',')) for line in lines]
coords = [sorted([(int(seg[0]), int(seg[1])) for seg in line]) for line in lines]
grid_size = max([max(a[0], b[0]) for a, b in coords])
grid = np.full((grid_size + 1, grid_size + 1), 0, dtype=int)

points = [point for line in coords for point in gen_points_on_line(line[0], line[1]) if is_hoz_or_vert_line(line)]
diag_points = [point for line in coords for point in gen_points_on_line(line[0], line[1], True)
               if not is_hoz_or_vert_line(line)]
countsA, countsB = add_points_to_grid_with_count(grid, points), add_points_to_grid_with_count(grid, diag_points)

print("A:", sum(countsA[2:]), "B:", sum(countsB[2:]))

# A: 6005 B: 23864

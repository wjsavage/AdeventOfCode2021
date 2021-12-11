from collections import Counter

with open("input") as file:
    lines = [str(line.rstrip()).split(" ") for line in file.readlines()]


def gen_points_on_line(a, b, use_diags=False):
    if a[0] == b[0] or a[1] == b[1]:
        if not use_diags:
            return [(a[0], p) for p in range(a[1], b[1] + 1)] if a[0] == b[0] \
                else [(p, a[1]) for p in range(a[0], b[0] + 1)]
    elif use_diags:
        return [(a[0] + p, a[1] + p) for p in range(b[0] - a[0] + 1)] if a[1] < b[1]\
            else [(a[0] + p, a[1] - p) for p in range(b[0] - a[0] + 1)]
    return []


lines = [(line[0].split(','), line[2].split(',')) for line in lines]
coords = [sorted([(int(seg[0]), int(seg[1])) for seg in line]) for line in lines]
orth_points = [point for line in coords for point in gen_points_on_line(line[0], line[1])]
diag_points = [point for line in coords for point in gen_points_on_line(line[0], line[1], True)]

print("A:", len([y for x, y in Counter(orth_points).items() if y > 1]))
print("B:", len([y for x, y in Counter(orth_points + diag_points).items() if y > 1]))

# A: 6005 B: 23864

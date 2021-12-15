from collections import defaultdict
from itertools import repeat

with open("input") as file:
    rows = [list(map(int, list(line.rstrip()))) for line in file.readlines()]


def is_valid_pos(pos, m):
    return pos[0] in range(len(m)) and pos[1] in range(len(m[0]))


def search_grid(a, b, grid):

    queue = []
    point_costs = defaultdict(int)

    queue.append(a)

    while queue:
        cost, x, y = queue.pop(0)

        if x == b[0] and y == b[1]:
            return cost

        for x1, y1 in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if is_valid_pos((x1, y1), grid):
                new_cost = cost + grid[y1][x1]
                if (x1, y1) in point_costs.keys() and point_costs[(x1, y1)] <= new_cost:
                    continue
                point_costs[(x1, y1)] = new_cost
                queue.append((new_cost, x1, y1))
        queue = sorted(queue)
        print(queue)
# 423


# start = (0, 0, 0)
# end = (len(rows[0]) - 1, len(rows) - 1)
# print(search_grid(start, end, rows))


def inc(x, i):
    y = x + i
    return y if y < 10 else y % 9


big_grid = []
n = 5
for j in range(n):
    for row in rows:
        long_row = []
        for i, x in enumerate(repeat(row, n)):
            long_row = long_row + [inc(r, i + j) for r in x]
        big_grid.append(long_row)

start = (0, 0, 0)
end = (len(big_grid[0]) - 1, len(big_grid) - 1)
print(end)
print(big_grid[49][49])
# print(*big_grid, sep='\n')
print(search_grid(start, end, big_grid))




from collections import defaultdict
from itertools import repeat
import heapq

with open("input") as file:
    rows = [list(map(int, list(line.rstrip()))) for line in file.readlines()]


def is_valid_pos(pos, m):
    return pos[0] in range(len(m)) and pos[1] in range(len(m[0]))


def search_grid(a, grid):

    queue = []
    heapq.heapify(queue)
    heapq.heappush(queue, a)
    end = (len(grid[0]) - 1, len(grid) - 1)
    point_costs = defaultdict(int)

    while queue:
        cost, x, y = heapq.heappop(queue)

        if x == end[0] and y == end[1]:
            return cost

        for x1, y1 in [(x, y + 1), (x, y - 1), (x + 1, y), (x - 1, y)]:
            if is_valid_pos((x1, y1), grid):
                new_cost = cost + grid[y1][x1]
                if (x1, y1) in point_costs.keys() and point_costs[(x1, y1)] <= new_cost:
                    continue
                point_costs[(x1, y1)] = new_cost
                heapq.heappush(queue, (new_cost, x1, y1))



def inc(x, i):
    y = x + i
    return y if y < 10 else y % 9


def gen_grid_multiple(n, grid):
    large_grid = []
    for j in range(n):
        for row in grid:
            long_row = []
            for i, x in enumerate(repeat(row, n)):
                long_row = long_row + [inc(r, i + j) for r in x]
            large_grid.append(long_row)
    return large_grid


start = (0, 0, 0)
# A: 423
print("A:", search_grid(start, rows))

big_grid = gen_grid_multiple(5, rows)
# B: 2778
print("B:", search_grid(start, big_grid))




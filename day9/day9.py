with open("input") as file:
    rows = [list(map(int, list(line.rstrip()))) for line in file.readlines()]

n_cols, n_rows = len(rows[0]), len(rows)


def get_neighbours(i, j):
    neighbours = []
    if i != 0:
        neighbours.append((i - 1, j))
    if i != n_rows - 1:
        neighbours.append((i + 1, j))
    if j != 0:
        neighbours.append((i, j - 1))
    if j != n_cols - 1:
        neighbours.append((i, j + 1))

    return neighbours


def bfs_basin(i, j):
    visited = set()
    queue = [(i, j)]
    while queue:
        p1, p2 = queue.pop()
        visited.add((p1, p2))
        for k, l in get_neighbours(p1, p2):
            if rows[k][l] != 9 and (k, l) not in visited:
                queue.append((k, l))

    return len(visited)


risk_levels, basins = [], []

for i in range(n_rows):
    for j in range(n_cols):
        n = rows[i][j]
        neighbours = get_neighbours(i, j)
        neigh_val = [rows[i][j] for i, j in neighbours]

        if n < min(neigh_val):
            risk_levels.append(n + 1)
            basins.append((i, j))

# A: 550
print("A:", sum(risk_levels))

from functools import reduce
basin_sizes = sorted([bfs_basin(i, j) for i, j in basins], reverse=True)
# B: 1100682
print("B:", reduce((lambda x, y: x * y), basin_sizes[:3]))

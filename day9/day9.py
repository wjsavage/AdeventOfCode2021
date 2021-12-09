with open("input") as file:
    lines = [line.rstrip() for line in file.readlines()]

rows = []
for line in lines:
    row = [int(x) for x in line]
    rows.append(row)

n_cols = len(rows[0])
n_rows = len(rows)

risk_levels = []



def get_neighbours(i, j):
    neighbours = []
    # get hoz neighbours
    if i == 0:
        neighbours.append((i + 1,j))
    elif i == n_rows - 1:
        neighbours.append((i - 1, j))
    else:
        neighbours.append((i + 1, j))
        neighbours.append((i - 1, j))
    # then get vert neighbours
    if j == 0:
        neighbours.append((i, j + 1))
    elif j == n_cols - 1:
        neighbours.append((i, j - 1))
    else:
        neighbours.append((i, j + 1))
        neighbours.append((i, j - 1))

    return neighbours


# B thoughts
# this is a tree search method,
# start at each of the basins found in the previous part
# add that location to the queue
# while there are elements in the queue
    # pop the top
    # add its i, j to the visited set
    # increment basin accumulator
    # get all of its neighbours
    # for those that are not of value 9 and that are have not been visited
        # add their i, j to the queue
# return basin accumulator

def bfs_basin(i, j):
    visited = set()
    queue = []
    count = 0
    queue.append((i,j))
    while queue:
        p1, p2 = queue.pop()
        if rows[p1][p2] == 9 or (p1, p2) in visited:
            pass
        else:
            visited.add((p1,p2))
            count += 1
            for k, l in get_neighbours(p1, p2):
                queue.append((k, l))

    return count

basins = []

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

# B
basin_sizes = []
for i, j in basins:
    basin_sizes.append(bfs_basin(i, j))

from functools import reduce
import heapq

print("B:", reduce((lambda x, y: x * y), heapq.nlargest(3, basin_sizes)))
with open("input") as file:
    rows = [list(map(int, list(line.rstrip()))) for line in file.readlines()]

n_cols, n_rows = len(rows[0]), len(rows)
# print(*rows, sep='\n')


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
    if i != 0 and j != 0: # top left diag
        neighbours.append((i - 1, j - 1))
    if i != 0 and j != n_cols - 1: # bottom left diag
        neighbours.append((i - 1, j + 1))
    if i != n_rows - 1 and j != n_cols - 1:  # bottom right diag
        neighbours.append((i + 1, j + 1))
    if i != n_rows - 1 and j != 0: # top right diag
        neighbours.append((i + 1, j - 1))

    return neighbours


# print([rows[i][j] for i, j in get_neighbours(1,1)])

simal = -1
total_flashes = 0
for i in range(1_000_000):
    flashed = set()
    ready_to_flash = set()

    if all(n == 0 for row in rows for n in row):
        print(i)
        break
    # First, the energy level of each octopus increases by 1.
    for k in range(n_rows):
        for l in range(n_cols):
            rows[k][l] += 1
            if rows[k][l] > 9:
                ready_to_flash.add((k,l))

    # print(*rows, sep='\n')

    while ready_to_flash:
        # any octopus with an energy level greater than 9 flashes
        octo = ready_to_flash.pop()

        flashed.add(octo)
        rows[octo[0]][octo[1]] = 0
        neighs = get_neighbours(octo[0], octo[1])
        for k, l in neighs:
            if (k, l) not in flashed:
                rows[k][l] += 1
                if rows[k][l] > 9:
                    ready_to_flash.add((k,l))

        # print()
        # print(*rows, sep='\n')

    total_flashes += len(flashed)
print(total_flashes)

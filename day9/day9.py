with open("input") as file:
    lines = [line.rstrip() for line in file.readlines()]

rows = []
for line in lines:
    row = [int(x) for x in line]
    rows.append(row)

n_cols = len(rows[0])
n_rows = len(rows)

risk_levels = []

for i in range(n_rows):
    for j in range(n_cols):
        n = rows[i][j]
        neighbours = []
        # get hoz neighbours
        if i == 0:
            neighbours.append(rows[i + 1][j])
        elif i == n_rows - 1:
            neighbours.append(rows[i - 1][j])
        else:
            neighbours += [rows[i-1][j], rows[i+1][j]]
        # then get vert neighbours
        if j == 0:
            neighbours.append(rows[i][j+1])
        elif j == n_cols - 1:
            neighbours.append(rows[i][j-1])
        else:
            neighbours += [rows[i][j-1], rows[i][j + 1]]

        if n < min(neighbours):
            risk_levels.append(n + 1)

print(sum(risk_levels))

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
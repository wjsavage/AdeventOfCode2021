with open("input") as file:
    lines = [line.rstrip() for line in file.readlines()]

point_map_a = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

point_map_b = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

chunk_map = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
}

line_scores = []
incompletes = []
for line in lines:
    open_queue = []
    corrupted = False
    for char in line:
        if char in chunk_map.keys():
            open_queue.append(char)
        else:
            if char != chunk_map[open_queue.pop()]:
                corrupted = True
                line_scores.append(point_map_a[char])

        if corrupted: break
    if not corrupted:
        incompletes.append(open_queue)

# A: 166191
print("A:", sum(line_scores))

from functools import reduce
incomplete_scores = []
for stack in incompletes:
    scores = [0] + [point_map_b[r] for r in stack[::-1]]
    incomplete_scores.append(reduce((lambda x, y: 5 * x + y), scores))

incomplete_scores.sort()
i = int((len(incomplete_scores) + 1) / 2) - 1
# B: 1152088313
print("B:", incomplete_scores[i])

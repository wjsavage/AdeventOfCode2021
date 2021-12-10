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
            chuck_last = open_queue.pop()
            if char == chunk_map[chuck_last]:
                pass
            else:
                corrupted = True
                line_scores.append(point_map_a[char])
        if corrupted: break
    if not corrupted:
        incompletes.append(open_queue)

print("A:", sum(line_scores))

incomplete_scores = []
for stack in incompletes:
    score = 0
    for opener in stack[::-1]:
        score = 5 * score + point_map_b[opener]
    incomplete_scores.append(score)

incomplete_scores.sort()
i = int((len(incomplete_scores) + 1) / 2) - 1
print(incomplete_scores[i])

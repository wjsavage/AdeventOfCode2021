
with open("input") as file:
    lines = [int(line.rstrip()) for line in file.readlines()]

# A
# answer: 1288
print("A:", sum([x < y for x, y in zip(lines, lines[1:])]))

# B
# answer: 1311
sums = [sum(x) for x in zip(lines, lines[1:], lines[2:])]
print("B:", sum([x < y for x, y in zip(sums, sums[1:])]))

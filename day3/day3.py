from collections import Counter
import re

with open("input") as file:
    lines = [str(line.rstrip()) for line in file.readlines()]

cols = []
for i in range(len(lines[0])):
    digits = []
    for line in lines:
        digits.append(line[i])
    cols.append(digits)

# A
# answer: 3912944

bin = ""
for col in cols:
    c = Counter(col)
    if c['0'] < c['1']:
        bin += '1'
    else:
        bin += '0'

gamma = int(bin, 2)
eps = (~gamma & 0xFFF)
print("A:", gamma * eps)

# B
# answer: 4996233


def part_b(a, b):
    regex = ''
    rows = lines.copy()

    while rows:
        p = re.compile('^' + regex)
        rows = list(filter(p.match, lines))

        count = Counter([row[len(regex)] for row in rows])
        if len(count.keys()) == 1:
            break

        if count['0'] > count['1']:
            regex += a
        else:
            regex += b

    return rows[0]


ox = part_b('0', '1')
co = part_b('1', '0')

print("B:", int(ox, 2) * int(co, 2))


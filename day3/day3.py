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
bin2 = ""
for col in cols:
    c = Counter(col)
    if c['0'] < c['1']:
        bin += '1'
        bin2 += '0'
    else:
        bin += '0'
        bin2 += '1'

gamma = int(bin, 2)
eps = int(bin2, 2)
print("A:", gamma * eps)

# B
# answer: 4996233


regex = ''
rows = lines.copy()
i = 0

while rows:
    p = re.compile('^' + regex)
    rows = list(filter(p.match, lines))

    cols = [row[len(regex)] for row in rows]
    c = Counter(cols)
    if len(c.keys()) == 1:
        break

    if c['0'] > c['1']:
        regex += '0'
    else:
        regex += '1'

ox = rows[0]

regex = ''
rows = lines.copy()

while rows:
    p = re.compile('^' + regex)
    rows = list(filter(p.match, lines))

    cols = [row[len(regex)] for row in rows]
    c = Counter(cols)
    if len(c.keys()) == 1:
        break

    if c['0'] <= c['1']:
        regex += '0'
    else:
        regex += '1'

co = rows[0]

print("B:", int(ox, 2) * int(co, 2))


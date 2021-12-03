from collections import Counter

with open("input") as file:
    lines = [str(line.rstrip()) for line in file.readlines()]

# print(len(lines[0]))
cols = []
for i in range(len(lines[0])):
    digits = []
    for line in lines:
        digits.append(line[i])
    cols.append(digits)

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
import re


regex = ''
rows = lines.copy()
i = 0

while rows:
    if i > len(lines[0]) - 1:
        break

    cols = [row[i] for row in rows]
    c = Counter(cols)

    if '0' not in c.keys():
        regex += '1'
        break
    if '1' not in c.keys():
        regex += '0'
        break

    if c['0'] > c['1']:
        regex += '0'
    else:
        regex += '1'
    p = re.compile('^'+regex)
    rows = [line for line in lines if p.match(line)]

    i += 1

p = re.compile('^'+regex)
rows = [line for line in lines if p.match(line)]
ox = rows[0]

regex = ''
rows = lines.copy()
i = 0

while rows:
    if i > len(lines[0]) - 1:
        break

    cols = [row[i] for row in rows]
    c = Counter(cols)
    if '0' not in c.keys():
        regex += '1'
        break
    if '1' not in c.keys():
        regex += '0'
        break
    if c['0'] <= c['1']:
        regex += '0'
    elif c['1'] == c['0']:
        regex += '0'
    else:
        regex += '1'
    p = re.compile('^'+regex)
    rows = [line for line in lines if p.match(line)]

    i += 1

p = re.compile('^'+regex)
rows = [line for line in lines if p.match(line)]
co = rows[0]

print("B:", int(ox, 2) * int(co, 2))


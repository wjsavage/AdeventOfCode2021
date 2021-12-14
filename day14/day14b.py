from collections import Counter, defaultdict
with open("input") as file:
    lines = [line.rstrip() for line in file.readlines()]

template = lines[0]
gap = [i for i, x in enumerate(lines) if not x][0]

insertion_rules = {}

for line in lines[gap + 1:]:
    split = line.split(" -> ")
    insertion_rules[split[0]] = split[1]

pairs = defaultdict(int)
counts = {}

for i, val in enumerate(template[:-1]):
    pairs[val + template[i+1]] += 1

for i in range(40):
    new_pairs = pairs.copy()
    for p in pairs.keys():
        if p in insertion_rules.keys() and pairs[p] > 0:
            new_ps = insertion_rules[p]
            c = pairs[p]
            new_pairs[p[0] + new_ps] += c
            new_pairs[new_ps + p[1]] += c
            new_pairs[p] -= c

    pairs = new_pairs

c = defaultdict(int)
for k, v in pairs.items():
    c[k[1]] += v
c['N'] += 1
print("B:", max(c.values()) - min(c.values()))


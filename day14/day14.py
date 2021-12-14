from collections import Counter
with open("input") as file:
    lines = [line.rstrip() for line in file.readlines()]

template = lines[0]
gap = [i for i, x in enumerate(lines) if not x][0]

insertion_rules = {}

for line in lines[gap + 1:]:
    split = line.split("->")
    k = split[0].rstrip()
    insertion_rules[k] = split[1].strip()

print(insertion_rules)
print(template)

for n in range(10):
    tot = 0
    new = list(template)[:]
    for i, val in enumerate(template[:-1]):
        k = val+template[i+1]
        if k in insertion_rules.keys():
            before = new[:i + tot + 1]
            after = new[i + tot + 1:]
            mid = [insertion_rules[k]]
            new = before + mid + after
            tot += 1
    template = "".join(new)
    print(n, len(template), template)


c = Counter(template)
print(c)
print(max(c.values()) - min(c.values()))
from collections import Counter, defaultdict

with open("input") as file:
    line = [str(line.rstrip()).split(",") for line in file.readlines()]
    school = Counter([int(x) for x in line[0]])

for i in range(256):
    new_school = defaultdict(int)
    for k, v in school.items():
        if k-1 < 0:
            new_school[8] += v
            new_school[6] += v
        else:
            new_school[k-1] += v

    school = new_school

print(sum(school.values()))

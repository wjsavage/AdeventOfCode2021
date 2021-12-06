from collections import Counter, defaultdict

with open("input") as file:
    line = [str(line.rstrip()).split(",") for line in file.readlines()]
    school1 = [int(x) for x in line[0]]

school = defaultdict(int)
for k, v in Counter(school1).items():
    school[k] = v

print(school)


def dec_days(school):
    new_school = defaultdict(int)
    six_count = 0
    for k, v in school.items():
        new_k = k-1
        if new_k < 0:
            new_school[8] = v
            six_count += v
        else:
            new_school[new_k] = v

    new_school[6] += six_count
    return new_school

for i in range(256):
    school = dec_days(school)
    print(i, school)

print(school.values())
print(sum(school.values()))
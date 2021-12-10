from collections import Counter, defaultdict

with open("input") as file:
    line = [str(line.rstrip()).split(",") for line in file.readlines()]
    school = Counter([int(x) for x in line[0]])


def dec_days(school):
    new_school = defaultdict(int)
    for k, v in school.items():
        new_k = k - 1
        if new_k < 0:
            new_school[8] += v
            new_school[6] += v
        else:
            new_school[new_k] += v

    return new_school


def school_size_on_day_n(school, n):
    for _ in range(n):
        school = dec_days(school)
    return sum(school.values())

# A: 355386
print("A:", school_size_on_day_n(school, 80))
# B: 1613415325809
print("B:", school_size_on_day_n(school, 256))


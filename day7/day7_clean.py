from collections import Counter
from math import floor, ceil
from statistics import median, mean

with open("input") as file:
    crabs = list(map(int, [line.rstrip().split(",") for line in file.readlines()][0]))

md, mn = median(crabs), mean(crabs)
fuel_cost_b = lambda n: n * (n + 1) / 2

print("A:", sum([abs(x - md) for x in crabs]))
print("B:", min(sum([fuel_cost_b(abs(x - floor(mn))) for x in crabs]),
                sum([fuel_cost_b(abs(x - ceil(mn))) for x in crabs])))

# A: 339321
# B: 95476244

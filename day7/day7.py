from collections import Counter

with open("input") as file:
    line = [str(line.rstrip()).split(",") for line in file.readlines()]
    crabs = Counter([int(x) for x in line[0]])


def fuel_req_to_move(i, crabs, a_mode):
    moves = []
    for x, y in crabs.items():
        n = abs(x - i)
        cost = n if a_mode else int(n*(n+1)/2)
        moves.append(cost*y)
    return sum(moves)


print("A:", min([fuel_req_to_move(x, crabs, True) for x in range(max(crabs.keys()))]))
print("B:", min([fuel_req_to_move(x, crabs, False) for x in range(max(crabs.keys()))]))

# A: 339321
# B: 95476244

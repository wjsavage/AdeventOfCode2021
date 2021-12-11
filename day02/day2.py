with open("input") as file:
    lines = [str(line.rstrip()).split(" ") for line in file.readlines()]

commands = [(c, int(x)) for c, x in lines]

# A
# answer: 1692075
fwd, depth = 0, 0

for command, x in commands:
    if command == "forward":
        fwd += x
    elif command == "down":
        depth += x
    elif command == "up":
        depth -= x

print("A:", fwd * depth)

# B
# answer: 1749524700
fwd, depth, aim, = 0, 0, 0

for command, x in commands:
    if command == "forward":
        fwd += x
        depth += aim * x
    elif command == "down":
        aim += x
    elif command == "up":
        aim -= x

print("B:", fwd * depth)
with open("input") as file:
    lines = [str(line.rstrip()) for line in file.readlines()]

# A
fwd = 0
depth = 0

for line in lines:
    command, x = line.split(" ")
    command = str(command)
    x = int(x)
    if command == "forward":
        fwd += x
    elif command == "down":
        depth += x
    elif command == "up":
        depth -= x
    else:
        print(line)

print(fwd * depth)

#B
fwd = 0
aim = 0
depth = 0

for line in lines:
    command, x = line.split(" ")
    command = str(command)
    x = int(x)
    if command == "forward":
        fwd += x
        depth += aim * x
    elif command == "down":
        aim += x
    elif command == "up":
        aim -= x
    else:
        print(line)

print(fwd * depth)
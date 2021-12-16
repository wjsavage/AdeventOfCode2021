from functools import reduce

with open("input") as file:
    data = [line.rstrip() for line in file.readlines()][0]

print("Input:", data)
packet = bin(int(data, 16))[2:]
while len(packet) < len(data) * 4:
    packet = '0' + packet
print("Input in binary:", packet)

versions = []


def decode_packet(i):
    v = int(packet[i: i + 3], 2)
    i += 3
    versions.append(v)
    t = int(packet[i: i + 3], 2)
    i += 3
    if t == 4:
        return decode_literal(i)
    else:
        return decode_operator(i, int(t))


def decode_literal(i):
    literal = ""
    while packet[i] == '1':
        literal += packet[i + 1: i + 5]
        i += 5

    literal += packet[i + 1:i + 5]
    i += 5
    return i, int(literal, 2)


def decode_operator(i, t):
    mode = packet[i]
    i += 1
    values = []
    if mode == '0':
        sub_packets_tot_len = int(packet[i:i + 15], 2)
        i += 15
        n = i
        while i < n + sub_packets_tot_len:
            i, a = decode_packet(i)
            values.append(a)

    else:
        num_of_sub_packets = int(packet[i:i + 11], 2)
        i += 11
        for _ in range(num_of_sub_packets):
            i, x = decode_packet(i)
            values.append(x)

    return i, handle_type(t, values)


def handle_type(operator, values):
    if operator == 0:
        return sum(values)
    elif operator == 1:
        return reduce((lambda x, y: x * y), values)
    elif operator == 2:
        return min(values)
    elif operator == 3:
        return max(values)
    elif operator == 5:
        return 1 if values[0] > values[1] else 0
    elif operator == 6:
        return 1 if values[0] < values[1] else 0
    elif operator == 7:
        return 1 if values[0] == values[1] else 0
    else:
        raise Exception("Incorrect type:", operator)


b = decode_packet(0)[1]

print("A:", sum(versions))
print("B:", b)

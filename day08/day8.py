from collections import Counter

with open("input") as file:
    lines = [str(line.rstrip()).split('|') for line in file.readlines()]

count = 0
for signals, output in lines:
    for out in output.split(" "):
        if len(out) in [2, 3, 4, 7]:
            count += 1
print("A:", count)
# A: 237

truth_map = {'abcefg': 0,
           'cf': 1,
           'acdeg': 2,
           'acdfg': 3,
           'bcdf': 4,
           'abdfg': 5,
           'abdefg': 6,
           'acf': 7,
           'abcdefg': 8,
           'abcdfg': 9}

vals = []
for signals, output in lines:
    sol_map = {} # left hand side is the truth
    dig_map = {}
    digits = signals.rstrip().split(" ")
    for digit in digits:
        if len(digit) == 2:
            dig_map[1] = digit
        elif len(digit) == 3:
            dig_map[7] = digit
        elif len(digit) == 4:
            dig_map[4] = digit
    # the a signal is the only signal that is in a 7 but not in a 1
    sol_map['a'] = list(set(dig_map[7]) - set(dig_map[1]))[0]

    # we can count how many times in the total each signal should occur, given we know a this count is unique except
    # for g & d so we can now generate a nearly complete mapping
    sig_counts = Counter(''.join(digits))
    sig_counts.pop(sol_map.get('a'))
    for sig, freq in sig_counts.items():
        if freq == 4:
            sol_map['e'] = sig
        elif freq == 6:
            sol_map['b'] = sig
        elif freq == 8:
            sol_map['c'] = sig
        elif freq == 9:
            sol_map['f'] = sig
    # we still can't do g or d yet as they both appear 8 times in the 10 digits
    # however a d is in a 4 and a g is not
    sol_map['d'] = str([x for x in dig_map[4] if x not in sol_map.values()][0])
    sol_map['g'] = str([x for x in 'abcdefg' if x not in sol_map.values()][0])

    out_digits = ""
    outs = output.strip().split(" ")

    ran_dig_map = {}
    for key, value in truth_map.items():
        k = "".join(sorted([sol_map[x] for x in key]))
        ran_dig_map[k] = value

    for out in outs:
        for key, value in ran_dig_map.items():
            if set(out) == set(key):
                out_digits += str(value)
    vals.append(int(out_digits))

print("B:", sum(vals))
# B: 1009098


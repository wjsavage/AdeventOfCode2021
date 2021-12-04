from itertools import chain

with open("input") as file:
    lines = [str(line.rstrip()) for line in file.readlines()]

calls = lines[0].split(',')
boards = []

for i in range(2, len(lines), 6):
    board = [lines[i + j].split() for j in range(5)]
    boards.append(board)

winning_board = None
winning_call = None


def check_winning_list(entry):
    return len(set(entry)) == 1


for call in calls:
    print(call)

    # mark the number in each grid
    for i, board in enumerate(boards):
        if winning_call:
            print("finf")
            break
        for row in board:
            for j, num in enumerate(row):
                if num == call:
                    row[j] = 'x'
                    if check_winning_list(row):
                        winning_board = i
                        winning_call = call
                if winning_call:
                    break
            if winning_call:
                break

        # now need to check for each col
        for k in range(5):
            if check_winning_list(set([row[k] for row in board])):
                winning_board = i
                winning_call = call

        if winning_call:
            break
    if winning_call:
        break

print(winning_call)
rem = list(chain.from_iterable(boards[winning_board]))
rems = sum([int(x) for x in rem if x != 'x'])
print(rems*int(winning_call))
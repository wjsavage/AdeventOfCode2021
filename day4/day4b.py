from itertools import chain

# B
# Answer: 1284

with open("input") as file:
    lines = [str(line.rstrip()) for line in file.readlines()]

calls = lines[0].split(',')
boards = []

for i in range(2, len(lines), 6):
    board = [lines[i + j].split() for j in range(5)]
    boards.append(board)


def check_winning_list(entry):
    return len(set(entry)) == 1


remaining_boards = [i for i in range(len(boards))]
losing_board = None
last_call = None

for h, call in enumerate(calls):
    this_rounds_winners = []

    for i in remaining_boards:
        board = boards[i]
        for row in board:
            for j, num in enumerate(row):
                if num == call:
                    row[j] = 'x'
                    if check_winning_list(row):
                        this_rounds_winners.append(i)

        for k in range(5):
            if check_winning_list([row[k] for row in board]):
                this_rounds_winners.append(i)

    remaining_boards = [x for x in remaining_boards if x not in this_rounds_winners]
    if len(remaining_boards) == 0:
        last_call = call
        losing_board = this_rounds_winners[0]
        break

print("Last call:", last_call)
print("Last board to win:", boards[losing_board])

rem = list(chain.from_iterable(boards[losing_board]))
rems = sum([int(x) for x in rem if x != 'x'])

print(rems * int(last_call))

with open("input") as file:
    lines = [str(line.rstrip()) for line in file.readlines()]

boards = [[lines[i + j].split() for j in range(5)] for i in range(2, len(lines), 6)]
completed_boards = []

def sum_of_board(board):
    return sum([int(num) for row in board for num in row if num != 'x'])


for call in lines[0].split(','):
    for i, board in enumerate(boards):
        if i not in [idx for idx, c in completed_boards]:
            for row in board:
                for j, num in enumerate(row):
                    if num == call:
                        row[j] = 'x'
            if any([True for row in board if len(set(row)) == 1]) \
                    or any([True for col in zip(*board) if len(set(col)) == 1]):
                completed_boards.append((i, int(call)))

print(f"A: {sum_of_board(boards[completed_boards[0][0]]) * completed_boards[0][1]}")
print(f"B: {sum_of_board(boards[completed_boards[-1][0]]) * completed_boards[-1][1]}")

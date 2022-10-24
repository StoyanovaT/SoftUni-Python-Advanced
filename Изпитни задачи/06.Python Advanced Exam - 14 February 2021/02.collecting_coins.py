import sys
from io import StringIO
test_input1 = '''5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
left
right
right
up
up
right
'''
test_input2 = '''8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
down
up
left
'''

sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

import math


def get_next_position(row, col, direction):
    if direction == 'up':
        row = row - 1
        col = col
    elif direction == 'down':
        row = row + 1
        col = col
    elif direction == 'left':
        row = row
        col = col - 1
    elif direction == 'right':
        row = row
        col = col + 1

    return row, col


def is_outside(r, c, s):
    return r < 0 or c < 0 or r >= s or c >= s


size = int(input())
matrix = []
pl_row = 0
pl_col = 0
path = []
coins = 0
for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "P":
            pl_row = row
            pl_col = col
    matrix.append(row_elements)
path.append([pl_row, pl_col])
while True:
    command = input()

    if command not in ["up", "down", "left", "right"]:
        continue

    next_row, next_col = get_next_position(pl_row, pl_col, command)

    if is_outside(next_row, next_col, size):
        if command == 'left':
            next_row, next_col = next_row, size - 1
        elif command == 'right':
            next_row, next_col = next_row, 0
        elif command == 'up':
            next_row, next_col = size - 1, next_col
        elif command == 'down':
            next_row, next_col = 0, next_col

    path.append([next_row, next_col])
    pl_row, pl_col = next_row, next_col

    if matrix[pl_row][pl_col] == 'X':
        coins /= 2
        break

    if matrix[pl_row][pl_col] != 'P':
        coins += int(matrix[pl_row][pl_col])
        matrix[pl_row][pl_col] = 'P'
        if coins >= 100:
            break


if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {math.floor(coins)} coins.")

print("Your path:")
for position in path:
    print(position)

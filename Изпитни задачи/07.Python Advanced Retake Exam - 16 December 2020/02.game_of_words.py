import sys
from io import StringIO

test_input1 = '''Hello
4
P---
Mark
-l-y
--e-
4
down
right
right
right
'''
test_input2 = '''Initial
5
-----
t-r--
--Pa-
--S--
z--t-
4
up
left
left
left
'''

# sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)


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
    return r < 0 or c < 0 or row >= s or c >= s


string = input()
size = int(input())
pl_row = 0
pl_col = 0
matrix = []

for row in range(size):
    row_elements = [x for x in input()]
    for col in range(size):
        if row_elements[col] == 'P':
            pl_row = row
            pl_col= col
    matrix.append(row_elements)

num_of_commands = int(input())

for _ in range(num_of_commands):
    matrix[pl_row][pl_col] = '-'

    command = input()
    next_row, next_col = get_next_position(pl_row, pl_col, command)

    if is_outside(next_row, next_col, size):
        if len(string) > 0:
            string = string[:-1]
        matrix[pl_row][pl_col] = 'P'
        continue

    pl_row, pl_col = next_row, next_col

    if matrix[pl_row][pl_col] == '-':
        matrix[pl_row][pl_col] = 'P'
        continue

    string = string + matrix[pl_row][pl_col]

    matrix[pl_row][pl_col] = 'P'

print(string)
for row in matrix:
    new_row = ''.join(row)
    print(new_row)

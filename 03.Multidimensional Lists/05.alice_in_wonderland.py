import sys
from io import StringIO
test_input1 = '''5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
'''
test_input2 = '''7
. A . 1 1 . .
9 . . . 6 . 5
. 6 . R . . .
. 3 . . 1 . .
. . . 2 . . 2
. 3 . . 1 . .
. 8 3 . . . 2
left
down
down
right
'''
test_input3 = '''5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
left
left
left
'''
# sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

size = int(input())
matrix = []
alice_row = 0
alice_col = 0
for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == 'A':
            alice_row = row
            alice_col = col

tea_bags = 0

directions = {
    'left': lambda r, c: (r, c - 1),
    'right': lambda r, c: (r, c + 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c)
}

while tea_bags < 10:
    matrix[alice_row][alice_col] = '*'

    direction = input()
    next_row, next_col = directions[direction](alice_row, alice_col)

    if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
        break

    alice_row, alice_col = next_row, next_col

    if matrix[alice_row][alice_col] == '.' or matrix[alice_row][alice_col] == '*':
        continue

    if matrix[alice_row][alice_col] == 'R':
        break

    tea_bags += int(matrix[alice_row][alice_col])

matrix[alice_row][alice_col] = '*'

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(*row)


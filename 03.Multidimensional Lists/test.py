import sys
from io import StringIO
test_input1 = '''2 3
1 2 3
4 5 6
swap 0 0 1 1
swap 10 9 8 7
swap 0 1 1 0
END
'''
# test_input2 = '''1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
# '''
# test_input3 = '''
# '''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def is_outside(row, col, r_s, c_s):
    return row < 0 or col < 0 or row >= r_s or col >= c_s


rows, cols = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]


while True:
    line = input()
    if line == 'END':
        break

    line_parts = line.split()
    if line_parts[0] != 'swap' or len(line_parts) != 5:
        print("Invalid input!")
        continue
    row1, col1, row2, col2 = [int(x) for x in line_parts[1:]]

    if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
        print("Invalid input!")
        continue

    matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]

    for row in matrix:
        print(*row, sep=' ')

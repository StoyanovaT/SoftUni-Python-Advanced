import sys
from io import StringIO
test_input1 = '''4
8 3 2 5
6 4 7 9
9 9 3 6
6 8 1 2
1,2 2,1 2,0
'''
test_input2 = '''3
7 8 4
3 1 5
6 4 9
0,2 1,0 2,2
'''
# test_input3 = '''
# '''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def get_children(matrix, row, col):
    possible_children_cords = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1],
    ]

    result = []
    for child_row, child_col in possible_children_cords:
        if 0 <= child_row < len(matrix) and 0 <= child_col < len(matrix) and matrix[child_row][child_col] > 0:
            result.append([child_row, child_col])
    return result


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

bombs = input().split()

for bomb in bombs:
    row, col = [int(x) for x in bomb.split(',')]
    power = matrix[row][col]

    if power <= 0:
        continue

    matrix[row][col] = 0

    children = get_children(matrix, row, col)
    for child_row, child_col in children:
        matrix[child_row][child_col] -= power

alive_cells_count = 0
alive_cells_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells_count += 1
            alive_cells_sum += el

print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")
for row in matrix:
    print(*row, sep=' ')

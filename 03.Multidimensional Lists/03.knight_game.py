import sys
from io import StringIO
test_input1 = '''5 
0K0K0
K000K
00K00
K000K
0K0K0
'''
test_input2 = '''2
KK
KK
'''
test_input3 = '''8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK
'''
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)


def find_count(board, row, col):
    moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1]
    ]

    result = 0
    for r, c in moves:
        if 0 <= r < len(board) and 0 <= c < len(board) and board[r][c] == 'K':
            result += 1
    return result


size = int(input())
board = [[x for x in input()] for _ in range(size)]
removed_knights_counter = 0

while True:
    best_count = 0
    knight_row = 0
    knight_col = 0
    for row in range(size):
        for col in range(size):
            if board[row][col] == '0':
                continue
            count = find_count(board, row, col)
            if count > best_count:
                best_count = count
                knight_row = row
                knight_col = col

    if best_count == 0:
        break

    board[knight_row][knight_col] = '0'
    removed_knights_counter += 1

print(removed_knights_counter)
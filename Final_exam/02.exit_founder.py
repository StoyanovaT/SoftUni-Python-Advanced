import sys
from io import StringIO

test_input1 = '''Tom, Jerry
. . T . . .
. . . . . .
. . W . . .
. . W . . E
. . . . . .
. T . W . .
(3, 2)
(1, 3)
(5, 1)
(5, 1)
'''
test_input2 = '''Jerry, Tom
. T . . . W
. . . . T .
. W . . . T
. T . E . .
. . . . . T
. . T . . .
(1, 1)
(3, 0)
(3, 3)
'''
test_input3 = '''Jerry, Tom
. . . W . .
. . T T . .
. . . . . .
. T . W . .
W . . . E .
. . . W . .
(0, 3)
(3, 3)
(1, 3)
(2, 2)
(3, 5)
(4, 0)
(5, 3)
(3, 1)
(4, 4)
(4, 4)
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)

curr_player, next_player = input().split(', ')

size = 6

matrix = [[x for x in input().split()] for _ in range(size)]

curr_pl_skip = 0
next_pl_skip = 0

while True:
    coords = input().strip('()')
    row, col = [int(x) for x in coords.split(', ')]

    if curr_pl_skip > 0 or matrix[row][col] == '.':
        if curr_pl_skip > 0:
            curr_pl_skip -= 1
        curr_player, next_player = next_player, curr_player
        curr_pl_skip, next_pl_skip = next_pl_skip, curr_pl_skip
        continue

    if matrix[row][col] == 'E':
        print(f"{curr_player} found the Exit and wins the game!" )
        break

    if matrix[row][col] == 'T':
        print(f"{curr_player} is out of the game! The winner is {next_player}.")
        break

    if matrix[row][col] == 'W':
        print(f"{curr_player} hits a wall and needs to rest.")
        curr_pl_skip += 1

    curr_player, next_player = next_player, curr_player
    curr_pl_skip, next_pl_skip = next_pl_skip, curr_pl_skip

print(matrix[-0][8])
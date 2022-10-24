import sys
from io import StringIO
test_input1 = '''3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
'''
test_input2 = '''4
1 2 3 4
5 6 7 8
8 7 6 5
4 3 2 1
Add 4 4 100
Add 3 3 100
Subtract -1 -1 42
Subtract 0 0 42
END
'''
# test_input3 = '''1| 4 5 6 7  |  8 9
# '''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
command = input().split()

while True:
    if "END" in command:
        break

    action = command[0]
    row, col, value = [int(x) for x in command[1:]]

    if row < 0 or row >= n or col < 0 or col >= n:
        print("Invalid coordinates")
        command = input().split()
        continue

    if action == "Add":
        matrix[row][col] += value
    else:
        matrix[row][col] -= value

    command = input().split()

for row in matrix:
    print(*row, sep=' ')
import sys
from io import StringIO
test_input1 = '''4 5
1 5 5 2 4
2 1 4 14 3
3 7 11 2 8
4 8 12 16 4
'''
test_input2 = '''5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5

'''
# test_input3 = '''5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P
# '''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def find_3x3_sum(matrix):
    max_sum = float('-inf')
    cur_subset = []
    for i in range(n-2):
        for j in range(m-2):
            cur_sum = matrix[i][j] + matrix[i][j+1] + matrix[i][j+2] + \
                      matrix[i+1][j] + matrix[i+1][j+1] + matrix[i+1][j+2] + \
                      matrix[i+2][j] + matrix[i+2][j+1] + matrix[i+2][j+2]
            if cur_sum > max_sum:
                max_sum = cur_sum
                cur_subset = [matrix[i][j], matrix[i][j+1], matrix[i][j+2],
                              matrix[i+1][j], matrix[i+1][j+1], matrix[i+1][j+2],
                              matrix[i+2][j], matrix[i+2][j+1], matrix[i+2][j+2]]
    return cur_subset, max_sum


n, m = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(n)]
subset, max_sum = find_3x3_sum(matrix)

print(f"Sum = {max_sum}")
print(f"{subset[0]} {subset[1]} {subset[2]}")
print(f"{subset[3]} {subset[4]} {subset[5]}")
print(f"{subset[6]} {subset[7]} {subset[8]}")
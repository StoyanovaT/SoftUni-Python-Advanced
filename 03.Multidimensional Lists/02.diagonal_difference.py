# import sys
# from io import StringIO
# test_input1 = '''3
# 11 2 4
# 4 5 6
# 10 8 -12
# '''
# test_input2 = '''4
# -7 14 9 -20
# 3 4 9 21
# -14 6 8 44
# 30 9 7 -14
# '''
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def find_sum_primary(matrix):
    return sum([matrix[i][i] for i in range(len(matrix))])


def find_sum_secondary(matrix):
    n = len(matrix)
    return sum([matrix[i][n - i - 1] for i in range(n)])


def abs_difference(sum_primary, sum_secondary):
    return abs(sum_primary - sum_secondary)


n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
sum_primary = find_sum_primary(matrix)
sum_secondary = find_sum_secondary(matrix)

print(abs_difference(sum_primary, sum_secondary))

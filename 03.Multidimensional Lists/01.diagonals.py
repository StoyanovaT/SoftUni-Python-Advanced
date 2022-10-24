import sys
from io import StringIO
test_input1 = '''3
1, 2, 3
4, 5, 6
7, 8, 9
'''
test_input2 = '''3, 3
1 2 3
4 5 6
7 8 9
'''
sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)


def primary(matrix):
    on_primary = [matrix[i][i] for i in range(len(matrix))]
    sum_primary = sum(on_primary)
    return on_primary, sum_primary


def secondary(matrix):
    n = len(matrix)
    secondary = [matrix[i][n - i - 1] for i in range(n)]
    sum_secondary = sum(secondary)
    return secondary, sum_secondary


n = int(input())
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]

primary_diagonal, sum_primary = primary(matrix)
secondary_diagonal, sum_secondary = secondary(matrix)

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum_primary}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum_secondary}")
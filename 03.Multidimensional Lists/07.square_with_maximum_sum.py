import sys
from io import StringIO
test_input1 = '''3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
'''
test_input2 = '''2, 4
10, 11, 12, 13
14, 15, 16, 17
'''
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)


def find_max_sum_el(matrix):
    max_sum = 0
    current_subset = []
    for i in range(n - 1):
        for j in range(m - 1):
            current_sum = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
            if max_sum < current_sum:
                max_sum = current_sum
                current_subset = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
    return current_subset, max_sum


n, m = (int(x) for x in input().split(', '))
matrix = [[int(x) for x in input().split(', ')] for _ in range(n)]
sub_matrix, sum_sub_matrix = find_max_sum_el(matrix)

print(f"{sub_matrix[0]} {sub_matrix[1]}")
print(f"{sub_matrix[2]} {sub_matrix[3]}")
print(sum_sub_matrix)

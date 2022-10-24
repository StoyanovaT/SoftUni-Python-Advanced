import sys
from io import StringIO
test_input1 = '''3 4
A B B D
E B B B
I J B B
'''
test_input2 = '''2 2
a b
c d
'''
test_input3 = '''5 4
A A B D
A A B B
I J B B
C C C G
C C K P
'''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def find_2x2(matrix):
    matches = 0
    for i in range(n-1):
        for j in range(m-1):
            if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
                matches += 1
    return matches


n, m = (int(x) for x in input().split())
matrix = [[x for x in input().split()] for _ in range(n)]

result = find_2x2(matrix)
print(result)

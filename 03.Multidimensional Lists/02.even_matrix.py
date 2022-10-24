import sys
from io import StringIO
test_input1 = '''2
1, 2, 3
4, 5, 6
'''
test_input2 = '''4
10, 33, 24, 5, 1
67, 34, 11, 110, 3
4, 12, 33, 63, 21
557, 45, 23, 55, 67
'''
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

# n = int(input())
# result = []
# for _ in range(n):
#     row = [int(x) for x in input().split(', ')]
#     result.append([x for x in row if x % 2 == 0])
# print(result)

# ili:

matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
print([[x for x in row if x % 2 == 0] for row in matrix])

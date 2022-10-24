import sys
from io import StringIO
test_input1 = '''5 6
SoftUni
'''
test_input2 = '''1 4
Python
'''
# test_input3 = '''
# '''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

# rows, cols = [int(x) for x in input().split()]
# word = input()
#
# idx = 0
#
# for row in range(rows):
#     elements = [None] * cols
#     if row % 2 == 0:
#         for col in range(cols):
#             elements[col] = word[idx % len(word)]
#             idx += 1
#     else:
#         for col in range(cols - 1, -1, -1):
#             elements[col] = word[idx % len(word)]
#             idx += 1
#     print(''.join(elements))

# ili:
rows, cols = [int(x) for x in input().split()]
word = input()

idx = 0

for row in range(rows):
    elements = [None] * cols
    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols - 1, -1, -1)
    for col in range(start, end, step):
        elements[col] = word[idx % len(word)]
        idx += 1
    print(''.join(elements))

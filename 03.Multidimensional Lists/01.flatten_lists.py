import sys
from io import StringIO
test_input1 = '''1 2 3 |4 5 6 |  7  88
'''
test_input2 = '''7 | 4  5|1 0| 2 5 |3
'''
test_input3 = '''1| 4 5 6 7  |  8 9
'''
sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)

matrix = []
sublists = input().split('|')
for index in range(len(sublists) - 1, -1, -1):
    row = sublists[index].split()
    matrix.append(row)

flattened = [num for sublist in matrix for num in sublist]

print(' '.join(flattened))

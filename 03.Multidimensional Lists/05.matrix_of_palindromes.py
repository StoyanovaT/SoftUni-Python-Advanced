from collections import deque

matrix = []
rows, cols = [int(x) for x in input().split()]
letters = deque(a for a in range(97, 123))

for row in range(rows):
    letter_num = letters.popleft()
    row_elements = []
    b = letter_num
    for col in range(cols):
        row_el = ''
        row_el += chr(letter_num) + chr(b) + chr(letter_num)
        row_elements.append(row_el)
        b += 1
    matrix.append(row_elements)

for row in matrix:
    print(*row)


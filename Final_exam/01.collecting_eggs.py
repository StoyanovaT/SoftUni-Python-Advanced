import sys
from io import StringIO

test_input1 = '''20, 13, -7, 7
10, 5, 20, 15, 7, 9
'''
test_input2 = '''2, 4, 7, 8, 0
5, 6, 2
'''
test_input3 = '''12, 23
28, 40
'''
# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)

from collections import deque

boxes_filled = 0

eggs_deque = deque(int(x) for x in input().split(', '))
pieces_paper = [int(x) for x in input().split(', ')]

while eggs_deque and pieces_paper:
    while eggs_deque[0] <= 0 or eggs_deque[0] == 13:
        removed_egg = eggs_deque.popleft()
        if removed_egg == 13:
            pieces_paper[0], pieces_paper[-1] = pieces_paper[-1], pieces_paper[0]
        if not eggs_deque:
            break
    if not eggs_deque:
        break

    egg = eggs_deque.popleft()
    paper = pieces_paper.pop()
    sum_e_p = egg + paper

    if sum_e_p <= 50:
        boxes_filled += 1


if boxes_filled >= 1:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_deque:
    print(f"Eggs left: {', '.join(str(x) for x in eggs_deque)}")
if pieces_paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in pieces_paper)}")

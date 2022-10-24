import sys
from io import StringIO
test_input1 = '''4 5 7 3 6 9 12
12 9 6 1
'''
test_input2 = '''3 0 3 6 9 0 12
12 9 6 1 2 3 15 13 4
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

matches = 0
no_more = False

while males and females:
    while males[-1] <= 0:
        males.pop()
        if not males:
            no_more = True
            break
    if no_more:
        break

    while males[-1] % 25 == 0:
        males.pop()
        if not males:
            no_more = True
            break
    if no_more:
        break

    while females[0] <= 0:
        females.popleft()
        if not females:
            no_more = True
            break
    if no_more:
        break

    while females[0] % 25 == 0:
        females.popleft()
        if not females:
            no_more = True
            break
    if no_more:
        break

    female = females.popleft()
    male = males.pop()

    if female != male:
        male -= 2
        males.append(male)
    else:
        matches += 1

print(f"Matches: {matches}")
if males:
    rev_males = reversed(males)
    print(f"Males left: {', '.join(str(x) for x in rev_males)}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print("Females left: none")

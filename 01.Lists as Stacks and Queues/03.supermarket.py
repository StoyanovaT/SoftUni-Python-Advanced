from collections import deque

line_deque = deque()
name = input()

while not name == "End":
    if name == "Paid":
        while line_deque:
            print(line_deque.popleft())
    else:
        line_deque.append(name)

    name = input()
print(f"{len(line_deque)} people remaining.")

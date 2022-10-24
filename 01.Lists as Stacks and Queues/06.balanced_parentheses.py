sequence = input()
opening_stack = []
condition = True

if sequence[0] in ")}]":
    condition = False

if condition:
    for symb in sequence:
        if symb in "({[":
            opening_stack.append(symb)

        elif not opening_stack:
            condition = False
            break

        else:
            last_opened = opening_stack.pop()

            if f"{last_opened}{symb}" not in "()[]{}":
                condition = False
                break

if condition and not opening_stack:
    print("YES")
else:
    print("NO")

text = input()

par_stack = []

for index in range(len(text)):
    if text[index] == "(":
        par_stack.append(index)
    elif text[index] == ")":
        print(text[par_stack.pop():index+1])

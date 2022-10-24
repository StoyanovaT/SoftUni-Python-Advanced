def even_odd(*args):
    command = args[-1]
    remainder = 0 if command == 'even' else 1
    result = []
    for i in range(len(args) - 1):
        number = args[i]
        if number % 2 == remainder:
            result.append(number)

    return result




print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
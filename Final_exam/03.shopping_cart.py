def shopping_cart(*args):
    meals_dict = {'Soup': [], 'Pizza': [], 'Dessert': []}
    for arg in args:
        if arg == "Stop":
            break

        meal, product = arg

        if meal == 'Soup' and len(meals_dict[meal]) == 3 or product in meals_dict[meal]:
            continue
        if meal == 'Pizza' and len(meals_dict[meal]) == 4 or product in meals_dict[meal]:
            continue
        if meal == 'Dessert' and len(meals_dict[meal]) == 2 or product in meals_dict[meal]:
            continue

        meals_dict[meal].append(product)
    empty = False
    for key, value in meals_dict.items():
        if value == []:
            empty = True
        else:
            empty = False
            break
    if empty:
        return "No products in the cart!"
    else:
        for key, value in meals_dict.items():
            meals_dict[key] = sorted(value)
        sorted_meals = sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0]))
        result = []
        for key, value in sorted_meals:
            result.append(f'{key}:')
            for val in value:
                result.append(f' - {val}')

        return '\n'.join([str(x) for x in result])



print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))

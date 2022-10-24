def shopping_list(budget, **kwargs):
    bought_products = {}
    full_basket = False
    if budget < 100:
        return "You do not have enough budget."
    else:
        for key, value in kwargs.items():
            price_1 = float(value[0])
            quantity = int(value[1])
            tot_price = price_1 * quantity

            if tot_price > budget:
                continue
            else:
                budget -= tot_price
                bought_products[key] = tot_price
                if len(bought_products) == 5:
                    full_basket = True
                    break
        result = ''
        for key, value in bought_products.items():
            result += f"You bought {key} for {value:.02f} leva.\n"
        return result


# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))

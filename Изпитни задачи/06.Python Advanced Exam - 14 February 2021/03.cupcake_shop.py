from collections import deque


def stock_availability(boxes, action, *args):
    inventory = deque(boxes)
    if action == "delivery":
        for box in args:
            inventory.append(box)

    else:
        if not args:
            inventory.popleft()
        else:
            first, *_ = args
            if isinstance(first, int):
                for _ in range(first):
                    inventory.popleft()
            else:
                if len(args) == 1:
                    while first in inventory:
                        inventory.remove(first)
                else:
                    for flavour in args:
                        while flavour in inventory:
                            inventory.remove(flavour)

    result = [x for x in inventory]
    return result


# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

from collections import deque

food_quantity = int(input())
orders = deque([int(n) for n in input().split()])

print(max(orders))

for index in range(len(orders)):
    if food_quantity >= orders[0]:
        current_order = orders.popleft()
        food_quantity -= current_order

    else:
        break

if orders:
    print("Orders left:", end=' ')
    while orders:
        print(f"{orders.popleft()}", end=' ')
else:
    print("Orders complete")
    # ili:
    # print(f"Orders left: {' '.join([str(x) for x in orders])}")
from collections import deque

orders = deque(int(x) for x in input().split(', '))
employees = [int(x) for x in input().split(', ')]
tot_pizzas = 0
while employees:
    if not orders:
        break

    while orders[0] > 10 or orders[0] <= 0:
        orders.popleft()
        if not orders:
            break

    if not orders:
        break

    pizzas = orders.popleft()
    empl_capacity = employees.pop()

    if pizzas <= empl_capacity:
        tot_pizzas += pizzas

    else:
        pizzas -= empl_capacity
        tot_pizzas += empl_capacity
        if not employees:
            orders.appendleft(pizzas)
            break
        empl_capacity = employees.pop()
        if pizzas <= empl_capacity:
            tot_pizzas += pizzas


if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {tot_pizzas}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in orders)}")

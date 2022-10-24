from collections import deque
ramen_bowls_stack = [int(x) for x in input().split(', ')]
customers_deque = deque(int(x) for x in input().split(', '))

while ramen_bowls_stack and customers_deque:
    curr_ramen = ramen_bowls_stack.pop()
    curr_customer = customers_deque.popleft()

    if curr_ramen == curr_customer:
        continue
    elif curr_ramen > curr_customer:
        curr_ramen -= curr_customer
        ramen_bowls_stack.append(curr_ramen)
    else:
        curr_customer -= curr_ramen
        customers_deque.appendleft(curr_customer)

if not customers_deque:
    print("Great job! You served all the customers.")
    if ramen_bowls_stack:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen_bowls_stack)}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers_deque)}")


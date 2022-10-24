from collections import deque

price = int(input())
gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
shoots = 0

opened = False

while locks:
    current_bullets = bullets.pop()
    current_lock = locks[0]

    if current_bullets <= current_lock:
        print("Bang!")
        locks.popleft()

    elif current_bullets > current_lock:
        print("Ping!")

    shoots += 1
    intelligence_value -= price

    if not bullets:
        break

    if gun_barrel == shoots:
        print("Reloading!")
        shoots = 0

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")


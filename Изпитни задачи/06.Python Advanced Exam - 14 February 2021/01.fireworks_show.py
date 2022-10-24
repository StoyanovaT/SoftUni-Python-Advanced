from collections import deque

firework_effects = deque(int(x) for x in input().split(', '))
explosive_power = [int(x) for x in input().split(', ')]
success = False
fireworks_made = [0, 0, 0]

while firework_effects and explosive_power:
    while firework_effects[0] <= 0:
        firework_effects.popleft()
        if not firework_effects:
            break
    while explosive_power[-1] <= 0:
        explosive_power.pop()
        if not explosive_power:
            break

    if not firework_effects or not explosive_power:
        break

    effect = firework_effects.popleft()
    power = explosive_power.pop()
    mix = effect + power

    if mix % 5 == 0 and mix % 3 == 0:
        fireworks_made[2] += 1

    elif mix % 5 == 0 and mix % 3 != 0:
        fireworks_made[1] += 1

    elif mix % 5 != 0 and mix % 3 == 0:
        fireworks_made[0] += 1

    else:
        effect -= 1
        firework_effects.append(effect)
        explosive_power.append(power)
        continue

    for i in fireworks_made:
        if i >= 3:
            success = True
        else:
            success = False
            break

    if success:
        break

if success:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f" Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

print(f"Palm Fireworks: {fireworks_made[0]}")
print(f"Willow Fireworks: {fireworks_made[1]}")
print(f"Crossette Fireworks: {fireworks_made[2]}")

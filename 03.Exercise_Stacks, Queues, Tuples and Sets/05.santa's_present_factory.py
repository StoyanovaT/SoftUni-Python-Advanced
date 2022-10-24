from collections import deque

materials = [int(x) for x in input().split()]
magic_levels_deque= deque(int(x) for x in input().split())

present_magic_needed = {'Doll': 150, 'Wooden train': 250, 'Teddy bear': 300, 'Bicycle': 400}
toys_made = {}

while materials and magic_levels_deque:
    material = materials.pop()
    magic_level = magic_levels_deque.popleft()

    if material == 0 and magic_level == 0:
        continue

    elif material == 0:
        magic_levels_deque.appendleft(magic_level)
        continue
    elif magic_level == 0:
        materials.append(material)
        continue

    result = material * magic_level
    if result < 0:
        result = material + magic_level
        materials.append(result)
        continue
    else:
        if result not in present_magic_needed.values():
            material += 15
            materials.append(material)

        else:
            for toy, points in present_magic_needed.items():
                if points == result:
                    if toy in toys_made.keys():
                        toys_made[toy] += 1
                        break
                    else:
                        toys_made[toy] = 1
                        break

if ('Doll' in toys_made.keys() and 'Wooden train' in toys_made.keys()) or ('Teddy bear' in toys_made.keys() and 'Bicycle' in toys_made.keys()):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")
if magic_levels_deque:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels_deque])}")

for key, value in sorted(toys_made.items()):
    print(f"{key}: {value}")

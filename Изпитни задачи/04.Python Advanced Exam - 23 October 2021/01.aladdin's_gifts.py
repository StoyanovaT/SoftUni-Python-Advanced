import collections
from collections import deque

materials = [int(x) for x in input().split()]
magic_levels_deque = deque(int(x) for x in input().split())

gifts_magic_needed = {
    'Gemstone': [100, 199],
    'Porcelain Sculpture': [200, 299],
    'Gold': [300, 399],
    'Diamond Jewellery': [400, 499],
}

crafted_gifts = {}

while materials and magic_levels_deque:
    cur_materials = materials.pop()
    cur_magic = magic_levels_deque.popleft()

    tot_magic = cur_magic + cur_materials

    if tot_magic < 100:
        if tot_magic % 2 == 0:
            cur_materials *= 2
            cur_magic *= 3

        else:
            cur_materials *= 2
            cur_magic *= 2

        tot_magic = cur_materials + cur_magic

    if tot_magic > 499:
        tot_magic /= 2

    if 100 > tot_magic > 499:
        continue

    for key, value in gifts_magic_needed.items():
        if value[0] <= tot_magic <= value[1]:
            if key not in crafted_gifts.keys():
                crafted_gifts[key] = 0
            crafted_gifts[key] += 1
            break

if 'Gemstone' in crafted_gifts.keys() and 'Porcelain Sculpture' in crafted_gifts.keys() or\
        'Gold' in crafted_gifts.keys() and 'Diamond Jewellery' in crafted_gifts.keys():
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '. join(str(x) for x in materials)}")
if magic_levels_deque:
    print(f"Magic left: {', '. join(str(x) for x in magic_levels_deque)}")

sorted_crafted_dict = collections.OrderedDict(sorted(crafted_gifts.items()))

for key, value in sorted_crafted_dict.items():
    print(f"{key}: {value}")

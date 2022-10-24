clothes_in_box = [int(x) for x in input().split()]
rack_capacity = int(input())
racks_used = 0
rack_status = 0

while clothes_in_box:
    current_clothes = clothes_in_box.pop()

    if current_clothes <= (rack_capacity - rack_status):
        rack_status += current_clothes
        if rack_capacity == rack_status:
            racks_used += 1
            rack_status = 0
    else:
        racks_used += 1
        rack_status = 0
        rack_status += current_clothes
if rack_status > 0:
    racks_used += 1

print(racks_used)

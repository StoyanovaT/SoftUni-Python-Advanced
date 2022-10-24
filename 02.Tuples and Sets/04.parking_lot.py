n = int(input())
parking = set()

for _ in range(n):
    direction, car = input().split(", ")

    if direction == "IN":
        parking.add(car)
    else:
        parking.remove(car)

if parking:
    for c in parking:
        print(c, end='\n')
else:
    print("Parking Lot is Empty")




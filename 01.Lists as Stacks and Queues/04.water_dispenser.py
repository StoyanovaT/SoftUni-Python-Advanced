from collections import deque

water = int(input())
name = input()
people_line = deque()

while not name == "Start":
    people_line.append(name)

    name = input()

command = input()
while not command == "End":
    if command.isdigit():
        liters = int(command)
        current_name = people_line.popleft()
        if water >= liters:
            water -= liters
            print(f"{current_name} got water")
        else:
            print(f"{current_name} must wait")

    else:
        _, liters_to_refill = command.split()
        liters_to_refill = int(liters_to_refill)
        water += liters_to_refill

    command = input()

print(f"{water} liters left")
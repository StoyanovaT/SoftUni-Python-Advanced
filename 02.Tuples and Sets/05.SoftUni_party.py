n = int(input())
guests_list = set()

for _ in range(n):
    guests_list.add(input())

guest_came = input()
while guest_came != "END":
    guests_list.remove(guest_came)

    guest_came = input()

print(len(guests_list))
sorted_list = sorted(guests_list)

for g in sorted_list:
    print(g)


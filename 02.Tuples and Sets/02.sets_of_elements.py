n, m = [int(n) for n in input().split()]

a_set = set()
b_set = set()

for _ in range(n):
    a_set.add(int(input()))

for _ in range(m):
    b_set.add(int(input()))

intersections = a_set.intersection(b_set)

for i in intersections:
    print(i)

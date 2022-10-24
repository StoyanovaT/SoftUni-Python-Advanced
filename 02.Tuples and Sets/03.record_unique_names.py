n = int(input())
names = set()
for _ in range(n):
    name = input()

    names.add(name)

for i in names:
    print(i, end='\n')

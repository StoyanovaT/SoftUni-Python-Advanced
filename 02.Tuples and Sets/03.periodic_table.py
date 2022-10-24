n = int(input())
unique_el_set = set()
for _ in range(n):
    chemical_compounds = set(input().split(' '))
    unique_el_set = unique_el_set.union(chemical_compounds)

for i in unique_el_set:
    print(i)
# ili
# [print(i) for i in unique_el_set]

# ili
# print(*unique_el_set, sep='\n')
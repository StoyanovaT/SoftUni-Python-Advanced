n = int(input())
odd_set = set()
even_set = set()

for row in range(1, n+1):
    name = input()
    res_after_division = sum([ord(x) for x in name]) // row

    if res_after_division % 2 == 0:
        even_set.add(res_after_division)
    else:
        odd_set.add(res_after_division)

odd_set_sum = sum(odd_set)
even_set_sum = sum(even_set)

if odd_set_sum == even_set_sum:
    result = odd_set.union(even_set)
elif odd_set_sum > even_set_sum:
    result = odd_set.difference(even_set)
else:
    result = odd_set.symmetric_difference(even_set)

print(*result, sep=', ')

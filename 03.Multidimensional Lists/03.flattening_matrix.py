rows = int(input())

matrix = [map(int, input().split(', ')) for _ in range(rows)]
flattened = [num for row in matrix for num in row]
# ==
# flattened = []
# for row in matrix:
#     for num in row:
#         flattened.append(num)

print(flattened)


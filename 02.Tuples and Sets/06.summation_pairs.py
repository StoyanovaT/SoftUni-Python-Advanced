numbers = [int(n) for n in input().split()]
target_n = int(input())
un_nums = set()
iterations = 0

for a in range(len(numbers)):
    for b in range(a+1, len(numbers)):
        iterations += 1
        if numbers[a] + numbers[b] == target_n:
            pair = (numbers[a], numbers[b])
            un_nums.add(pair)
            print(f"{numbers[a]} + {numbers[b]} = {target_n}")
print(f"Iterations done: {iterations}")

for i in un_nums:
    print(i)

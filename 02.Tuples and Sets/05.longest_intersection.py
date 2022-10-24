n = int(input())
longest_intersection = []

for _ in range(n):
    ranges_info = input().split("-")
    first_start, first_end = [int(x) for x in ranges_info[0].split(",")]
    second_start,second_end = [int(x) for x in ranges_info[1].split(",")]

    first = set(range(first_start, first_end + 1))
    second = set(range(second_start, second_end + 1))

    intersection = first.intersection(second)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] with length {len(longest_intersection)}")

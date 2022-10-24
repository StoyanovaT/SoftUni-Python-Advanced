def neg_pos(*args):
    negatives = []
    positives = []
    for num in args:
        if num < 0:
            negatives.append(num)
        else:
            positives.append(num)

    print(sum(negatives))
    print(sum(positives))

    if abs(sum(negatives)) > sum(positives):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(x) for x in input().split()]

neg_pos(*numbers)

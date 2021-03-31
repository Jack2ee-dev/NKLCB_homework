def quicksort(x):
    if len(x) <= 1:
        return x

    mid = len(x) // 2
    pivot = x[mid]
    left = []
    right = []
    for i in range(0, len(x)):
        if i == mid:
            continue
        if x[i] < pivot:
            left.append(x[i])
        else:
            right.append(x[i])

    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([6, 2, 4, 15, 2, 5, 13, 6, 12]))

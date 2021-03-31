# 공간복잡도 O(1)
def quicksort_space_efficient(x):

    def recursive(low=0, high=-1):
        nonlocal x

        if high == -1:
            high = len(x)

        if low >= high:
            return x

        p_idx = high - 1
        pivot = x[p_idx]

        curr = 0
        while True:
            if curr >= p_idx:
                break

            if x[curr] > pivot:
                x.append(x.pop(curr))
                p_idx -= 1
                pivot = x[p_idx]
            else:
                curr += 1

        return recursive(low, p_idx) + recursive(p_idx + 1, high)

    recursive()
    return x


print(quicksort_space_efficient([6, 2, 4, 15, 2, 5, 13, 6, 12]))

def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    rocks = rocks + [distance]
    left, right = 0, distance

    while left <= right:
        curr = 0
        min_dist = float("inf")
        mid = (left + right) // 2
        remove_cnt = 0

        for rock in rocks:
            diff = rock - curr
            if diff < mid:
                remove_cnt += 1
            else:
                curr = rock
                min_dist = min(min_dist, diff)

        if remove_cnt > n:
            right = mid - 1
        else:
            left = mid + 1
            answer = min_dist
    return answer


if __name__ == "__main__":
    print(solution(25, [2, 14, 11, 21, 17], 2) == 4)

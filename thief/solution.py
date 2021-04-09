def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i - 1], money[i] + dp1[i - 2])

    dp2 = [0] * len(money)
    dp2[0] = money[0]
    dp2[1] = money[1]

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i - 1], money[i] + dp2[i - 2])

    return max(max(dp1), max(dp2))


def solution2(money):
    answer = 0

    n = len(money)
    dp = [0] * (n - 1)
    dp[0], dp[1] = money[0], max(money[:2])

    for i in range(2, n - 1):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])

    answer = dp[-1]

    dp = [0] * n
    dp[0], dp[1] = 0, money[1]

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + money[i], dp[i - 1])

    answer = max(answer, dp[-1])
    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 1]))
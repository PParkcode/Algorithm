def solution():
    n = int(input())
    case = []
    for i in range(n):
        case.append(int(input()))

    m = max(case)
    dp = [0] * (m + 1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, m + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    for item in case:
        print(dp[item])

solution()
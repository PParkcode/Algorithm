def solution():
    n = int(input())
    steps = [0]
    for i in range(n):
        steps.append(int(input()))

    dp = [[0]*2 for _ in range(n+1)]

    dp[0][0] = 0
    dp[0][1] = 0
    dp[1][0] = steps[1]
    dp[1][1] = steps[1]
    for i in range(2,n+1):
        dp[i][0] = max(dp[i-2][1],dp[i-2][0]) + steps[i]
        dp[i][1] = dp[i-1][0] + steps[i]

    answer = max(dp[n][0],dp[n][1])
    print(answer)

solution()
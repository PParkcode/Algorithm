def solution():
    n = int(input())

    dp = [987654321] * (n + 1)
    dp[1] = 0
    tracker = [0] * (n + 1)
    tracker[1] = 0
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        tracker[i] = i - 1

        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            tracker[i] = i // 3
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            tracker[i] = i // 2

    print(dp[n])
    trace = tracker[n]
    print(n, end=" ")
    while trace != 0:
        print(trace, end=" ")
        trace = tracker[trace]


solution()
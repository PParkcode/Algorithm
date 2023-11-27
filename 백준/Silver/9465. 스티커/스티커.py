def solution():
    t = int(input())
    for i in range(t):
        n = int(input())
        print(find(n))


def find(n):
    ls = []
    for i in range(2):
        ls.append(list(map(int,input().split())))

    dp = [[0]*n for _ in range(2)]
    dp[0][0] =ls[0][0]
    dp[1][0] = ls[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[1][i-1]  + ls[0][i], dp[0][i-1])
        dp[1][i] = max(dp[0][i-1] + ls[1][i], dp[1][i-1])
    
    return max(dp[0][n-1],dp[1][n-1])


solution()
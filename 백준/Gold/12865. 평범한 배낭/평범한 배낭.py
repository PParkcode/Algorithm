def solution():
    n, k = map(int, input().split())
    ls = []
    for _ in range(n):
        ls.append(list(map(int, input().split())))

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = ls.pop(0)
        cur_w = item[0]
        cur_v = item[1]
        
        for j in range(1, k + 1):
            # 현재 꺼낸 아이템의 무게가 현재 수용 가능한 무게보다 크다면,
            # 이전 아이템까지에서의 현재 무게까지의 최고 가치를 현재의 최고 가치로 할당하낟. 
            if cur_w > j:
                dp[i][j] = dp[i - 1][j]
            # 이전 아이템에서의 수용 가능한 무게까지의 최고 가치와,
            # 현재 꺼낸 아이템의 가치 + 이전 아이템까지에서 (현재 수용 무게 - 현재 아이템의 무게)에서의 가치를 더한 값 중 큰 것으로 설정
            else:
                dp[i][j] = max(dp[i - 1][j], cur_v + dp[i - 1][j - cur_w])

    print(dp[n][k])


solution()
def solution():
    n = int(input())
    timeTable = []
    dpTable = [0] * (n + 6)
    timeTable.append((0, 0))
    for i in range(n):
        t, p = map(int, input().split())
        timeTable.append((t, p))

    # 날짜를 거꾸로 확인한다.
    # 마지막 날부터 해당 날 이후로 구할 수 있는 최대 수익을 dpTable에 갱신한다.
    for i in range(n, 0, -1):
        t = timeTable[i][0]
        p = timeTable[i][1]

        # 진행 불가능한 경우 
        if i + t > n + 1:
            # dpTable[i] = 0 --> 여기를 0으로 해주면 안됨
            dpTable[i] = dpTable[i+1]
            continue

        # i번째 날에는 해당 날의 수익 + 소요 일 이후의 최대 수익값과 i+1번쨰 날의 수익을 비교하여
        # 최대값을 i번째 날의 수익으로 갱신한다.
        dpTable[i] = max(p + dpTable[i + t], dpTable[i + 1])

    print(dpTable[1])


solution()
def solution():
    n = int(input())
    ls = list(map(int, input().split()))
    ls.append(0)
    table = [0] * (n + 1)
    maxValue = 0
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            if ls[j] > ls[i]:
                maxValue = max(maxValue, table[j])

        table[i] = maxValue + 1
        maxValue = 0

    print(max(table))


solution()
def solution():
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    table = [[0] * (i + 1) for i in range(n)]
    table[0][0] = graph[0][0]

    for i in range(0, n - 1):
        for j in range(len(table[i])):
            table[i + 1][j] = max(table[i + 1][j], graph[i + 1][j] + table[i][j])
            table[i + 1][j + 1] = max(table[i + 1][j + 1], graph[i + 1][j + 1] + table[i][j])

    print(max(table[n - 1]))


solution()
import sys
from collections import deque

input = sys.stdin.readline

INF = 1000001


def solution():
    n = int(input())
    m = int(input())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    trace = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = min(graph[a][b], c)
        trace[a][b] = b

    for i in range(1, n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    continue
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    trace[i][j] = trace[i][k]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == INF:
                graph[i][j] = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(graph[i][j], end=" ")
        print()

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j] == 0:
                print(0)
                continue
            getRoute(trace, i, j)


def getRoute(trace, a, b):
    count = 1
    route = [a]
    destination = b
    q = deque()
    q.append(trace[a][b])

    while q:
        count += 1
        node = q.popleft()
        route.append(node)
        if destination == node:
            print(count, end=" ")
            for item in route:
                print(item, end=" ")
            print()
            return
        else:
            q.append(trace[node][destination])


solution()
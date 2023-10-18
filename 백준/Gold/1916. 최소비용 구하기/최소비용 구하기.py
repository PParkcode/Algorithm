import sys
import heapq

input = sys.stdin.readline

INF = 987654321


def solution():
    n = int(input())
    m = int(input())

    graph = [[] for _ in range(n + 1)]
    table = [INF] * (n + 1)

    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    start, goal = map(int, input().split())
    dijkstra(graph, table, start, goal)


def dijkstra(graph, table, start, goal):
    q = []
    table[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        weight, now = heapq.heappop(q)

        # 꺼낸 값이 거리 테이블의 값보다 크면 방문한거임.
        if table[now] < weight:
            continue

        for item in graph[now]:
            cost = weight + item[1]

            # 거쳐 가는 값이 더 작으면 갱신
            if cost < table[item[0]]:
                table[item[0]] = cost
                heapq.heappush(q, (cost, item[0]))

    print(table[goal])


solution()
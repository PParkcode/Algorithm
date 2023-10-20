import sys
import heapq
from collections import deque

input = sys.stdin.readline

INF = 987654321


def solution():
    n, k = map(int, input().split())
    graph = [[] for _ in range(200000)]
    distance = [INF] * 400001
    for i in range(100000):
        graph[i].append((i + 1, 1))
        graph[i].append((i - 1, 1))
        graph[i].append((2 * i, 0))
    if n > k:
        print(n - k)
        return

    dijkstra(graph, distance, n, k)

    print(distance[k])


# 다익스트라를 사용해 최단 거리를 찾는다.
def dijkstra(graph, distance, n, k):
    q = []

    heapq.heappush(q, (0, n))
    distance[n] = 0

    while q:

        weight, num = heapq.heappop(q)

        if weight > distance[num]:
            continue

        for item in graph[num]:
            cost = weight + item[1]

            if cost < distance[item[0]]:
                distance[item[0]] = cost
                heapq.heappush(q, (cost, item[0]))


solution()

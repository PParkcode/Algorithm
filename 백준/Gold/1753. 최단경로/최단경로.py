import sys
import heapq

input = sys.stdin.readline

INF = 987654321


def soulution():
    n, e = map(int, input().split())
    k = int(input())

    # 간선 정보를 저장하기에는 n*n 사이즈의 2차원 배열보다는 링크드 리스트 형식이 낫다.
    graph = [[] for _ in range(n + 1)]
    table = [INF] * (n + 1)

    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    dijkstra(graph, table, k, n)

    for i in range(1, len(table)):
        if table[i] == INF:
            print("INF")
        else:
            print(table[i])


def dijkstra(graph, table, start, n):
    q = []

    heapq.heappush(q, (0, start))
    table[start] = 0

    while q:
        # 가장 최단 거리값과 해당 노드 꺼내기
        distance, now = heapq.heappop(q)

        # 만약 현재 갱신된 거리가 아까 큐에 넣은 값보다 작으면 무시
        if table[now] < distance:
            continue
        # 인접 노드에 접근해서 최소값 갱신
        for item in graph[now]:
            cost = distance + item[1]

            if cost < table[item[0]]:
                table[item[0]] = cost
                heapq.heappush(q, (cost, item[0]))


soulution()

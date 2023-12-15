import sys
input = sys.stdin.readline
from collections import deque

def solution():
    n, m = map(int, input().split())
    edges = []
    graph = {}
    visited = [True] * (n + 1)
    answer = 0

    for i in range(1, n + 1):
        graph[i] = []

    for _ in range(m):
        edges.append(list(map(int, input().split())))

    for item in edges:
        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])

    for item in graph.keys():
        if visited[item]:
            answer += 1
            bfs(graph, item, visited)

    print(answer)


def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = False

    while q:
        node = q.popleft()

        for item in graph[node]:
            if visited[item]:
                q.append(item)
                visited[item] = False


solution()
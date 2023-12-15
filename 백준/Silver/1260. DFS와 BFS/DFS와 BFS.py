import sys
input = sys.stdin.readline
from collections import deque

def solution():
    n, m, v = map(int, input().split())
    edges = []
    graph = {}
    visited = {}
    for _ in range(m):
        edges.append(list(map(int, input().split())))

    graph[v] = []
    visited[v] = True
    for item in edges:
        if item[0] not in graph.keys():
            graph[item[0]] = []
            visited[item[0]] = True
        if item[1] not in graph.keys():
            graph[item[1]] = []
            visited[item[1]] = True

        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])

    for item in graph.values():
        item.sort()
    dfs(v, graph, visited)
    for key in visited.keys():
        visited[key] = True

    print()
    bfs(graph, v, visited)


def bfs(graph, start, visited):
    q = deque()
    q.append(start)
    visited[start] = False

    while q:
        node = q.popleft()
        print(node, end=" ")
        for item in graph[node]:
            if visited[item]:
                q.append(item)
                visited[item] = False


def dfs(node, graph, visited):
    visited[node] = False
    print(node, end=" ")
    for item in graph[node]:
        if visited[item]:
            dfs(item, graph, visited)


solution()
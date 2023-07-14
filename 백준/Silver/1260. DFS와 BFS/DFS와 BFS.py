from collections import deque
import sys
import copy


def dfs(v):
    for idx in range(n + 1):
        if graph[v][idx] != 0 and visited1[idx]:
            visited1[idx] = False
            answer1.append(idx)
            dfs(idx)


def bfs(v):
    q = deque()
    q.append(v)

    while q:
        node = q.popleft()
        answer2.append(node)
        for i in range(len(graph[node])):
            if graph[node][i] != 0 and visited2[i]:
                visited2[i] = False
                q.append(i)


n, m, v = map(int, input().split())

answer1 = []
answer2 = []

graph = [[0] * (n + 1) for _ in range(n + 1)]

visited1 = [True] * (n + 1)
visited2 = [True] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] += 1
    graph[b][a] += 1

visited1[v] = False
answer1.append(v)

visited2[v] = False


dfs(v)
bfs(v)

for item in answer1:
    print(item,end=" ")
print()
for item in answer2:
    print(item, end=" ")
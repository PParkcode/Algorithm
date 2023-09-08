import sys
import copy
from collections import deque
sys.setrecursionlimit(10**9)


def solutionbyBfs():
    flag = True
    (n, m, k, x) = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)
    visited[x] = 0
    for i in range(m):
        (a, b) = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)

    q = deque()

    q.append(x)

    while q:
        node = q.popleft()
        now = visited[node]
        for item in graph[node]:
            if visited[item] == -1:
                visited[item] = now + 1
                q.append(item)

    for i in range(len(visited)):
        if visited[i] == k:
            print(i)
            flag = False

    if flag:
        print(-1)


solutionbyBfs()
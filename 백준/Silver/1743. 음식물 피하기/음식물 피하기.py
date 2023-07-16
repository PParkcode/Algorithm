import sys
sys.setrecursionlimit(100000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0


def dfs(y, x):
    count = 1
    visited[y][x] = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1 and visited[ny][nx]:
            count += dfs(ny, nx)
    return count


n, m, k = map(int, input().split())

graph = [[0] * m for _ in range(n)]
visited = [[True] * m for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j]:
            answer = max(dfs(i, j), answer)
print(answer)
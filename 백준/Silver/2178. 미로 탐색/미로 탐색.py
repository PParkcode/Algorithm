from collections import deque

dx = [0,1,0,-1]
dy = [1,0,-1,0]
INF = 987654321
def dfs(y,x):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <=nx<m and 0<=ny<n and graph[ny][nx]!=0 and visited[ny][nx] > visited[y][x]+1:
            visited[ny][nx] = visited[y][x]+1
            dfs(ny,nx)


def bfs():
    q = deque()
    q.append((0,0))

    while(q):
        y,x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] != 0 and visited[ny][nx] > visited[y][x] + 1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny,nx))


n,m = map(int,input().split())

graph = []
visited= [[INF]*m for _ in range(n)]
for i in range(n):
    graph.append(list(map(int,input())))

visited[0][0] = 1
bfs()

print(visited[n-1][m-1])
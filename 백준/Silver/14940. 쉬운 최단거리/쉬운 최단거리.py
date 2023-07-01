from collections import deque


def bfs():
    while q:
        val, y, x = q.popleft()


        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if go(ny, nx):
                visited[ny][nx] = True
                answer[ny][nx] = val + 1
                q.append((answer[ny][nx], ny, nx))




def go(y, x):
    if y < 0 or y >= n or x < 0 or x >= m or visited[y][x] == True or graph[y][x] == 0:
        return False

    return True


def find():
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 2:
                q.append((answer[a][b], a, b))
                visited[a][b] = True
                bfs()
                return


n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = []
q = deque()
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(n):
    graph.append(list(map(int, input().split())))

answer = [[0] * m for _ in range(n)]

find()

for i in range(n):
    for j in range(m):
        if visited[i][j] == False and graph[i][j]!=0:
            answer[i][j] = -1

for i in range(n):
    for j in range(m):
        print(answer[i][j] ,end=" ")
    print()
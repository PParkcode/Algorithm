dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfsW(y,x):
    visited[y][x] = False
    time = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <n and 0<= ny <m and graph[ny][nx] =='W' and visited[ny][nx]:
            time += dfsW(ny,nx)
    return time

def dfsB(y, x):
    visited[y][x] = False
    time = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <n and 0<= ny <m and graph[ny][nx] =='B' and visited[ny][nx]:
            time += dfsB(ny,nx) 
    return time


graph = []
answerW=0
answerB=0

n, m = map(int,input().split())
visited =[[True]*n for _ in range(m)]
for _ in range(m):
   graph.append(input())

for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and visited[i][j]:
            temp = dfsW(i,j)
            answerW = (temp * temp) + answerW
            
        if graph[i][j] =='B' and visited[i][j]:
            temp = dfsB(i,j)
            answerB = (temp * temp) + answerB

print(str(answerW)+" "+str(answerB))
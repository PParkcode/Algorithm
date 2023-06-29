import sys
from collections import deque
n,m,k,x = map(int,sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b= map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)

visited = [False] * (n+1)
d = [0] * (n+1)
answer=0
q=deque()
q.append(x)
visited[x]=True
count= 0

d[x]=0
while q:
    

    v = q.popleft()

    for i in range(len(graph[v])):
        if not visited[graph[v][i]]:
            q.append(graph[v][i])
            visited[graph[v][i]] = True
            d[graph[v][i]]= d[v]+1
    count+=1


for i in range(len(d)):
    if d[i]==k:
        answer+=1
        print(i)

if answer==0:
    print(-1)
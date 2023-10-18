# 1. 간선 정보를 내가 사용하기 쉽게 바꾼다.
# 2. 시작 노드로부터 모든 노드에 대하여 최단 거리를 구한다.
# 2-1 이때 힙을 사용하여 구현하자.
# 3. 가장 멀리 떨어진 노드 갯수 반환

# 근데 이거 걍 BFS로 풀 수 있을 것 같은디...
from collections import deque
def solution(n, edge):
    answer = 0
    
    graph = [[] for i in range(n+1)]
    visited = [False] *(n+1)
    table = [0]*(n+1)
    for item in edge:
        graph[item[0]].append(item[1])
        graph[item[1]].append(item[0])
    
    
    answer = bfs(graph,visited,table)
        
    
    return answer

def bfs(graph,visited,table):
    answer = 0
    q = deque()
    q.append(1)
    visited[1] = True
    
    while q:
        node = q.popleft()
        
        for item in graph[node]:
            if not visited[item]:
                q.append(item)
                visited[item] = True
                table[item] = table[node] +1
    
    maxValue = max(table)
    for item in table:
        if item == maxValue:
            answer+=1
    
    return answer
    
            
        
        
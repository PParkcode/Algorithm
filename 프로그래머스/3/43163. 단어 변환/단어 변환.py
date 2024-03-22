from collections import deque
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    graph = {}
    graph[begin] = []
    
    for item in words:
        graph[item]= []
        
    
    for i in range(len(words)):
        for j in range(i,len(words)):
            if check_can_go(words[i],words[j]):
                graph[words[i]].append(words[j])
                graph[words[j]].append(words[i])
    
    if begin not in words:
        for item in words:
            if check_can_go(begin,item):
                graph[item].append(begin)
                graph[begin].append(item)
    
    for key,value in graph.items():
        print(key, value)
        
    answer = search(graph,begin,target)
        
        
    
    return answer


def check_can_go(start,target):
    count = 0
    size = len(start)
    for i in range(size):
        if start[i] == target[i]:
            count+=1
    return count == size -1 

def search(graph,begin,target):
    s = set([begin])
    q = deque()
    q.append((begin,0))
    
    while q:
        node,count = q.popleft()
        for item in graph[node]:
            if node == target:
                return count
            if item in s:
                continue
            q.append((item,count+1))
            s.add(item)
    
    return 0
        
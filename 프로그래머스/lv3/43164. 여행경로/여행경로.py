def solution(tickets):
    answer = []
    dic = {}
    # 티켓정보를 통해 이동 가능 경로 표현
    for item in tickets:
        if item[0] in dic:
            dic[item[0]].append(item[1])
        else:
            dic[item[0]] = []
            dic[item[0]].append(item[1])
        if item[1] not in dic:
            dic[item[1]] = []
    
    # 문자열 순으로 정렬
    for key in dic:
        dic[key].sort()
    
    answer.append("ICN")
    
    for item in dic:
        print(item,dic[item])
    
    # 탐색 시작
    dfs(dic,"ICN",answer,tickets)
    
    return answer
        

def dfs(dic,key,answer,tickets):
    
    for path in dic[key]:
        # 아직 사용하지 않은 티켓에 대하여
        if [key,path] in tickets:
            answer.append(path)
            tickets.remove([key,path])
            dfs(dic,path,answer,tickets)
            
        
    # 잘못 이동했을 경우도 처리해줘야 함
    # 사용하지 않은 티켓이 남았고, 
    if tickets:
        answer.pop()
        
        tickets.append([answer[-1],key])
        return 
        
    
    
    
        

    

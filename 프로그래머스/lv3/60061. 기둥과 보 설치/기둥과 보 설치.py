def solution(n, build_frame):
    answer = []
    
    pillerList = []
    paperList = []
    
    for order in build_frame:
        x = order[0]
        y = order[1]
        item = order[2]
        commend = order[3]
        
        if commend ==0:
            if item == 0:
                deletePiller(x,y,pillerList,paperList)
            if item ==1:
                deletePaper(x,y,pillerList,paperList)
        if commend == 1:
            if item ==0:
                #기둥 설치
                buildPiller(x,y,pillerList,paperList)
            if item ==1:
                # 보 설치
                buildPaper(x,y,pillerList,paperList)
    
    for item in pillerList:
        temp =[]
        temp.append(item[0])
        temp.append(item[1])
        temp.append(0)
        answer.append(temp)
    for item in paperList:
        temp=[]
        temp.append(item[0])
        temp.append(item[1])
        temp.append(1)
        answer.append(temp)
    
    sorted_answer = sorted(answer,key=lambda x: (x[0],x[1],x[2]) )

    return sorted_answer

def buildPiller(x,y,pillerList,paperList):
     #설치 가능 - 바닥에 설치
    if y == 0:
        pillerList.append((x,y))
        
    #설치 가능 - 보 위에 설치
    elif (x,y) in paperList or (x-1,y) in paperList:
        pillerList.append((x,y))
        
    #설치 가능 - 기둥 위에 설치
    elif (x,y-1) in pillerList:
        pillerList.append((x,y))
    
    else:
        return

def buildPaper(x,y,pillerList,paperList):
    # 설치 가능 - 기둥 위 오른쪽 설치
    if (x,y-1) in pillerList:
        paperList.append((x,y))
    # 설치 가능 - 기둥 위 왼쪽 설치
    elif (x+1,y-1) in pillerList:
        paperList.append((x,y))
    
    # 설치 가능 - 양쪽 보와 연결
    elif (x-1,y) in paperList and (x+1,y) in paperList:
        paperList.append((x,y))
    
    else:
        return

def deletePiller(x,y,pillerList,paperList):
    # 기둥 위 오른쪽에 보가 존재할 때
    if (x,y+1) in paperList:
        # 기둥 위 왼쪽에 보가 존재할 때
        if (x-1,y+1) in paperList:
            # 왼쪽 보와 오른쪽 보가 존재할 수 있는 조건
            if ((x-1,y) in pillerList or (x-2,y+1) in paperList) and ((x+1,y) in pillerList or (x+1,y+1) in paperList):
                pillerList.remove((x,y))
                return
            else:
                return
        # 기둥 위 왼쪽 보가 없을 때
        else:
            if (x+1,y) in pillerList:
                pillerList.remove((x,y))
                return
            else:
                return
    
    # 기둥 위 오른쪽 보가 존재하지 않을 때
    else:
        # 기둥 위 왼쪽 보가 존재할 때
        if (x-1,y+1) in paperList:
            if (x-1,y) in pillerList:
                pillerList.remove((x,y))
                return
            else:
                return
        # 기둥위 왼쪽 보가 존재하지 않을 때
        else:
            if (x,y+1) in pillerList:
                return
            else:
                pillerList.remove((x,y))
                return

def deletePaper(x,y,pillerList,paperList):
    # 왼쪽 보가 존재할 때
    if (x-1,y) in paperList:
        # 오른쪽 보가 존재할 때
        if (x+1,y) in paperList:
            # 삭제 가능 조건
            if ((x,y-1) in pillerList or (x-1,y-1) in pillerList) and ((x+1,y-1) in pillerList or (x+2,y-1) in pillerList):
                paperList.remove((x,y))
                return
            else:
                return
                
        
        #왼쪽 보 있고 오른쪽 보 없을때 ---> 여기 기둥 존재 가능 여부에 대해 다뤄야함
        else:
            if (x+1,y) in pillerList:
                if (x+1,y-1) not in pillerList:
                    return
                
            if ((x-1,y-1) in pillerList or (x,y-1) in pillerList):
                paperList.remove((x,y))
                return
                
            else:
                return
            
    
    # 왼쪽 보 없을때
    else:
         # 왼쪽 보 없고 오른쪽 보가 존재할 때
        
        
        if (x,y) in pillerList:
            if (x,y-1) not in pillerList:
                return
            
        if (x+1,y) in paperList:
            if (x+1,y-1) in pillerList or (x+2,y-1) in pillerList:
                paperList.remove((x,y))
                return
            else:
                return
        # 양 옆에 보가 없을 때
        else:
            if (x,y) in pillerList and (x,y-1) not in pillerList:
                return
            elif (x+1,y) in pillerList and (x+1,y-1) not in pillerList:
                return
            else:
                paperList.remove((x,y))
            
            
        
            
                
            
            
            

            
            
    
    
    
        
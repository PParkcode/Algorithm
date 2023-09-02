from collections import deque
def solution(s):
    answer = 1000
    
    if len(s) ==1:
        return 1
    # 모든 경우의 수 진행
    for i in range(1,len(s)):
        result = found(s,i)
        if answer > result:
            answer = result
    
    return answer


def found(s, sliceNum):
    # 문자열 자르고 리스트로 만드는 코드
    # 사용하는 경우가 많을 수 있으니 외우자
    sliceList = [s[i:i+sliceNum] for i in range(0, len(s), sliceNum)]
    
    zip = ""
    count = 1 
    item1 = sliceList.pop(0)
    
    while(sliceList) :
        item2 = sliceList.pop(0)
        # 같은 수 만큼 센다
        if item1 == item2:
            count+=1
        # 문자열이 다를경우
        else:
            if count == 1:
                zip+= item1
            else:
                zip +=str(count)+item1
            item1 = item2
            count = 1
        # 리스트의 마지막이 같아서 else 문을 거치지 않고 while문이 종료되는 경우
        # 남은 중목 문자열들을 처리하자
        if not sliceList:
            if count == 1:
                zip+= item1
            else:
                zip +=str(count)+item1
            item1 = item2
            count = 1
            

    return len(zip)
        
        
        
        
        
    
        
    
    
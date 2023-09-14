def solution(p):
    answer = ''
    
    if isCorrect(p):
        return p
    
    answerList = algorithm(list(p))
    print(answerList)
    answer = ''.join(answerList)
    
    return answer

def algorithm(p):
    count = 0
    temp =[]
    # 빈 문자열인지 체크
    if len(p) == 0:
        return p
    
    # 문자열 u,v 쪼개기
    for i in range(len(p)):
        if p[i] == '(':
            count+=1
        if p[i] == ')':
            count-=1
        if count ==0:
            u = p[0:i+1]
            v = p[i+1:]
            break
    # u가 올바른 문자열
    if isCorrect(u):
        return u + algorithm(v)
    
    else:
        temp.append('(')
        temp = temp + algorithm(v)
        temp.append(')')
        print(u)
        u=reverseList(u)
        print(u)
        return  temp + u
    
        
    
def reverseList(s):
    del s[len(s)-1]
    del s[0]
    
    temp= []
    
    for c in s:
        if c =='(':
            temp.append(')')
        if c ==')':
            temp.append('(')
    return temp
    
def isCorrect(s):
    count = 0
    
    for c in s:
        if c =='(':
            count+=1
        if c ==')':
            count-=1
        if count<0:
            return False
    
    return count == 0
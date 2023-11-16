from collections import deque

def solution(queue1, queue2):
    answer = 0

    sum_q = sum(queue1) + sum(queue2)
    limit = len(queue1)*2 +1
    
    if sum_q % 2 == 1:
        return -1
    
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 =sum(q1)
    sum_q2 = sum(q2)
    
    while sum_q1!=sum_q2:
        if answer>limit:
            return -1
            
        if sum_q1 > sum_q2:
            temp = q1.popleft()
            q2.append(temp)
            sum_q1-=temp
            sum_q2+=temp
        else:
            temp = q2.popleft()
            q1.append(temp)
            sum_q2-=temp
            sum_q1+=temp
        answer +=1
    
    return answer
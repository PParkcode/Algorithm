import itertools

def solution(users, emoticons):
    answer = sol(users,emoticons)
    
    return answer

def sol(users,emoticons):
    answer= []
    sales = [40,30,20,10]
    temp_count = 0
    temp_price = 0
    
    # 모든 중복 순열
    p = list(itertools.product(sales, repeat=len(emoticons)))
    
    #하나의 순열에 대해 
    for item in p:
        for user in users:
            sum = 0
            # 적정 할인율이라면 구매
            for i in range(len(item)):
                if user[0]<=item[i]:
                    sum+= int(emoticons[i]*((100-item[i]))/100)
            # 구매한 값이 설정한 금액보다 높다면 구매인원 +1, 해당 사람의 가격합은 0
            if user[1]<=sum:
                temp_count+=1
                sum = 0
            temp_price+=sum
            
        answer.append((temp_count,temp_price))

        temp_price = 0
        temp_count = 0
    
    # 내림차순 정렬 순서는 구매 인원, 구매 가격 순
    sorted_pairs = sorted(answer, key=lambda answer: (answer[0], answer[1]), reverse =True)
    return sorted_pairs[0]
            
        
                
                    
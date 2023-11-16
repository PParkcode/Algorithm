def solution(survey, choices):
    answer = ""
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0 }
    count =0
    
    for i in range(len(survey)):
        first = survey[i][0]
        second = survey[i][1]
        if choices[i]<4:
            dic[first]= dic[first] + 4 - choices[i]
        if choices[i]>4:
            dic[second] = dic[second] + choices[i] - 4
    
    for item in dic.items():
        if count % 2 == 1:
            if temp[1] < item[1]:
                answer+=item[0]
            else: 
                answer+=temp[0]
            
            count=0
            continue
            
        temp = item
        count+=1
        
        
        
        
    return answer
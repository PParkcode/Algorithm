def solution(nums):
    
    length = len(nums)
    unique = set(nums)

    answer = len(unique)
    if answer < length/2 :
        return answer
    else :
        return length / 2
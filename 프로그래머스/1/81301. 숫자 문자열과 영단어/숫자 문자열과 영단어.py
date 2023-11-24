def solution(s):
    answer = ""
    stack = []
    dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for c in s:
        if str(c).isdigit():
            answer += str(c)
        else:
            stack.append(c)
            if len(stack)>=3:
                answer+=check(stack,dic)
    
    return int(answer)


def check(stack,dic):
    word = ""
    for item in stack:
        word+=item
    if word in dic:
        answer = str(dic[word])
        stack.clear()
        return answer
    return ""
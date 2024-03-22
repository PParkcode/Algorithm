answer = -987654321
def solution():
    global answer
    n = input()
    ls = list(map(int,input().split()))
    # 합을 담을 임시공간
    temp = 0
    for i in range(len(ls)):
        temp = temp + ls[i]
        # 최대값 갱신
        answer = max(answer,temp)
        # 여태까지 담은게 음수가 되었다면 버린다.
        if temp<0:
            temp = 0

    print(answer)

solution()
INF = 2000000001


def solution():
    n, m = map(int, input().split())
    ls = []
    answer = INF
    ls = list((map(int, input().split())))

    s = e = 0
    temp = ls[0]
    while e < n  and s < n :
        if temp < m:
            e += 1
            if e>=n:
                continue
            temp += ls[e]
        else:
            answer = min(answer, e - s)
            temp -= ls[s]
            s += 1

    if answer == INF:
        print(0)
    else:
        print(answer + 1)


solution()
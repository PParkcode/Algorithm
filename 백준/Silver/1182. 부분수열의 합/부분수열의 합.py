from collections import deque

answer = 0


def solution():
    n, s = map(int, input().split())

    arr = list(map(int, input().split()))
    arr.sort()
    total = [0]
    ls = deque()

    recur(arr, n, s, 0, total, ls)
    print(answer)


def recur(arr, n, s, idx, total, ls):
    global answer
    if ls:
        if total[0] == s:
            answer += 1

    for i in range(idx, n):
        total[0] += arr[i]
        ls.append(arr[i])
        recur(arr, n, s, i + 1, total, ls)
        total[0] -= arr[i]
        ls.pop()


solution()
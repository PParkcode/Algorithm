from collections import deque

def solution():
    n, m = map(int, input().split())
    arr = [i for i in range(n + 1)]
    is_used = [False] * (n + 1)
    answer = deque()
    recur(arr, is_used, answer, n, m, 0, 1)


def recur(arr, is_used, answer, n, m, count, idx):
    if count == m:
        for item in answer:
            print(item, end=" ")
        print()
        return

    for i in range(1, n + 1):
        if not is_used[i]:
            is_used[i] = True
            answer.append(arr[i])
            recur(arr, is_used, answer, n, m, count + 1, i + 1)
            is_used[i] = False
            answer.pop()


solution()
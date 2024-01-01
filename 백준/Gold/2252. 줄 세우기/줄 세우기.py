import sys
input = sys.stdin.readline

from collections import deque

def solution():
    n, m = map(int, input().split())
    answer = []
    inDegree = [0] * (n + 1)
    arr = {}
    for i in range(1, n + 1):
        arr[i] = []

    for i in range(m):
        a, b = map(int, input().split())
        arr[a].append(b)
        inDegree[b] += 1
    q = deque()

    for i in range(1, n + 1):
        if inDegree[i] == 0:
            q.append(i)
            inDegree[i] -= 1

    while q:
        node = q.popleft()
        answer.append(node)

        for item in arr[node]:
            if inDegree[item] > 0:
                inDegree[item] -= 1
                if inDegree[item] == 0:
                    q.append(item)
                    inDegree[item] = -1

    for item in answer:
        print(item, end=" ")


solution()
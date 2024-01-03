import sys
input = sys.stdin.readline

import heapq
INF = 987654321

def solution():
    n = int(input())
    cost = [INF] * n
    arr = []
    q = []
    answer = 0
    s = set()
    for i in range(n):
        cost[i] = int(input())

    for i in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n):
        heapq.heappush(q, (cost[i], i))

    while q:
        cost, node = heapq.heappop(q)
        if node in s:
            continue
        answer += cost
        s.add(node)

        for i in range(n):
            if i not in s:
                heapq.heappush(q, (arr[node][i], i))

    print(answer)


solution()
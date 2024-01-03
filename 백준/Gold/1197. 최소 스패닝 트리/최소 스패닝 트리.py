import heapq
import sys
input = sys.stdin.readline

INF = 2000000001


def solution():
    v, e = map(int, input().split())
    answer = 0
    count = 0
    q = []

    for i in range(e):
        a, b, c = map(int, input().split())
        heapq.heappush(q, (c, a, b))

    parents = [i for i in range(v + 1)]

    while q:
        if count == v - 1:
            break
        value, node1, node2 = heapq.heappop(q)
        if find(parents, node1) != find(parents, node2):
            answer += value
            union(parents, node1, node2)
            count += 1

    print(answer)


def find(parents, x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents, parents[x])
        return parents[x]


def union(parents, x, y):
    rootX = find(parents, x)
    rootY = find(parents, y)
    parents[rootY] = rootX


solution()
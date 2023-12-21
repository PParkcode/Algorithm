import sys
input = sys.stdin.readline
from collections import deque

def solution():
    n = int(input())
    parents = [0] * (n + 1)
    tree = {}

    for i in range(n + 1):
        tree[i] = []

    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    q = deque()
    q.append(1)
    parents[1] = 1

    while q:
        node = q.popleft()
        for item in tree[node]:
            if parents[item] != 0:
                continue
            q.append(item)
            parents[item] = node

    for i in range(2, n + 1):
        print(parents[i])


solution()

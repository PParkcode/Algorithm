from collections import deque

def solution():
    a, b = map(int, input().split())
    q = deque()
    q.append(a)
    q2 = deque()
    q2.append((a, 1))

    dic = {}

    while q:
        node = q.popleft()

        if node not in dic.keys():
            dic[node] = []

        if node * 2 <= b:
            q.append(node * 2)
            dic[node].append(node * 2)

        temp = int(str(node) + "1")
        if temp <= b:
            dic[node].append(temp)
            q.append(temp)

    while q2:
        node = q2.popleft()
        if node[0] == b:
            print(node[1])
            return

        for item in dic[node[0]]:
            q2.append((item, node[1] + 1))

    print(-1)


solution()
from collections import deque


def solution():
    k = int(input())
    ls = list(map(int, input().split()))
    q = deque(ls)
    dic = {}
    for i in range(1, 2 ** k):
        dic[i] = 0

    inorder(dic, q, 1, 2 ** k)

    depth = 1
    for k, v in dic.items():
        print(v, end=" ")
        if k == 2 ** depth - 1:
            depth += 1
            print()


def inorder(dic, q, root, maximum):
    if root >= maximum:
        return
    inorder(dic, q, root * 2, maximum)
    node = q.popleft()
    dic[root] = node
    inorder(dic, q, root * 2 + 1, maximum)


solution()

from collections import deque

def solution():
    n = int(input())
    q = deque()

    hanoi(n, 1, 2, 3, q)

    print(len(q))

    while q:
        a, b = q.popleft()
        print(str(a) + " " + str(b))


def hanoi(n, start, mid, end, q):
    # 원판이 하나라면, start에서 end로 보내라
    if n == 1:
        q.append((start, end))
        return

    # n-1개의 원판을 start에서 mid로 보내라.
    hanoi(n-1,start,end,mid,q)
    # n번째 원판을 start에서 end로 보내라
    q.append((start,end))
    #다시 가운데에 있는 n-1개의 원판을 end로 보내라.
    hanoi(n-1,mid,start,end,q)

solution()
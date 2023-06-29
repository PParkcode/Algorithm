import sys
from collections import deque


def spread(v, ny, nx,count):
    if ny < 0 or nx < 0 or ny > (n - 1) or nx > (n - 1) or arr[ny][nx] != 0 or count>=s:
        return

    arr[ny][nx] = v
    q.append((v, ny, nx,count+1))


n, k = map(int, sys.stdin.readline().rstrip().split())
arr = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

temp = []
q = deque()
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))
s, x, y = map(int, sys.stdin.readline().rstrip().split())

for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            # 모든 경우의 수를 값과 좌표를 큐에 담음
            temp.append((arr[i][j], i, j, 0))
temp.sort()
q = deque(temp)


# 요구하는 초만큼 반복

# 큐가 빌 때까지 값과 모든 경우의 수에 대해 바이러스 전파
while q:
    val, ty, tx, count = q.popleft()
    for d in range(4):
        spread(val, ty + dy[d], tx + dx[d],count)

print(arr[x - 1][y - 1])
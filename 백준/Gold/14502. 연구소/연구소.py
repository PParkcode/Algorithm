
import sys
import copy

"""
1. 데이터 입력 받기 V
2. 모든 경우의 수에 대해 벽 3개 세우기 V
 2.1 재귀를 사용?V
3. 벽이 3개 세워지면 바이러스 퍼뜨림V
4. 안전 영역 계산 V
5. 데이터 원상복구 V
 --> arr 배열에는 벽만 설치
    temp 배열에 arr 배열 값을 복사하고,
    temp 배열에서 바이러스를 퍼뜨리고 안전영역 계산
    arr 배열은 벽만 설치하고 그 데이터를 temp에 전해주기만 하면됨
    

궁금한 점 
3중 for문을 통해 모든 벽을 세울 수는 없을까?

"""


def wall(count):
    global answer
    if count == 3:
        # 바이러스를 퍼뜨려야 함

        # temp에 배열 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = arr[i][j]

        # 바이러스 전파
        for i in range(n):
            for j in range(m):
                if arr[i][j] == 2:
                    virus(j, i)
        answer = max(countSafe(), answer)
        return

    # 모든 경우의 수에 대해 벽 세움
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(count + 1)
                arr[i][j] = 0


def virus(x, y):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if nx < 0 or nx >= m or ny < 0 or ny >= n or temp[ny][nx] != 0:
            continue
        temp[ny][nx] = 2
        virus(nx, ny)


def countSafe():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1

    return count


n, m = map(int, input().split())
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
arr = []
temp = [[0] * m for _ in range(n)]
answer = 0

for i in range(n):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

wall(0)

print(answer)
import sys
import copy
from collections import deque

sys.setrecursionlimit(10 ** 9)


def solution():
    board = []
    answer = 0
    n, l, r = map(int, input().split())
    for _ in range(n):
        board.append(list(map(int, input().split())))

    while True:

        count = 1
        # 연합 번호와 평균값을 Pair로 저장할 리스트
        unionData = []
        # 연합 번호를 저장할 리스트
        unionBoard = [[0] * n for _ in range(n)]

        # 연합 정보 찾기
        for i in range(n):
            for j in range(n):
                if unionBoard[i][j] == 0:
                    total = bfs(board, unionBoard, n, l, r, i, j, count)
                    # 만약 평균이 현재 값과 같다면 오류 남
                    if total != -1:
                        unionData.append((count, total))
                        count += 1

        # 더 이상 이동 가능한 국가가 없는 경우 반복문 탈출
        if count == 1:
            break

        # 연합 인구 이동
        while unionData:
            unionNum, num = unionData.pop(0)
            for i in range(n):
                for j in range(n):
                    if unionBoard[i][j] == unionNum:
                        board[i][j] = num

        answer += 1

    print(answer)


def bfs(board, unionBoard, n, l, r, y, x, count):
    q = deque()

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    total = board[y][x]
    unionNum = 1
    q.append((y, x))

    while q:

        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n and unionBoard[ny][nx] == 0 and l <= abs(board[y][x] - board[ny][nx]) <= r:
                q.append((ny, nx))
                unionBoard[y][x] = count
                unionBoard[ny][nx] = count
                total += board[ny][nx]
                unionNum += 1

    # 연합 가능한 국가가 없다면 -1 리턴
    if unionNum == 1:
        return -1
    return total // unionNum


solution()
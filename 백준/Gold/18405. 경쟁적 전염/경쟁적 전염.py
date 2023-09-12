import sys
import copy
from collections import deque

sys.setrecursionlimit(10 ** 9)


def solution():
    n, k = map(int, input().split())

    board = []

    for i in range(n):
        board.append(list(map(int, input().split())))
    s, x, y = map(int, input().split())

    virus(board, n, k, s)

    print(board[x - 1][y - 1])


def virus(board, n, k, s):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 바이러스 번호와 좌표를 담을 리스트
    virusIndex = []
    count = 0
    time = 0

    q = deque()

    # 바이러스를 담고 번호순 대로 정렬하여 큐에 담는다.
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                virusIndex.append((i, j, board[i][j]))

    sortedvirus = sorted(virusIndex, key=lambda x: (x[2]))

    for item in sortedvirus:
        q.append((item[0], item[1]))

    # 큐 사이즈만큼 돌면 1초가 지났다고 생각
    qsize = len(q)

    # BFS로 진행
    while q:

        y, x = q.popleft()
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[ny][nx] == 0:
                board[ny][nx] = board[y][x]
                q.append((ny, nx))

        # count를 하나씩 증가하면서 qSize와 같아지면 1초가 지난것이다.
        # qsize를 현재 큐의 사이즈로 갱시해주고 count =0 시간은 1증가시킨다.
        if count == qsize:
            qsize = len(q)
            count = 0
            time += 1

        # return 조건
        if time == s:
            return


solution()
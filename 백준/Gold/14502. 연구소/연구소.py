import sys
import copy
from collections import deque

sys.setrecursionlimit(10 ** 9)

answer = 0


def solution():
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(map(int, input().split())))

    wall(board, 0, n, m, 0, 0)

    print(answer)


# 벽을 세우는 함수
def wall(board, count, n, m, a, b):
    global answer

    # 벽이 3개 세워지면 바이러스를 퍼뜨린다
    if count == 3:
        answer = max(answer, virus(board, n, m))
        return

    # 전체 배열을 순회하며 벽을 하나씩 세운다. 재귀를 이용해 모든 경우의 수에 대해 벽 3개를 세운다.
    for i in range(a, n):
        for j in range(m):
            if i == a and j < b:
                continue
            if board[i][j] == 0:
                board[i][j] = 1
                wall(board, count + 1, n, m, i, j)  # count를 하나씩 증가해가며 벽을 세움
                board[i][j] = 0


# BFS를 이용하여 바이러스를 퍼뜨린다.
def virus(board, n, m):
    safeArea = 0
    tempBoard = copy.deepcopy(board)
    visited = [[True] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if tempBoard[i][j] == 2 and visited[i][j]:
                bfs(tempBoard, visited, n, m, i, j)

    # 바이러스를 모두 퍼뜨리면 안전 구역 계산후 반환
    for i in range(n):
        for j in range(m):
            if tempBoard[i][j] == 0:
                safeArea += 1
    return safeArea


# BFS를 이용한 바이러스 전파
def bfs(tempBoard, visited, n, m, a, b):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = deque()
    q.append((a, b))
    visited[a][b] = False
    while q:
        y, x = q.popleft()
        tempBoard[y][x] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and tempBoard[ny][nx] == 0 and visited[ny][nx]:
                q.append((ny, nx))
                visited[ny][nx] = False


solution()
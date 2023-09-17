import sys
import copy
from collections import deque

sys.setrecursionlimit(10 ** 9)
answer = "NO"


def solution():
    n = int(input())
    board = []
    for i in range(n):
        board.append(list(input().split()))

    wall(board, n, 0, 0, 0)
    print(answer)


def wall(board, n, a, b, count):
    global answer
    if count == 3:
        # 선생님 감시 시작
        result = watch(board, n)
        # 이때 Stack의 모든 재귀함수들을 return 하고 싶은데...
        # 감시에 피할 수 있는 경우가 있다면 True를 리턴하여 다른 재귀함수도 종료할 수 있게 해준다.
        if result:
            answer = "YES"
            return True
        return False

    # 장애물 3개 설치
    for i in range(a, n):
        for j in range(n):
            if i == a and j < b:
                continue
            if board[i][j] == 'X':
                board[i][j] = 'O'
                # 감시에 안걸릴 경우가 있다면 True를 리턴하여 모든 재귀 종료
                if wall(board, n, i, j, count + 1):
                    return True
                board[i][j] = 'X'


# 선생님 감시
def watch(board, n):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    flag = True

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'T':
                # 4 방향에 대해 while문 진행
                for k in range(4):
                    y = i
                    x = j
                    while True:
                        y = y + dy[k]
                        x = x + dx[k]

                        if 0 <= x < n and 0 <= y < n:
                            if board[y][x] == 'S':
                                # 이 경우에는 감시에 들킴
                                flag = False
                                return flag

                            if board[y][x] == 'O':
                                break
                        else:
                            break
    return flag


solution()
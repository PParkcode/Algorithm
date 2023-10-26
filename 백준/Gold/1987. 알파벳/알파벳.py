import sys

input = sys.stdin.readline

answer = 0


def solution():
    r, c = map(int, input().split())

    graph = [[] for _ in range(r)]
    s = [False]*26
    for i in range(r):
        temp = input()
        for j in range(c):
            graph[i].append(temp[j])

    dfs(graph, 0, 0, s, r, c,1)
    print(answer)


def dfs(graph, x, y, s, r, c,count):
    global answer
    
    # 아스키 코드로 변환
    start = ord('A')
    s[start-ord(graph[y][x])] = True
    answer = max(answer, count)
    if answer ==26:
        return

    # 하우상좌 순으로
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < c and 0 <= ny < r and not s[start-ord(graph[ny][nx])]:
            dfs(graph, nx, ny, s, r, c,count+1)
            s[start-ord(graph[ny][nx])] = False


solution()

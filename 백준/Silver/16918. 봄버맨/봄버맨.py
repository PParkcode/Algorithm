from collections import deque


def solution():
    r, c, n = map(int, input().split())
    graph = []
    q = deque()

    for i in range(r):
        graph.append(list(input()))

    # 초기 폭탄 위치 저장
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "O":
                q.append((i, j))

    # 시작
    play(graph, r, c, n, q)

    for i in range(r):
        for j in range(c):
            print(graph[i][j], end="")
        print()


def play(graph, r, c, n, q):
    count = 1

    # 지정된 초가 넘지 않을 때 까지 반복
    while count < n:
        count += 1
        # 모든 공간 폭탄 채우기
        fill(graph, r, c)
        # 지정된 시간이면 리턴
        if count == n:
            return

        # 큐에 들어 있는 좌표를 폭발
        boom(graph, r, c, q)
        count += 1


# 모든 좌표에 폭탄으로 채우기
def fill(graph, r, c):
    for i in range(r):
        for j in range(c):
            graph[i][j] = "O"


# 폭발
def boom(graph, r, c, q):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        y, x = q.popleft()
        graph[y][x] = "."

        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < r and 0 <= nx < c:
                graph[ny][nx] = "."
    # 폭발 후 남은 폭탄 좌표 저장
    addQueue(graph, r, c, q)


# 폭발 후 남은 폭탄 좌표 저장
def addQueue(graph, r, c, q):
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "O":
                q.append((i, j))


solution()
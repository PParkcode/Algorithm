from collections import deque


def solution():
    r, c, t = map(int, input().split())
    graph = []
    q = deque()
    up = 0
    down = 0
    for i in range(r):
        graph.append(list(map(int, input().split())))

    # 미세 먼지 위치 찾기
    search(graph, q, r, c)

    # 공기 청정기 위치 찾기
    for i in range(r):
        if graph[i][0] == -1:
            up = i
            down = i + 1
            break

    simulate(graph, q, r, c, t, up, down)
    answer = calculate(graph, r, c)

    print(answer)


def simulate(graph, q, r, c, t, up, down):
    time = 0
    while True:
        if time == t:
            return
        spread(graph, q, r, c)
        move(graph, r, c, up, down)
        search(graph, q, r, c)
        time += 1


def spread(graph, q, r, c):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        y, x, spread_unit = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < c and 0 <= ny < r and graph[ny][nx] != -1:
                graph[ny][nx] += spread_unit
                graph[y][x] -= spread_unit


def move(graph, r, c, up, down):
    run_up_air_cleaner(graph, r, c, up, down)
    run_down_air_cleaner(graph, r, c, up, down)


def run_up_air_cleaner(graph, r, c, up, down):
    if up != 0:
        for i in range(up - 1, -1, -1):
            if graph[i + 1][0] == -1:
                continue
            graph[i + 1][0] = graph[i][0]

    for j in range(1, c):
        if graph[0][j - 1] == -1:
            continue
        graph[0][j - 1] = graph[0][j]

    for i in range(1, up + 1):
        graph[i - 1][c - 1] = graph[i][c - 1]

    for j in range(c - 2, 0, -1):
        graph[up][j + 1] = graph[up][j]

    graph[up][1] = 0


def run_down_air_cleaner(graph, r, c, up, down):
    if down != r - 1:
        for i in range(down + 1, r):
            if graph[i - 1][0] == -1:
                continue
            graph[i - 1][0] = graph[i][0]

    for j in range(1, c):
        if graph[r - 1][j - 1] == -1:
            continue
        graph[r - 1][j - 1] = graph[r - 1][j]

    for i in range(r - 2, down - 1, -1):
        graph[i + 1][c - 1] = graph[i][c - 1]

    for j in range(c - 2, 0, -1):
        graph[down][j + 1] = graph[down][j]

    graph[down][1] = 0


# 미세 먼지 지수 5 이상인 곳 찾기
def search(graph, q, r, c):
    for i in range(r):
        for j in range(c):
            if graph[i][j] >= 5:
                # graph[i][j] 값도 저장하고 있어야 함
                q.append((i, j, graph[i][j] // 5))


# 결과 계산
def calculate(graph, r, c):
    result = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] == -1:
                continue
            result += graph[i][j]
    return result


solution()
from collections import deque


def solution():
    m, n = map(int, input().split())

    graph = []
    q = deque()

    for i in range(n):
        graph.append(list(map(int, input().split())))

    # 초기 토마토 위치 저장
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j))

    # 탐색
    answer = bfs(q, n, m, graph)

    # 안 익은 토마토 있는지 확인
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                print(-1)
                return

    print(answer - 1)


def bfs(q, n, m, graph):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    answer = 0
    # 임시로 다음 토마토를 저장할 큐
    temp_q = deque()

    # 큐가 빌 때 까지 동작
    while q:

        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 0:
                temp_q.append((ny, nx))
                graph[ny][nx] = 1

        # 큐가 다 비었다면, 하루가 지난것이다.
        # 임시큐에 넣어 놓은 값을 메인 큐로 옮기자 
        if len(q) == 0:
            answer += 1
            while temp_q:
                q.append(temp_q.popleft())

    return answer

solution()
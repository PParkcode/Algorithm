from collections import deque


def solution():
    graph = []

    for i in range(8):
        graph.append(list(input()))


    answer = play(graph)

    print(answer)
def play(graph):
    main_q = deque()
    main_q.append((7, 0))
    temp_q = deque()

    # 대기, 상, 우상, 우, 우하,  좌하, 좌, 좌상
    dy = [0, -1, -1, 0, 1, 1, 0, -1]
    dx = [0, 0, 1, 1, 1, -1, -1, -1]

    while main_q:
        y, x = main_q.popleft()
        # 목표 지점에 도달 했다면 리턴
        if y == 7 and x ==7:
            return 1

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < 8 and 0 <= ny < 8 and graph[ny][nx] != "#":
                # 갈 수 있는 모든 경우의 수를 temp_q에 넣는다.
                temp_q.append((ny, nx))
        
        # 갈 수 있는 모든 경우의 수에 대해 벽 이동 후 충돌하는지 확인
        # 충돌이 없다면 main_q에 넣어준다
        if len(main_q) == 0:
            move_wall(graph)
            while temp_q:
                ty,tx = temp_q.popleft()
                if graph[ty][tx] !="#":
                    main_q.append((ty,tx))
    return 0

# 벽 이동
def move_wall(graph):
    for i in range(6,-1,-1):
        graph[i+1] = graph[i]
    graph[0] = [".",".",".",".",".",".",".","."]


solution()
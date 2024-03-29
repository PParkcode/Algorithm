from collections import deque
import heapq

answer = 0


def solution():
    graph = []
    n, m = map(int, input().split())
    visited = [[True] * m for _ in range(n)]

    for i in range(n):
        graph.append(list(map(int, input().split())))

    simulate(graph, visited, n, m)
    print(answer)


def simulate(graph, visited, n, m):
    q = deque()
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            q.append((i, j))
            recur(graph, visited, n, m, i, j, 1, graph[i][j], q)
            visited[i][j] = True

    another(graph, n, m)


def recur(graph, visited, n, m, y, x, count, score, q):
    global answer
    # depth가 4가되면 정답 갱신후 리턴
    if count == 4:
        answer = max(answer, score)
        return

    # 우하좌상 순
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m and visited[ny][nx]:
            visited[ny][nx] = False
            # depth를 1 증가시키고, score도 갱신하여 재귀 실행
            recur(graph, visited, n, m, ny, nx, count + 1, score + graph[ny][nx], q)
            visited[ny][nx] = True


# ㅗ,ㅓ,ㅏ,ㅜ 의 경우는 이 방법으로 해줘야한다.
def another(graph, n, m):
    global answer
    q = []
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    for i in range(n):
        for j in range(m):
          
            result = graph[i][j]
            # 4가지 방향값을 일단 다 더한다.
            # 그리고 4 방향 중에서 최소 값을 빼준다.
            for k in range(4):
                ny = dy[k] + i
                nx = dx[k] + j
                if 0 <= ny < n and 0 <= nx < m:
                    result += graph[ny][nx]
                    heapq.heappush(q, graph[ny][nx])
            if len(q)< 3:
                q.clear()
                continue
            if len(q) == 4:
                result -= heapq.heappop(q)
            answer = max(answer, result)
            q.clear()


solution()
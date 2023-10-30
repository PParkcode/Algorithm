import sys
import heapq
from collections import deque

input = sys.stdin.readline


"""
1. 먹을 수 있는 물고기를 찾아야 함
2. 먹을 수 있는 물고기가 2마리 이상이면 가장 가까운 물고기로 이동
3. 거리가 가까운 물고기가 두마리 이상이면 가장 위쪽으로. 위쪽에서는 왼쪽으로

4. 먹으면 크기 증가(초기 값은 2)
5. 내 크기만큼 먹어야 크기 증가 -> 즉 두마리를 먹어야 3이 될 수 있음
"""


def solution():
    answer = 0
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    mySize = 2
    count = 0

    # 처음 내 위치 찾기
    a, b = findMyPlace(graph, n)

    while True:
        # 내 숫자만큼 먹었다면 사이즈 업
        if count == mySize:
            count = 0
            mySize += 1

        # 현재 위치와 이동 수 만큼 반환
        result = findFish(graph, a, b, mySize, n)
        a, b, temp = result
        answer += temp
        if temp == 0:
            break

        count += 1

    print(answer)


def printGraph(graph):
    for item in graph:
        print(item)
    print()


def findMyPlace(graph, n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                return j, i


def findFish(graph, a, b, mySize, n):
    # 이동 수를 담을것, 0이 아니라면 한번은 방문한거
    visited = [[0] * n for _ in range(n)]

    # 상좌우하 순
    dy = [-1, 0, 0, 1]
    dx = [0, -1, 1, 0]
    graph[b][a] = 0

    q = []
    # 우선순위 큐를 사용하자 - 순서는 거리, y좌표, x좌표 순으로 작은것을 꺼냄
    heapq.heappush(q, (0, b, a))

    while q:
        value, y, x = heapq.heappop(q)
        # 0이 아니지만 나보다 작다면 먹이 발견!
        if graph[y][x] < mySize and graph[y][x] != 0:
            graph[y][x] = 9
            return x, y, visited[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < n and 0 <= ny < n and visited[ny][nx] == 0 and graph[ny][nx] <= mySize:
                visited[ny][nx] = visited[y][x] + 1
                heapq.heappush(q, (visited[ny][nx], ny, nx))

    # 먹이를 못찾았을 때
    return 0, 0, 0


solution()

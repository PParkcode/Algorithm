import copy
from collections import deque


def solution(places):
    answer = []
    people = []
    for place in places:
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    people.append((i, j))

        answer.append(findDistance(people, place))
        people.clear()
    print(answer)
    return answer


def findDistance(people, place):
    temp_place = copy.deepcopy(place)
    for item in people:
        if not bfs(temp_place, item[0], item[1]):
            return 0
    return 1


def bfs(temp_place, y, x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    visited = [[0] * 5 for _ in range(5)]
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    
    while q:
        y, x = q.popleft()
        if visited[y][x] >= 4:
            return True

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == 0 and temp_place[ny][nx] != 'X':
                q.append((ny, nx))
                visited[ny][nx] = visited[y][x] + 1
                if temp_place[ny][nx] == 'P' and visited[ny][nx]<=3:
                    return False
    return True
    
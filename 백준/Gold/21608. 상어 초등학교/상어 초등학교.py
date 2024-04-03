def solution():
    n = int(input())
    graph = [[0] * n for _ in range(n)]

    students = []

    students_seat = {}
    for i in range(1, (n * n) + 1):
        students_seat[i] = (0, 0)

    for i in range(n * n):
        students.append(list(map(int, input().split())))
    answer = simulate(students, graph, students_seat, n)

    print(answer)


def simulate(students, graph, students_seat, n):
    answer = 0
    for student in students:
        target = student[0]
        candidates = process_1(graph, student, n)
        if len(candidates) == 0:
            y, x = process_2(graph, candidates, n)

        elif len(candidates) == 1:
            y = candidates[0][0]
            x = candidates[0][1]
        else:
            y, x = process_2(graph, candidates, n)
        
        graph[y][x] = target
        students_seat[target] = (y, x)

    for student in students:
        y, x = students_seat[student[0]]
        answer += calculate(graph, y, x, n, student[1], student[2], student[3], student[4])

    return answer


# 각 자리 후보들 구하기
def process_1(graph, student, n):
    ls = []
    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0:
                count = check_friends(graph, i, j, n, student[1], student[2], student[3], student[4])
                if count == result:
                    ls.append((i, j))
                if count > result:
                    result = count
                    ls.clear()
                    ls.append((i, j))
    return ls


def process_2(graph, candidates, n):
    max = 0
    ls = []
    for candidate in candidates:
        count = check_empty_seat(graph, candidate[0], candidate[1], n)
        if count == 4:
            return (candidate[0], candidate[1])
        elif max == count:
            ls.append((candidate[0], candidate[1]))
        elif max < count:
            max = count
            ls.clear()
            ls.append((candidate[0], candidate[1]))
    return ls[0]


def check_empty_seat(graph, y, x, n):
    count = 0

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x

        if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == 0:
            count += 1

    return count


def check_friends(graph, y, x, n, f1, f2, f3, f4):
    count = 0

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x

        if 0 <= ny < n and 0 <= nx < n and (
                graph[ny][nx] == f1 or graph[ny][nx] == f2 or graph[ny][nx] == f3 or graph[ny][nx] == f4):
            count += 1

    return count


def calculate(graph, y, x, n, f1, f2, f3, f4):
    count = 0

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x

        if 0 <= ny < n and 0 <= nx < n and (
                graph[ny][nx] == f1 or graph[ny][nx] == f2 or graph[ny][nx] == f3 or graph[ny][nx] == f4):
            count += 1

    if count == 4:
        return 1000
    elif count == 3:
        return 100
    elif count == 2:
        return 10
    elif count == 1:
        return 1
    else:
        return 0


solution()
INF = 987654321
answer = INF


def solution():
    n, m = map(int, input().split())
    graph = []
    # 치킨집과 가정집의 좌표를 담을 리스트
    chickens = []
    houses = []

    for i in range(n):
        graph.append(list(map(int, input().split())))

    # 치킨집과 집 좌표 저장
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 2:
                chickens.append((i, j))
            if graph[i][j] == 1:
                houses.append((i, j))
    # 재귀 시작
    recur(chickens, set(), houses, 0, 0, m)

    print(answer)


# 재귀문
# 탈출 조건: count == answer 이면 치킨 거리 계산 후 answer 갱신
# 선택한 치킨집이 m개가 될 때 까지 temp_chickens에 담는다.
# m개가 된다면 치킨 거리 계산
# 계산을 마친 후 계속 반복문 진행
# temp_chickens는 시간 복잡도 최적화를 위해 set으로 설정 O(1)
def recur(chickens, temp_chickens, houses, idx, count, m):
    global answer
    if count == m:
        answer = min(answer, calculate(temp_chickens, houses))
        return

    for i in range(idx, len(chickens)):
        y, x = chickens[i]
        temp_chickens.add((y, x))
        recur(chickens, temp_chickens, houses, i + 1, count + 1, m)
        temp_chickens.remove((y, x))


def calculate(temp_chickens, houses):
    chicken_distance = 0

    # 각각의 집들에 대해 살아남은 치킨집들 중 최소거리를 구하고,
    # 최소 거리들을 합해 치킨 거리를 반환해 준다.
    for house in houses:
        distance = INF
        house_y = house[0]
        house_x = house[1]
        for chicken in temp_chickens:
            chicken_y = chicken[0]
            chicken_x = chicken[1]
            distance = min(distance, abs(house_y - chicken_y) + abs(house_x - chicken_x))
        chicken_distance += distance

    return chicken_distance


solution()
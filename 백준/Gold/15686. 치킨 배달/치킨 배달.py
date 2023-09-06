from itertools import combinations


def solution():
    (n, m) = map(int, input().split())
    arr = []
    chickenList = []
    houseList = []
    for _ in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                chickenList.append((i, j))
            if arr[i][j] == 1:
                houseList.append((i, j))

    # 파이썬의 조합 기능 이용
    # 재귀와 bfs이용시 시간 초과 발생 하여 이 기능 사용
    candidates = list(combinations(chickenList, m))

    print(selectbyCombination(arr, houseList, candidates, m))


"""
기존에는 bfs를 이용하여 거리를 구했지만 시간 초과가 났다.
그래서 index를 이용해서 필요한 거리만 구하는 방식으로 수정
"""
def selectbyCombination(arr, houseList, candidates, m):
    distanceSum = 0
    chickenDistance = 999999999999
    chicenIndex = []

    # 후보군들을 하나씩 pop
    while candidates:
        distanceSum = 0
        chicenIndex.clear()
        index = candidates.pop(0)


        for i in range(m):
            chicenIndex.append((index[i][0], index[i][1]))

        # 집 하나당 치킨 집과의 거리를 모두 비교함
        for house in (houseList):
            houseY = house[0]
            houseX = house[1]
            distance = 9999999999
            for chicken in chicenIndex:
                y = chicken[0] - houseY
                x = chicken[1] - houseX
                if y < 0:
                    y = y * (-1)
                if x < 0:
                    x = x * (-1)
                distance = min(distance, x + y)

            distanceSum += distance

        chickenDistance = min(distanceSum, chickenDistance)


    return chickenDistance

solution()

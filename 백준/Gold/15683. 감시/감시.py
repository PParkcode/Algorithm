import copy

answer = 987654321


def solution():
    n, m = map(int, input().split())
    arr = []
    cctv = []
    for i in range(n):
        arr.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 or arr[i][j] == 2 or arr[i][j] == 3 or arr[i][j] == 4 or arr[i][j] == 5:
                cctv.append((i, j, arr[i][j]))

    recur(arr, cctv, n, m, 0)
    print(answer)


def recur(arr, cctv, n, m, idx):
    global answer

    if idx >= len(cctv):
        answer = min(searchSafe(arr, n, m), answer)
        return

    y = cctv[idx][0]
    x = cctv[idx][1]
    v = cctv[idx][2]

    if v == 1:
        cctv1(arr, y, x, n, m, idx, cctv)

    if v == 2:
        cctv2(arr, y, x, n, m, idx, cctv)

    if v == 3:
        cctv3(arr, y, x, n, m, idx, cctv)

    if v == 4:
        cctv4(arr, y, x, n, m, idx, cctv)

    if v == 5:
        cctv5(arr, y, x, n, m, idx, cctv)


def fill(arr, y, x, dir, n, m):
    # 상
    if dir == 1:
        for i in range(y - 1, -1, -1):
            if arr[i][x] == 6:
                break
            arr[i][x] = -1
    # 하
    if dir == 2:
        for i in range(y + 1, n):
            if arr[i][x] == 6:
                break
            arr[i][x] = -1

    # 좌
    if dir == 3:
        for j in range(x - 1, -1, -1):
            if arr[y][j] == 6:
                break
            arr[y][j] = -1
    # 우
    if dir == 4:
        for j in range(x + 1, m):
            if arr[y][j] == 6:
                break
            arr[y][j] = -1


def cctv1(arr, y, x, n, m, idx, cctv):
    time = 4

    for i in range(time):
        deep_copy = copy.deepcopy(arr)
        fill(deep_copy, y, x, i + 1, n, m)
        recur(deep_copy, cctv, n, m, idx + 1)


def cctv2(arr, y, x, n, m, idx, cctv):
    time = 2
    deep_copy = copy.deepcopy(arr)
    fill(deep_copy, y, x, 1, n, m)
    fill(deep_copy, y, x, 2, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)
    deep_copy = copy.deepcopy(arr)

    fill(deep_copy, y, x, 3, n, m)
    fill(deep_copy, y, x, 4, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)
    deep_copy = copy.deepcopy(arr)


def cctv3(arr, y, x, n, m, idx, cctv):
    time = 4
    deep_copy = copy.deepcopy(arr)

    fill(deep_copy, y, x, 1, n, m)
    fill(deep_copy, y, x, 3, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)
    deep_copy = copy.deepcopy(arr)

    fill(deep_copy, y, x, 1, n, m)
    fill(deep_copy, y, x, 4, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)
    deep_copy = copy.deepcopy(arr)

    fill(deep_copy, y, x, 2, n, m)
    fill(deep_copy, y, x, 3, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)
    deep_copy = copy.deepcopy(arr)

    fill(deep_copy, y, x, 2, n, m)
    fill(deep_copy, y, x, 4, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)
    deep_copy = copy.deepcopy(arr)


def cctv4(arr, y, x, n, m, idx, cctv):
    time = 4

    deep_copy = copy.deepcopy(arr)
    fill(deep_copy, y, x, 1, n, m)
    fill(deep_copy, y, x, 2, n, m)
    fill(deep_copy, y, x, 3, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)
    deep_copy = copy.deepcopy(arr)

    fill(deep_copy, y, x, 1, n, m)
    fill(deep_copy, y, x, 2, n, m)
    fill(deep_copy, y, x, 4, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)
    deep_copy = copy.deepcopy(arr)

    fill(deep_copy, y, x, 1, n, m)
    fill(deep_copy, y, x, 3, n, m)
    fill(deep_copy, y, x, 4, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)
    deep_copy = copy.deepcopy(arr)

    fill(deep_copy, y, x, 2, n, m)
    fill(deep_copy, y, x, 3, n, m)
    fill(deep_copy, y, x, 4, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)
    deep_copy = copy.deepcopy(arr)


def cctv5(arr, y, x, n, m, idx, cctv):
    deep_copy = copy.deepcopy(arr)

    fill(deep_copy, y, x, 1, n, m)
    fill(deep_copy, y, x, 2, n, m)
    fill(deep_copy, y, x, 3, n, m)
    fill(deep_copy, y, x, 4, n, m)
    recur(deep_copy, cctv, n, m, idx + 1)


def searchSafe(arr, n, m):
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                count += 1
    return count


solution()
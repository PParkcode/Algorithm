def solution():
    n, r, c = map(int, input().split())

    recur(2 ** n, r, c, 0)


def recur(n, r, c, count):
    if n == 1:
        print(count)
        return

    new_n = n // 2
    # 몇 사분면인지 위치 확인
    # 확인 했으면 해당 사분면에서 재귀 함수 진행
    # 사분면만큼 값을 더해주자.
    if r < new_n:
        if c < new_n:
            recur(new_n, r, c, count)
        else:
            recur(new_n, r, c - new_n, count + new_n ** 2)
    else:
        if c < new_n:
            recur(new_n, r - new_n, c, count + (new_n ** 2 * 2))
        else:
            recur(new_n, r - new_n, c - new_n, count + (new_n ** 2 * 3))


solution()
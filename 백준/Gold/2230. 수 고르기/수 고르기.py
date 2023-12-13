INF = 2000000001


def solution():
    answer = INF
    n, m = map(int, input().split())
    ls = []
    for i in range(n):
        ls.append(int(input()))

    ls.sort()
    s = 0
    e = 0

    while e < n and s < n:
        if ls[e] - ls[s] == m:
            print(m)
            return

        if ls[e] - ls[s] < m:
            e += 1
        elif ls[e] - ls[s] > m:
            answer = min(answer, ls[e] - ls[s])
            s += 1

    print(answer)


solution()
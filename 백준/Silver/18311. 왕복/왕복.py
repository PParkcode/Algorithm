def solution():
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))

    ls.extend(reversed(ls))
    answer = 1
    if k == 0:
        print(answer)
        return

    data = [0]

    for i in range(len(ls)):
        data.append(data[i] + ls[i])

    if k >= ls[0]:
        for i in range(len(data) - 1):
            if data[i] <= k < data[i + 1]:
                answer = i + 1
                break
    else:
        answer = 1
    if answer > n:
        answer = (2 * n) + 1 - answer

    print(answer)


solution()

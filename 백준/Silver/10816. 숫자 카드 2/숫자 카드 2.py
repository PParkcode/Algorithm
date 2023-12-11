def solution():
    n = int(input())
    cards = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))

    sortedCards = sorted(cards)
    dic = {}

    for item in sortedCards:
        if item in dic.keys():
            dic[item] += 1
        else:
            dic[item] = 1

    for i in range(m):
        print(binary_search(targets[i], sortedCards, dic, 0, n - 1),end=" ")


def binary_search(target, cards, dic, s, e):
    mid = (s + e) // 2

    if s > e:
        return 0

    if cards[mid] == target:
        return dic[cards[mid]]
    if target < cards[mid]:
        return binary_search(target, cards, dic, s, mid - 1)
    if target > cards[mid]:
        return binary_search(target, cards, dic, mid + 1, e)


solution()
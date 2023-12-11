def solution():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    targets = list(map(int, input().split()))

    sortedA = sorted(a)

    for i in range(m):
        print(search(targets[i], sortedA, n, 0, n - 1))


def search(target, a, n, s, e):
    mid = (s + e) // 2
    if s > e or a[n - 1] < target or a[0] > target:
        return 0
    if a[mid] == target:
        return 1

    if target < a[mid]:
        return search(target, a, n, s, mid - 1)
    if target > a[mid]:
        return search(target, a, n, mid + 1, e)


solution()
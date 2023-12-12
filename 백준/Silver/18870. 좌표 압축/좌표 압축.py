def solution():
    n = int(input())
    ls = list(map(int, input().split()))
    arr = sorted(ls)

    distinctArr = [arr[0]]
    last = arr[0]
    for i in range(1, len(arr)):
        if arr[i] == last:
            continue
        distinctArr.append(arr[i])
        last = arr[i]

    for i in range(n):
        print(search(ls[i], 0, len(distinctArr) - 1, distinctArr), end=" ")


def search(target, s, e, distinctArr):
    mid = (s + e) // 2

    if target == distinctArr[mid]:
        return mid

    if target > distinctArr[mid]:
        return search(target, mid + 1, e, distinctArr)
    if target < distinctArr[mid]:
        return search(target, s, mid - 1, distinctArr)


solution()

def solution():
    n, m = map(int, input().split())
    dic = {}
    arr = [""] * (n + 1)
    for i in range(1, n + 1):
        pokemon = input()
        arr[i] = pokemon
        dic[pokemon] = i
    question = []
    for i in range(m):
        question.append(input())

    for item in question:
        if item.isdigit():
            print(arr[int(item)])
        else:
            print(dic[item])


solution()
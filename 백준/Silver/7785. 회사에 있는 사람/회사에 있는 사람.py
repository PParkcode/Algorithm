def solution():
    n = int(input())
    dic = {}
    answer = []
    for i in range(n):
        name, status = input().split()
        if status == "enter":
            dic[name] = True
        else:
            dic[name] = False

    for key, value in dic.items():
        if value:
            answer.append(key)
        else:
            continue

    answer.sort(reverse=True)
    for item in answer:
        print(item)


solution()
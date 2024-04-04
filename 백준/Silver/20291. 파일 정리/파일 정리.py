def solution():
    n = int(input())
    ls = []
    for i in range(n):
        ls.append(input())

    # 파이썬의 딕셔너리 이용
    dic = {}
    
    for item in ls:
        name, extension = item.split(".")
        # 키가 존재한다면 갯수 추가
        if extension in dic.keys():
            dic[extension] += 1
        # 키가 없다면 키와 value 생성
        else:
            dic[extension] = 1
    # 정렬한 키 목록
    sorted_keys = sorted(dic.keys())
    
    for key in sorted_keys:
        print(str(key) + " " + str(dic[key]))


solution()
def trans(num):
    return sum(map(int, list(str(num))))

arr = [0] * 10001
arr[0] = 1
i = 1
result = 0

for i in range(10000):
    result = i + trans(i)
    if result>10000:
        continue
    arr[result] = 1

for i in range(len(arr)):
    if arr[i] == 0:
        print(i)

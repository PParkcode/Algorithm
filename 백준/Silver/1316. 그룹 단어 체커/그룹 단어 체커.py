def check(word):
    s= set([])
    s.add(word[0])
    for i in range(1, len(word)):
        if word[i-1] == word[i]:
            continue

        if word[i] in s:
            return False
        s.add(word[i])

    return True


num = int(input())
ls=[]
answer =0

for i in range(num):
    ls.append(input())

for item in ls:
    if check(item):
        answer+=1

print(answer)
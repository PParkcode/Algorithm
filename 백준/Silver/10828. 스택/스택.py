import sys
num = int(input())
stack = []
for i in range(num):
    a = sys.stdin.readline().rstrip().split()
    if a[0] =="push":
        stack.append(int(a[1]))
    elif a[0] == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif a[0] == "size":
        print(len(stack))

    elif a[0] == "empty":
        if stack:
            print(0)
        else:
            print(1)
    elif a[0] == "top":
        if stack:
            print(stack[len(stack)-1])
        else:
            print(-1)


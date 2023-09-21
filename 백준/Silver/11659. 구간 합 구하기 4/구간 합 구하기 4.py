import sys


def solution():
    n, m = map(int, input().split())
    sumArr=[0]*(n+1)
    numList = list(map(int, sys.stdin.readline().split()))
    sum =0
    for i in range(n):
        sum +=numList[i]
        sumArr[i+1] = sum


    for i in range(m):
        a, b = map(int, sys.stdin.readline().split())
        print(sumArr[b] - sumArr[a-1])

solution()
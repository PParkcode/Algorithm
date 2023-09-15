import sys
import copy
from collections import deque

sys.setrecursionlimit(10 ** 9)

maxValue = -9999999999
minValue = 99999999999


def solution():
    n = int(input())
    numList = list(map(int, input().split()))
    # + - x / 순
    calList = list(map(int, input().split()))

    # 재귀를 이용해 풀어보자
    # 각 단계마다 한개씩 뽑아서 연산자를 나열하면 될 것 같다.

    recur(numList, calList, numList[0], 0)
    print(maxValue)
    print(minValue)

# 연산자 정보를 담은 배열의 값을 사용할 때마다 1씩 빼주면서 재귀 순회
def recur(numList, calList, currentValue, count):
    global maxValue
    global minValue
    temp = 0
    
    # 모든 연산을 다 사용했을 때 최대값 혹은 최소값을 갱신하고 return
    if count == len(numList) - 1:
        maxValue = max(currentValue, maxValue)
        minValue = min(currentValue, minValue)
        return

    for i in range(len(calList)):
        if calList[i] > 0:
            calList[i] -= 1
            if i == 0:
                temp = currentValue + numList[count + 1]
            elif i == 1:
                temp = currentValue - numList[count + 1]
            elif i == 2:
                temp = currentValue * numList[count + 1]
            elif i == 3:
                if currentValue < 0:
                    temp = currentValue * (-1)
                    temp = temp // numList[count + 1]
                    temp *= (-1)
                else:
                    temp = currentValue // numList[count + 1]
            # 다음 연산으로 재귀
            recur(numList, calList, temp, count + 1)
            # 사용했던 연산자 복원
            calList[i] += 1


solution()
import heapq
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    heap = []
    command = []
    for _ in range(n):
        command.append(int(input()))

    for temp in command:
        if temp < 0:
            heapq.heappush(heap, ((temp * -1), temp))
        elif temp > 0:
            heapq.heappush(heap, (temp, temp))

        else:
            if heap:
                item = heapq.heappop(heap)
                print(item[1])
            else:
                print(0)


solution()
from collections import deque
answer = 0

def solution():
    n = int(input())
    q = deque()
    visited = [False] * n
    visited2 = [False] * (2 * n - 1)
    visited3 = [False] * (2 * n - 1)
    recur(q, n, 0, visited, visited2, visited3)
    print(answer)


def recur(q, n, count, visited, visited2, visited3):
    global answer

    if count == n:
        answer += 1
        return

    for i in range(n):
        if visited[i] or visited2[count + i] or visited3[i - count + n - 1]:
            continue
        q.append((count, i))
        visited[i] = True
        visited2[count + i] = True
        visited3[i - count + n - 1] = True

        recur(q, n, count + 1, visited, visited2, visited3)

        visited[i] = False
        visited2[count + i] = False
        visited3[i - count + n - 1] = False
        q.pop()

solution()
from collections import deque
def solution():
    n, k = map(int, input().split())

    if n > k:
        print(n - k)
        return

    answer = bfs(n, k)

    print(answer)


# BFS를 통해 최단 거리를 구한다.
def bfs(n, k):
    # 방문 여부는 집합을 통해 관리한다.
    visited = set()

    q = deque()
    # 현재 위치와 이동 시간을 큐에 담는다.
    q.append((n, 0))
    visited.add(n)

    while q:

        num, count = q.popleft()
       
        # 찾았다면 리턴
        if num == k:
            return count

        visited.add(num)
        if num > 2*k:
            continue

        #  방문 여부를 확인하고 큐에 집어 넣는다.
        if (2 * num) not in visited and num < k:
            q.append((2 * num, count + 1))
            visited.add(2 * num)
        if (num + 1) not in visited:
            q.append((num + 1, count + 1))
            visited.add(num + 1)

        if (num - 1) not in visited:
            q.append((num - 1, count + 1))
            visited.add(num - 1)


solution()
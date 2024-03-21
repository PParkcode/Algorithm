import heapq

LIMIT = 250000

def solution():
    n, k = map(int, input().split())
    
    # 동생이 더 뒤에 있다면 할 필요 없음
    if k<n:
        print(n-k)
        return
    else:
        answer = search(n, k)
        print(answer)


def search(n, k):
    q = []
    visited = [True] * LIMIT
    heapq.heappush(q, (0, n))
    visited[n] = False

    # 가질 수 있는 최대값
    dif = k - n

    while q:
        depth, place = heapq.heappop(q)

        # 발견 했다면 depth 리턴
        if place == k:
            return depth

        # 최대값을 넘어서는 2배로 이동할 필요 없음
        if 2 * place - k <= dif and visited[2 * place]:
            heapq.heappush(q, (depth, 2 * place))
            visited[place * 2] = False

        # 최초 위치의 절반 이하로는 갈 필요 없음
        if n//2 <= place - 1  and visited[place - 1]:
            heapq.heappush(q, (depth + 1, place - 1))
            visited[place - 1] = False

        # 목표 지점을 넘겨서는 갈 필요 없음
        if place + 1 <= k and visited[place + 1]:
            heapq.heappush(q, (depth + 1, place + 1))
            visited[place + 1] = False

solution()

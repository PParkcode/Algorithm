import copy
INF = 987654321

def solution():
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    # N x 3 배열에서 각 자리에 자신이 가질 수 있는 최소 비용을 담을 table 변수 생성
    table = copy.deepcopy(graph)
    minValue = INF

    for i in range(1, n):
        for j in range(3):
            for k in range(3):
                # 인덱스가 같다면 무시
                if j == k:
                    continue
                # 윗 단계에서 가질 수 있는 값들 중 최소 값을 구한다.
                minValue = min(table[i - 1][k], minValue)
            # 해당 최소 값을 현재 table에 더하여 현재 자신이 가질 수 있는 최소값 갱신
            table[i][j] += minValue
            # 최소값 초기화 
            minValue = INF

    answer = min(table[n - 1])
    print(answer)


solution()
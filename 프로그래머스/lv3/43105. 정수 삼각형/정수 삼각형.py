def solution(triangle):
    answer = 0
    totalDepth = len(triangle)
    
    # 각 항목에는 해당 위치의 최대값을 저장한다.
    table = [[0]*i for i in range(1, totalDepth+1)]
    # 맨 위 꼭지점 초기화
    table[0][0] = triangle[0][0]
    
    # 각 항목을 순회하면서 자신의 왼쪽 아래값과 오른쪽 아래 값에 최대값을 갱신해준다.
    for i in range(totalDepth -1 ):
        for j in range(len(triangle[i])):
            table[i+1][j] = max(table[i+1][j],table[i][j]+triangle[i+1][j])
            table[i+1][j+1] = max(table[i+1][j+1],table[i][j] + triangle[i+1][j+1])
    # 가장 아래 depth의 최대값을 출력한다.
    answer = max(table[totalDepth - 1])
    return answer
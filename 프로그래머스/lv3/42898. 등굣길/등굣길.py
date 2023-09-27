def solution(m, n, puddles):
    answer = 0
    
    # 보드 생성
    board = [[-1]*(m) for _ in  range(n)]
    
    # 시작점 (0,1), (1,0)은 1로 설정 - 코드 내 시작 좌표는 (0,0)
    board[0][0] = 1 
    
    # 물 웅덩이가 있는 곳은 0의 값으로 설정
    # 물 웅덩이가 없을 경우 빈 배열이 옴 -> 여기서 인덱스 에러 발생 가능
    for item in puddles:
        if item:
            board[item[1]-1][item[0]-1] = 0
    
    
    # board[0][i] 과 board[i][0]를 초기화
    if m>1:
        for i in range(1,m):
            if board[0][i] ==0:
                continue
            board[0][i] = board[0][i-1]
            
    if n>1:
        for i in range(1,n):
            if board[i][0] == 0:
                continue
            board[i][0] = board[i-1][0]
    
    if m == 1 or n == 1:
        return board[n-1][m-1]
        
    
    # 이제 m,n 둘다 적어도 2 이상
    # i,j = 자신의 왼쪽 값과 위쪽 값을 더한 값
    # i,j가 0 즉 웅덩이라면 무시
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == 0:
                continue
            board[i][j] = board[i-1][j] + board[i][j-1]
            
    
    
    answer = board[n-1][m-1] % 1000000007
    return answer
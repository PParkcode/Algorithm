def solution():
    n = int(input())
    k = int(input())
    movingList= []
    """
    사과는 3
    벽은 9
    몸통은 1
    빈 공간은 0
    """

    # 경계면까지 포함해 생성
    board = [[0] * (n + 2) for _ in range(n + 2)]

    # 경계면은 9로 설정
    for i in range(n + 2):
        board[0][i] = 9
        board[n + 1][i] = 9
        board[i][0] = 9
        board[i][n + 1] = 9

    # 사과는 3으로 설정
    for _ in range(k):
        (a,b) = map(int, input().split())
        board[a][b] = 3

    l = int(input())

    for _ in range(l):
        (a,b) = input().split()
        movingList.append((int(a),b))

    board[1][1] = 1
    print(game(board,movingList))

def game(board,movingList):
    # 초기 진행 방향
    directionX = 1
    directionY = 0
    x = 1
    y = 1
    taleX = 1
    taleY = 1

    count = 0
    #몸통의 INDEX를 담을 리스트
    body = [(1,1)]
    (time,dir) = movingList.pop(0)

    while(True):

        # 현재 진행 방향이 상하좌우일 때마다 좌우로 방향을 바꾸면
        # 다음 진행 방향이 규칙성 있게 변함
        if time == count:
            # 좌회전
            if dir == "L":
                # 현재 좌우 이동 시
                if directionY == 0:
                    directionY = -directionX
                    directionX = 0
                # 현재 상하 이동 시
                else:
                    directionX = directionY
                    directionY = 0
            #우회전
            else:
                # 현재 좌우 이동 시
                if directionY == 0:
                    directionY = directionX
                    directionX = 0
                # 현재 상하 이동 시
                else:
                    directionX = -directionY
                    directionY = 0
            if movingList:
                (time,dir) = movingList.pop(0)

        count+=1

        nx = x + directionX
        ny = y + directionY
        # 빈공간
        if board[ny][nx] == 0:
            board[ny][nx] = 1
            body.append((ny,nx))
            (taleY,taleX) = body.pop(0)
            board[taleY][taleX] = 0
            y = ny
            x = nx
        # 사과
        elif board[ny][nx] == 3:
            board[ny][nx] = 1
            body.append((ny, nx))
            y = ny
            x = nx
        # 벽 혹은 몸통
        elif board[ny][nx] == 1 or board[ny][nx] == 9:
            break

    return count



solution()
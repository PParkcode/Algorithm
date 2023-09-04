import copy

def solution(key, lock):
    answer = False
    n= len(lock)
    m = len(key)
    bigN= 3*n 
    bigLock = [[0]*(bigN) for _ in range(bigN)]
    
    # 확장한 자물쇠 생성
    for i in range(n):
        for j in range(n):
            bigLock[i+n][j+n] = lock[i][j]
    
    #하나씩 회전
    for _ in range(4):
        key = rotate(key,bigLock,m)
        if moving(key,bigLock,m,n):
            return True
    
    
    return answer


# 90도 회전
def rotate(key,newLock,m):
    newKey = [[0]*m for i in range(m)]
    
    for i in range(m):
        for j in range(m):
            newKey[i][j] = key[m-j-1][i]
    
    return newKey
            

# 하나씩 옮겨가면서 비교하기
def moving(key, bigLock,keySize,lockSize):
    diff = lockSize - keySize +1
    for i in range(diff,2*lockSize):
        for j in range(diff,2*lockSize):
            if add(key,bigLock,i,j):
                return True
    return False
            

# 이동하는 index를 가져와 이용해서 자물쇠와 열쇠 값을 더함
def add(key,bigLock,a,b):
    # 2차원 배열은 DeepCopy를 해야 함
    # 그렇지 않으면 내부 객체의 주소가 copy됨
    tempLock = copy.deepcopy(bigLock)
    
    for i in range(len(key)):
        for j in range(len(key)):
            tempLock[a+i][b+j] = bigLock[a+i][b+j] + key[i][j]
    
    
    return check(tempLock)

    
# 중앙 자물쇠 값에 1이 아닌 값이 있는지 확인
def check(bigLock):
    center = len(bigLock)//3
    for i in range(center,center+center):
        for j in range(center,center+ center):
            
            if bigLock[i][j] !=1:
                return False
    return True
            

    
        
            
                
    
        
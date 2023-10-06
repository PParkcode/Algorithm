import sys
sys.setrecursionlimit(10 ** 9)

def solution():
    n, m = map(int, input().split())

    ls = []
    answer = []
    for i in range(1, n + 1):
        ls.append(i)

    for i in range(n - m + 1):
        # 재귀 사용
        dfs(ls[i], 1, m, ls, answer, [ls[i]])

    for item in answer:
        for i in range(m):
            print(item[i], end=" ")
        print()


def dfs(idx, count, m, ls, answer, tempAnswer):
    
    if count == m:
        # list(tempAnswer)로 하여 넣어야 함
        # 그렇지 그냥 tempAnswer을 넣으면 리스트 안의 주소가 같아 answer에도 영향이 간다.
        answer.append(list(tempAnswer))
        return
    
    # 조합 하나를 tempAnswer에 담고, m개 만큼 찬다면 이걸 answer에 넣는다.
    for i in range(idx, len(ls)):
        tempAnswer.append(ls[i])
        dfs(ls[i], count + 1, m, ls, answer, tempAnswer)
        tempAnswer.pop()


solution()
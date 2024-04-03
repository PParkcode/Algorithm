"""
아이디어
첫번째 부터 마지막 요소까지 for문 진행
1. 다음 블록이 더 낮은 블록이면 진행
2. 만약 현재까지의 가장 높은 블록(a)보다 현재 블록(b)이 더 높다면
a부터 b 사이에 고인 물 계산/ 이제 b 블록 이전은 신경 쓰지 않아도 된다.

3. 만약 이전의 블록(pre)보다 현재 블록(current)이 더 크면
현재까지의 최대 블록 위치와 current 사이의 고인 물 계산


"""


def solution():
    h, w = map(int, input().split())

    ls = list(map(int, input().split()))

    results = simulate(ls, w)
   
    print(sum(results))


def simulate(ls, w):
    # 최대 블록의 위치와 높이
    current_max = (0, ls[0])

    # 바로 이전 블록의 높이
    previous = ls[0]

    # 각 블록 좌표마다 고인 물의 높이를 저장하는 리스트
    results = [0] * w

    # 2번째 블록부터 for문 시작
    for i in range(1, w):
        # 현재까지의 최대 높이보다 현재 높이가 더 높을 경우 빗물 계산하고 최대 높이 갱신
        if ls[i] >= current_max[1]:
            calculate(ls, results, current_max[0], i, current_max[1])
            current_max = (i, ls[i])

        # 바로 이전의 블록 높이보다 현재 블록의 높이가 높을 경우
        # 현재까지의 최대 블록위치에서 현재 블록 높이까지의 빗물 높이 계산
        elif ls[i] > previous:
            calculate(ls, results, current_max[0], i, ls[i])

        previous = ls[i]
    return results


def calculate(ls, results, start, end, limit):
    for i in range(start + 1, end):
        temp = limit - ls[i]
        results[i] = max(temp,results[i])


solution()
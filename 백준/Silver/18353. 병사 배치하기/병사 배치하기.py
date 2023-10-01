def solution():
    n = int(input())
    soldiers = list(map(int, input().split()))
    soldiers.append(0)
    table = [0] * (n + 1)

    # 거꾸로 접근해서 풀 수 있을 것 같음
    # 먼저 내 뒤에 나보다 작은값을 확인하고, 작은 값들 중 가장 큰 값 + 1 하면 현재 내 값이 된다.

    for i in range(n - 1, -1, -1):
        # 현재 자신의 값 갱신
        myVal = check(soldiers, i, table, n)
        table[i] = myVal

    print(n - max(table))


def check(soldiers, idx, table, n):
    maxNum = -1
    # 현재 인덱스부터 soldiers의 리스트 끝까지 순회
    # 뒤에 값에 작은게 있다면 maxNum과 비교해 최대값을 갱신
    for i in range(idx, n + 1):
        if soldiers[idx] > soldiers[i]:
            if maxNum < table[i]:
                maxNum = table[i]

    # 최대값 + 1(자기 자신 포함)을 리턴
    return maxNum + 1


solution()
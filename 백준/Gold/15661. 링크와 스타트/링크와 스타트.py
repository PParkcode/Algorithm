import itertools

INF = 987654321
answer = INF


def solution():
    n = int(input())
    graph = []
    members = []
    for i in range(n):
        graph.append(list(map(int, input().split())))

    half = n // 2

    for i in range(0, n):
        members.append(i)

    simulate(graph, members, half)
    print(answer)


def simulate(graph, members, half):
    global answer
    # 전부 할 필요 없이 전체 길이에 대해 절반 진행 해도 된다.
    for i in range(2, half + 1):
        # 조합
        ls = itertools.combinations(members, i)
        for team in ls:
            team1 = calculate(graph, team)
            # team1에 속하지 사람들로 이루어진 team2
            team2 = calculate(graph, [x for x in members if x not in team])
            answer = min(abs(team1 - team2), answer)


# 팀 능력치 합 계싼
def calculate(graph, team):
    result = 0
    for member1 in team:
        for member2 in team:
            result += graph[member1][member2]
    return result


solution()
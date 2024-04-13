from collections import deque


def solution():
    answer = []
    while True:
        # 트리 정보를 입력할 딕셔너리
        dic = {}
        n, k = map(int, input().split())
        if (n, k) == (0, 0):
            break
        ls = list(map(int, input().split()))
        for item in ls:
            dic[item] = []
        q = deque(ls)
        answer.append(case(n, k, q, dic))

    for item in answer:
        print(item)


def case(n, k, q, dic):
    # 부모 후보를 차례대로 큐에 담음
    parents = deque()
    root = q.popleft()
    pre = root
    parents.append(root)
    parent = root
    # 키는 자식, 벨류는 부모
    parent_dictionary = {}
    parent_dictionary[root] = -1

    while q:
        # 입력 값을 하나씩 뽑는다.
        # 해당 값을 부모 후보에 넣는다.
        node = q.popleft()
        parents.append(node)

        # 이전 값과 차이가 1이 아니라면
        # 부모 후보 큐에서 값 하나를 꺼내 해당 노드를 부모의 자식으로 설정
        if node - pre != 1:
            parent = parents.popleft()
            dic[parent].append(node)
        # 이전값과 차이가 1이라면 기존의 부모의 자식으로 설정
        else:
            dic[parent].append(node)
        # 이전 값 갱신
        # 부모 딕셔너리 업데이트
        pre = node
        parent_dictionary[node] = parent

    return find_cousin(dic, k, parent_dictionary, root)


def find_cousin(dic, target, parent_dictionary, root):
    if target == root:
        return 0
    # 타겟의 부모와 조부모 노드를 구한다.
    parent = parent_dictionary[target]
    grand_parent = parent_dictionary[parent]
    answer = 0
    # 이 경우는 조부모 노드가 없는 경우이다.
    if parent == -1 or grand_parent == -1:
        return 0

    # 조부모 노드의 자식들을 순회하며, 사촌의 수를 구한다.
    for item in dic[grand_parent]:
        if item == parent:
            continue

        answer += len(dic[item])
    return answer


solution()

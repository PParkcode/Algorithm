def solution():
    n = int(input())
    graph = {}
    for i in range(n):
        temp = input().split()
        graph[temp[0]] = []
        graph[temp[0]].append(temp[1])
        graph[temp[0]].append(temp[2])

    preOrder(graph, 'A')
    print()
    inOrder(graph, 'A')
    print()
    postOrder(graph, 'A')


def preOrder(graph, node):
    if node == '.':
        return
    print(node, end='')
    preOrder(graph, graph[node][0])
    preOrder(graph, graph[node][1])


def inOrder(graph, node):
    if node == '.':
        return
    inOrder(graph, graph[node][0])
    print(node, end='')
    inOrder(graph, graph[node][1])


def postOrder(graph, node):
    if node == '.':
        return
    postOrder(graph, graph[node][0])
    postOrder(graph, graph[node][1])
    print(node, end='')


solution()
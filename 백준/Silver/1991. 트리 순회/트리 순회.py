def solution():
    n = int(input())
    dic = {}
    for i in range(n):
        node, left, right = input().split()
        dic[node] = (left, right)

    preorder(dic, "A")
    print()
    inorder(dic, "A")
    print()
    postorder(dic, "A")


def preorder(dic, root):
    if root == ".":
        return
    print(root, end="")
    preorder(dic, dic[root][0])
    preorder(dic, dic[root][1])


def inorder(dic, root):
    if root == ".":
        return
    inorder(dic, dic[root][0])
    print(root, end="")
    inorder(dic, dic[root][1])


def postorder(dic, root):
    if root == ".":
        return
    postorder(dic, dic[root][0])
    postorder(dic, dic[root][1])
    print(root, end="")


solution()

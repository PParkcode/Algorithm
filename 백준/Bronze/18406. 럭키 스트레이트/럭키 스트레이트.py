def luckyStraight():
    num = input()

    size = len(num)
    left = 0
    right = 0
    for i in range(size):
        if i<size/2:
            left +=int(num[i])
        else:
            right += int(num[i])

    if left == right:
        print("LUCKY")
    else:
        print("READY")


luckyStraight()
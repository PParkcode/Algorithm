import heapq

def solution():
    n = int(input())
    cards = []
    answer = 0
    for _ in range(n):
        cards.append(int(input()))

    heapq.heapify(cards)
    for _ in range(n-1):
        card1 = heapq.heappop(cards)
        card2 = heapq.heappop(cards)
        result = card1 + card2
        answer+=result
        heapq.heappush(cards,result)

    print(answer)


solution()
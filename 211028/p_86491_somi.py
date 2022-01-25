

def solution(sizes):
    n = len(sizes)
    max_x, max_y = 0, 0
    for size in sizes:
        if size[0] > size[1]:
            size[1], size[0] = size[0], size[1]
    x = max(sizes[c][0] for c in range(n))
    y = max(sizes[c][1] for c in range(n))

    return x * y

'''
def solution(sizes):
    n = len(sizes)
    s = 1000000
    for i in range(1 << n):
        cards = [card for card in sizes]
        for j in range(n):
            if i & 1 << j:
                cards[j][0], cards[j][1] = cards[j][1], cards[j][0]
            x = max(cards[k][0] for k in range(n))
            y = max(cards[c][1] for c in range(n))
            if x * y < s:
                s = x * y
    return s
'''

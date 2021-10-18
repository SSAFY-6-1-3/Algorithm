import sys

sys.stdin = open('s_1251.txt')

def all():
    lines = []

    for i in range(N-1):
        for j in range(i+1, N):
            a = (pX[i], pY[i])
            b = (pX[j], pY[j])
            dist = (a[0]-b[0])**2 + (a[1]-b[1])**2
            lines.append((i, j, dist*tax))
    return sorted(lines, key= lambda x: x[2])

def kr(lines, N):
    idx = 0
    cost = 0
    for _ in range(N-1):
        while True:
            a, b, w = lines[idx]
            idx +=1
            if find_set(a) != find_set(b):
                break
        cost += w
        union(a, b)

    return round(cost)

def find_set(x):
    if p[x] == x: return x
    return find_set(p[x])

def union(x, y):
    p[find_set(y)] = find_set(x)

T= int(input())
for tc in range(1, T+1):
    N = int(input())
    pX = list(map(int, input().split()))
    pY = list(map(int, input().split()))
    tax = float(input())

    p = list(range(N))
    lines = all()
    print('#{} {}'.format(tc, kr(lines, N)))
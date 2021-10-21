import sys
sys.stdin = open('s_1251.txt')

def prim():
    key = [inf] * N
    visited = [0] * N
    key[0] = 0
    ans = 0

    for _ in range(N):
        min_idx = -1
        min_val = inf
        for i in range(N):
            if not visited[i] and key[i] < min_val:
                min_idx = i
                min_val = key[i]

        visited[min_idx] = 1
        ans += min_val


        for j in range(N):
            if not visited[j] and ((X[min_idx] - X[j]) ** 2) + ((Y[j] - Y[min_idx]) ** 2) < key[j]:
                key[j] = ((X[min_idx] - X[j]) ** 2) + ((Y[j] - Y[min_idx]) ** 2)
    return round(E * ans)



T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    inf = float('inf')

    print('#{} {}'.format(tc, prim()))
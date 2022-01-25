import sys
sys.stdin=open('input.txt')
# 프림 알고리즘
def prim(s):
    inf = float('inf')
    key = [inf] * N
    visited = [0] * N
    key[s] = 0

    for _ in range(N-1):
        minidx = -1
        minv = inf
        for i in range(N):
            if not visited[i] and key[i] < minv:
                minv = key[i]
                minidx = i

        visited[minidx] = 1

        for j in range(N):
            if island[minidx][j]:
                if not visited[j] and island[minidx][j] < key[j]:
                    key[j] = island[minidx][j]

    return sum(key)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    island = [[0] * N for _ in range(N)]                            # 섬 = 인덱스
    for i in range(N):
        for j in range(N):
            if not island[i][j]:
                result = ((X[i] - X[j])**2 + (Y[i] - Y[j])**2)     # 섬들 사이의 거리 저장
                island[i][j] = result
                island[j][i] = result

    print('#{} {}'.format(tc, round(prim(0)*E)))
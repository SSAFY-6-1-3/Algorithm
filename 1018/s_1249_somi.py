import sys
sys.stdin = open('s_1249.txt')

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def solution():
    cost = [[inf] * N for _ in range(N)]
    cost[0][0] = area[0][0]
    next = [(0, 0)]


    while next:
        r, c = next.pop(0)

        for di in range(4):
            nr, nc = r + dr[di], c + dc[di]
            if 0 <= nr < N and 0 <= nc < N and cost[nr][nc] > (cost[r][c] + area[nr][nc]):
                cost[nr][nc] = cost[r][c] + area[nr][nc]
                next.append((nr, nc))
    return cost[N-1][N-1]




T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    area = [list(map(int, input())) for _ in range(N)]
    inf = 987654321
    ans = solution()
    print('#{} {}'.format(tc, ans))



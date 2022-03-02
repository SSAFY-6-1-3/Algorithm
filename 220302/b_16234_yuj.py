from sys import stdin
from collections import deque
input = stdin.readline

def bfs(si, sj, cnt):
    people = cities[si][sj]                # 현재 인구 더하기
    deq = deque([[si, sj]])
    temp = [[si, sj]]                      # 인구 변경할 때 이용하기 위해서 따로 저장
    visited[si][sj] = cnt
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    while deq:
        i, j = deq.popleft()
        for k in range(4):
            ni, nj = i+di[k], j+dj[k]
            if ni in range(N) and nj in range(N) and not visited[ni][nj]:
                minus = abs(cities[ni][nj] - cities[i][j])
                if L <= minus <= R:
                    people += cities[ni][nj]
                    visited[ni][nj] = cnt
                    deq.append([ni, nj])
                    temp.append([ni, nj])

    return [people, temp]

N, L, R = map(int, input().split())
cities = [list(map(int, input().split())) for _ in range(N)]
day = -1
cnt = 1
while cnt != (N*N)+1:                       # 모든 나라가 연합이 아닐 경우 cnt == 전체 국가의 수
    day += 1
    cnt = 1
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                result = bfs(r, c, cnt)
                new = result[0] // len(result[1])
                for x, y in result[1]:      # 연합 국가 인구 변경하기
                    cities[x][y] = new
                cnt += 1

print(day)
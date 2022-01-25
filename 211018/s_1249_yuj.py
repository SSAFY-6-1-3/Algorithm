import sys
sys.stdin=open('input.txt')
from collections import deque

def move(i, j, road):
    global visited

    di = [0, +1, -1, 0]
    dj = [+1, 0, 0, -1]

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]

        if 0 <= ni < N and 0 <= nj < N:                     # 다음 이동 위치가 범위 안에 있다면
            if road + war[ni][nj] < visited[ni][nj]:        # 저장될 값이 현재값보다 더 작을 때 저장
                queue.append([ni, nj])
                visited[ni][nj] = road + war[ni][nj]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    war = [list(map(int, input())) for _ in range(N)]
    visited = [[987654321] * N for _ in range(N)]           # visited에 비용 최소 시간 누적

    visited[0][0] = 0                                       # 좌상단의 칸(출발지) 부터 시작
    queue = deque([[0, 0]])

    while queue:                                            # BFS
        i, j = queue.popleft()
        move(i, j, visited[i][j])

    print('#{} {}'.format(tc, visited[-1][-1]))
from collections import deque

def bfs(deq):
    global zero

    while deq:
        i, j = deq.popleft()

        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni in range(N) and nj in range(M) and tomato[ni][nj] == 0:
                deq.append((ni, nj))
                tomato[ni][nj] = tomato[i][j] + 1
                zero -= 1                   # 익었으니까 안 익은 토마토 갯수 빼주기


M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
deq = deque([])
zero = 0                                    # 아직 안 익은 토마토 갯수
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:               # 익은 토마토 위치 저장
            deq.append((i, j))
        elif not tomato[i][j]:
            zero += 1

if not zero:                                # 모든 토마토가 익었으면 0 출력
    print(0)
else:
    bfs(deq)
    if zero:                                # 안 익은 토마토가 남아있으면 -1 출력
        print(-1)
    else:
        print(max(map(max, tomato))-1)      # 최대 일수 출력 (1부터 시작해서 1빼기)
from collections import deque
import sys

sys.stdin = open('s_2383.txt')

Dy = (1, 0, -1, 0)
Dx = (0, 1, 0, -1)

def bfs(stair,  people):
    rtn = []
    visited = [[101 for _ in range(N)] for _ in range(N)]
    sy, sx = stair
    visited[sy][sx] = 0
    q = deque([(sy, sx)])
    cnt = 0
    while q and cnt < len(people):
        y, x = q.popleft()
        dist = visited[y][x]

        for d in range(4):
            ny, nx = y+Dy[d], x+Dx[d]
            if ny not in range(N) or nx not in range(N) : continue

            if visited[ny][nx] > dist+1 :
                if mat[ny][nx] == 1:            # q에 사람 넣기
                    idx = people.index([ny, nx])
                    rtn.append([idx, dist + 1])
                    cnt += 1

                visited[ny][nx] = dist+1
                q.append((ny, nx))
    return rtn

def check(mat, N):
    people = [] # [y, x] =bfs=> [계단, 계단거리]
    stairs = []
    for y in range(N):
        for x in range(N):
            if mat[y][x] ==1:
                people.append([y, x])
            elif mat[y][x] > 1:
                stairs.append((y, x, mat[y][x]))

    stair_a = bfs(stairs[0][:2], people)
    stair_b = bfs(stairs[1][:2], people)
    stair_a.sort(key= lambda x : x[1])
    stair_b.sort(key= lambda x : x[1])

    # return stair_a, stair_b
    return run(stair_a, stair_b, people, stairs[0][2], stairs[1][2])

def run(st_a, st_b, pp, cnt_a, cnt_b):
    sec = 0
    q_a, q_b = deque(st_a), deque(st_b)
    now_a = deque()
    now_b = deque()
    escaped = []
    while now_a or now_b or q_a or q_b:
        sec +=1
        for i in range(len(now_a)):     # 계단에 있는 애들 시간 -1
            now_a[i] -= 1

        for i in range(len(now_b)):
            now_b[i] -= 1

        while now_a and not now_a[0]:
            now_a.popleft()
        while now_b and not now_b[0]:
            now_b.popleft()


        break_a, break_b = False, False
        while not (break_a and break_b):
            if q_a and q_b and q_a[0][1]+cnt_a < q_b[0][1]+cnt_b:
                while q_a and q_a[0][0] in escaped:
                    q_a.popleft()
                if len(now_a) < 3 and not break_a:
                    if q_a and q_a[0][1] < sec:
                        person = q_a.popleft()
                        now_a.append(cnt_a)
                        escaped.append(person[0])
                    else:
                        break_a = True
                        break

                while q_b and q_b[0][0] in escaped:
                    q_b.popleft()
                if len(now_b) < 3 and not break_b:
                    if q_b and q_b[0][1] < sec:
                        person = q_b.popleft()
                        now_b.append(cnt_b)
                        escaped.append(person[0])
                    else:
                        break_b = True
                        break
            else :
                while q_b and q_b[0][0] in escaped:
                    q_b.popleft()
                while len(now_b) < 3 and not break_b:
                    if q_b and q_b[0][1] < sec:
                        person = q_b.popleft()
                        now_b.append(cnt_b)
                        escaped.append(person[0])
                    else:
                        break_b = True
                        break
                while q_a and q_a[0][0] in escaped:
                    q_a.popleft()
                while len(now_a) < 3 and not break_a:
                    if q_a and q_a[0][1] < sec:
                        person = q_a.popleft()
                        now_a.append(cnt_a)
                        escaped.append(person[0])
                    else:
                        break_a =True
                        break

    return sec



T  = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print(tc, check(mat, N))
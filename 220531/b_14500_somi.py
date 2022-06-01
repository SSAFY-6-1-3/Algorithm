small_i = [(0, 0), (1, 0)]
small_m = [(0, 0), (0, 1)]
M = small_m + [(0, 2)]
I = small_i + [(2, 0)]

tetrominos = [
    M + [(0, 3)],  # 1
    I + [(3, 0)],
    small_i + [(0, 1), (1, 1)],  # 2
    I + [(2, 1)],  # 3
    M + [(1, 0)],
    I + [(0, -1)],
    M + [(-1, 2)],
    I + [(2, -1)],
    M + [(-1, 0)],
    I + [(0, 1)],
    M + [(1, 2)],
    small_i + [(1, 1), (2, 1)],  # 4
    small_m + [(-1, 1), (-1, 2)],
    small_i + [(0, 1), (-1, 1)],
    small_m + [(1, 1), (1, 2)],
    M + [(1, 1)],  # 5
    I + [(1, -1)],
    M + [(-1, 1)],
    I + [(1, 1)],
]

def cal_sum(r, c):
    global ans
    for tetromino in tetrominos:
        tmp = 0
        flag = True
        for poliomino in tetromino:
            nr = r + poliomino[0]
            nc = c + poliomino[1]
            if 0 <= nr < N and 0 <= nc < M:
                tmp += paper[nr][nc]
            else:
                flag = False
                break
        if not flag:
            continue
        else:
            ans = max(ans, tmp)


N, M = map(int, input().split())
paper = list(list(map(int, input().split())) for _ in range(N))
ans = 0
for r in range(N):
    for c in range(M):
       cal_sum(r, c)

print(ans)

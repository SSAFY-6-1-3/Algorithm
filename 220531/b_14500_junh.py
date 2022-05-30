import sys
input = sys.stdin.readline

def turn(org):
    tet = org
    for _ in range(4):  # 네 방향으로
        tmp = []
        for i in range(4):  # 네 점들을 오른쪽으로 90도 돌림
            p = tet[i]
            np = [-p[1], p[0]]
            tmp.append(np)
        if tmp not in tetrominoes:
            tetrominoes.append(tmp)
            tet = tmp
    return tmp

originals = [
    [[0, 0], [0, 1], [1, 0], [1, 1]],   #네모
    [[0, 0], [0, 1], [0, 2], [0, 3]],   #작대기
    [[0, 0], [1, 0], [2, 0], [2, 1]],   # ㄴ
    [[0, 0], [1, 0], [2, 0], [2, -1]],  # 역ㄴ
    [[0, 0], [1, 0], [1, 1], [2, 1]],   # 번개
    [[0, 0], [1, 0], [1, -1], [2, -1]], # 역번개
    [[0, 0], [0, -1], [0, 1], [1, 0]]   # ㅗ
]
tetrominoes = originals[:]

for o in originals:
    turn(o)

def get_sco(y, x, tet):
    sco = 0
    for p in tet:
        ny, nx = y+p[0], x+p[1]
        if ny not in range(N) or nx not in range(M): return 0
        sco += mat[ny][nx]

    return sco



N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]
max_sco = 0
for i in range(N):
    for j in range(M):

        for tet in tetrominoes:
            max_sco = max(max_sco, get_sco(i, j, tet))

print(max_sco)





# print(originals[2])
# print(turn90(originals[2]))
# print(turn90(turn90(originals[2])))
# print(turn90(turn90(turn90(originals[2]))))
# print(turn90(turn90(turn90(turn90(originals[2])))))



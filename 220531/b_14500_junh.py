

# N, M = map(int, input().split())

originals = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],   #작대기
    [[0, 0], [0, 1], [1, 0], [1, 1]],   #네모
    [[0, 0], [1, 0], [2, 0], [2, 1]],   # ㄴ
    [[0, 0], [1, 0], [1, 1], [2, 1]],   # 번개
    [[0, 0], [0, -1], [0, 1], [1, 0]]   # ㅗ
]
tetrominoes = []

# 01 -10
# 10 01
# 0-1 10

def turn90(org):
    for _ in range(4):  # 네 방향으로
        tmp = []
        for i in range(4):  # 네 점들을 오른쪽으로 90도 돌림
            p = org[i]
            if p[0] < 0 and p[1] > 0 :
                np = [-p[1] , p[0]]
            elif p[0] < 0 and p[1] < 0:
                np = [p[1], -p[0]]
            elif p[0] > 0 and p[1] < 0:
                np = [-p[1], p[0]]
            else:
                np = [-p[1], p[0]]
            tmp.append(np)
        if tmp not in tetrominoes:
            tetrominoes.append(tmp)
    return tmp


print(turn90(turn90(originals[3])))




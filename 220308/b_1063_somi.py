direction = {
    "R": (0, -1),
    "L": (0, 1),
    "B": (-1, 0),
    "T": (1, 0),
    "RT": (1, -1),
    "LT": (1, 1),
    "RB": (-1, -1),
    "LB": (-1, 1)
}  # 180도 회전된 모습을 기준으로 이동

K, S, N = input().split()

kr = int(K[1])
kc = 9 - (ord(K[0]) - 64)  # A ~ H : 8 ~ 1

sr = int(S[1])
sc = 9 - (ord(S[0]) - 64)

for _ in range(int(N)):
    m = direction[input()]
    nr = m[0] + kr
    nc = m[1] + kc
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        if sr == nr and sc == nc:
            if 1 <= sr + m[0] <= 8 and 1 <= sc + m[1] <= 8:
                kr, kc = nr, nc
                sr += m[0]
                sc += m[1]
            else: continue
        else:
            kr, kc = nr, nc

king = chr(9 - kc + 64) + str(kr)
stone = chr(9 - sc + 64) + str(sr)

print(king)
print(stone)
import sys

input = sys.stdin.readline

dY = [1, 0, -1, 0]
dX = [0, 1, 0, -1]


def check(y, x, dir):
    global answer
    color = mat[y][x]
    candies = 1
    chance = True

    while True:
        y, x = y+dY[dir], x+dX[dir]
        if y not in range(N) or x not in range(N):
            return candies
        elif mat[y][x] != color:
            if chance:
                for oth in range(4):
                    ty, tx = y+dY[oth], x+dX[oth]
                    if oth == dir :
                        if ty in range(N) and tx in range(N) and mat[ty][tx] == color:
                            answer = max(answer, candies+1)
                            continue
                    elif (oth%2) == (dir%2) : continue
                    if ty in range(N) and tx in range(N) and mat[ty][tx] == color:
                        chance = False
                        break
                else: return candies
            else : return candies
        candies += 1




N = int(input())
mat = [list(input()) for _ in range(N)]

answer = 0
for i in range(N):
    for j in range(N):
        for d in range(4):
            # answer = max(answer, check(i, j, d)) 이렇게 하면 함수 25번 째 줄에서 answer를 바꿔도 이전에 저장된 answer와 check의 리턴값만 비교해서 answer가 더 작아질 수 있다.
            # 4
            # CPCP
            # YZYZ
            # CCPC
            # ZYZY
            answer = max(check(i, j, d), answer)

print(answer)
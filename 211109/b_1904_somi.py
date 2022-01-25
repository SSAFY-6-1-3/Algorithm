import sys
input= sys.stdin.readline
N = int(input())


tiles = [0] * (N + 2)

tiles[1] = 1
tiles[2] = 2
for i in range(3, N + 1):
    tiles[i] = (tiles[i - 1] + tiles[i - 2]) % 15746

# 마지막에 15746 나누면 메모리 초과!!!
print(tiles[N])


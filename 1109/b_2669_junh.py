

mat = [[0 for _ in range(101)] for _ in range(101)]
squares = [list(map(int, input().split())) for _ in range(4)]

for sq in squares:
    for y in range(sq[1], sq[3]):
        for x in range(sq[0], sq[2]):
            if not mat[y][x]:
                mat[y][x] = 1

ans = sum(map(sum, mat))
print(ans)
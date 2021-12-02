N = int(input())
stars = [[' ' for _ in range(N)] for _ in range(N)]

def draw_star(n, r, c):
    if n == 1:
        stars[r][c] = '*'
        #print(r, c)

    else:
        small_n = n // 3
        for dc in range(3):
            for dr in range(3):
                if not(dc == 1 and dr == 1):
                    draw_star(small_n, r + dr * small_n, c + dc * small_n)

draw_star(N, 0, 0)
#print(stars)
for i in stars:
    print(''.join(i))

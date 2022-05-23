def check(sr, sc, size):
    is_same = True
    now = papers[sr][sc]
    for r in range(sr, sr + size):
        for c in range(sc, sc + size):
            if papers[r][c] != now:
                is_same = False
                break
        if not is_same:
            break

    if is_same:
        num[now] += 1
    else:
        size //= 3
        for i in range(3):
            for j in range(3):
                check(sr + (i * size), sc + (j * size), size)


N = int(input())
papers = list(list(map(int, input().split())) for _ in range(N))

num = [0, 0, 0]
check(0, 0, N)
print(num[-1])
print(num[0])
print(num[1])


def find(N, x, y):
    global cnt

    if N == 1:
        cnt += 1
        if x == r and y == c:
            print(cnt)
            exit(0)
        return

    if r not in range(x, x + N) or c not in range(y, y + N):           # 가지치기 안 해주면 시간 초과
        cnt += N**2
        return

    find(N // 2, x, y)
    find(N // 2, x, y + N // 2)
    find(N // 2, x + N//2, y)
    find(N // 2, x + N//2, y + N//2)


N, r, c = map(int, input().split())
cnt = -1
find(2**N, 0, 0)
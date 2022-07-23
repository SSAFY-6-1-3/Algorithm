T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    cnt = 0
    x %= M
    y %= N                              # N == y이면 나머지를 0으로 두기 위해서
    while True:
        num = M * cnt + x               # 최소 공배수 구하기
        if num:                         # num = 0일 경우 제외
            if num > M * N:
                print(-1)
                break

            if num % N == y:
                print(num)
                break
        cnt += 1
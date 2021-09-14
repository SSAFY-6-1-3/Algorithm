def queens(y, n): # 실질적으로 y값만 인자로 사용
    if y == n: #
        return 1
    q_sum = 0
    for x in range(n):
        if board[y][x]:
            continue
        for d in range(n-y):
            board[y+d][x] += 1
            if x-d >= 0:
                board[y+d][x-d] += 1
            if x+d < n:
                board[y+d][x+d] += 1
        q_sum += queens(y+1, n)
        for d in range(n - y):
            board[y + d][x] -= 1
            if x - d >= 0:
                board[y+d][x-d] -= 1
            if x + d < n:
                board[y+d][x+d] -= 1
    return q_sum


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [[0] * N for _ in range(N)]
    print('#{} {}'.format(tc, queens(0, N)))
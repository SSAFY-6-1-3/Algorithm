'''
# dfs 시간초과
def dfs():
    cnt = 0
    stack = [(0, 0)]
    while stack:
        r, c = stack.pop()
        if r == N - 1 and c == N - 1:
           cnt += 1
           continue

        jump = board[r][c]
        can_go = [(r + jump, c), (r, c + jump)]
        for next_r, next_c in can_go:
            if 0 <= next_r < N and 0 <= next_c < N:
                stack.append((next_r, next_c))
    return cnt
'''


N = int(input())
board = list(list(map(int, input().split())) for _ in range(N))
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1  # 왼쪽 위에서 시작한 것만 경우의 수 cnt 될 수 있도록

for r in range(N):
    for c in range(N):

        if dp[r][c] == 0:  # 경우의 수가 없다면 더 볼 필요 없음
            continue

        jump = board[r][c]

        if jump == 0:  # 진행할 수 없음
            continue

        next = [(r + jump, c), (r, c + jump)]  # 아래, 오른쪽으로 이동
        for next_r, next_c in next:
            if 0 <= next_r < N and 0 <= next_c < N:
                dp[next_r][next_c] += dp[r][c]  # 지금까지 이동해온 경우의 수 더해주기


print(dp[N - 1][N - 1])


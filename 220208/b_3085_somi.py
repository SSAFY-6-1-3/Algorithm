def check():
    cnt = 1
    for i in range(N):
        row = 1
        col = 1
        for j in range(1, N):
            if candies[i][j - 1] == candies[i][j]:
                row += 1
                cnt = max(cnt, row)
            else:
                row = 1

            if candies[j - 1][i] == candies[j][i]:
                col += 1
                cnt = max(cnt, col)
            else:
                col = 1

    return cnt

N = int(input())
candies = [list(input()) for _ in range(N)]
ans = 0
for r in range(N):
    for c in range(N):
        if r + 1 < N and candies[r][c] != candies[r + 1][c]:                        # 다르면
            candies[r][c], candies[r + 1][c] = candies[r + 1][c], candies[r][c]     # 바꿔
            ans = max(ans, check())                                                 # 몇 개 먹을 수있는지 count
            candies[r][c], candies[r + 1][c] = candies[r + 1][c], candies[r][c]     # 원위치

        if c + 1 < N and candies[r][c] != candies[r][c + 1]:
            candies[r][c], candies[r][c + 1] = candies[r][c + 1], candies[r][c]
            ans = max(ans, check())
            candies[r][c], candies[r][c + 1] = candies[r][c + 1], candies[r][c]
print(ans)
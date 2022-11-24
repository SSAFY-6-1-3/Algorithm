A = ' ' + input()
B = ' ' + input()
dp = [[[0, set()] for _ in range(len(B))] for _ in range(len(A))]

for i in range(len(A)):
    dp[i][0][1].add('')
for i in range(len(B)):
    dp[0][i][1].add('')

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j][0] = dp[i-1][j-1][0] + 1
            for st in dp[i-1][j-1][1]:
                dp[i][j][1].add(st + A[i])
        else:
            a, b = dp[i-1][j], dp[i][j-1]
            if a[0] == b[0]:
                dp[i][j][0] = dp[i-1][j][0]
                dp[i][j][1].update(a[1])
                dp[i][j][1].update(b[1])
            elif a[0] > b[0]:
                dp[i][j][0] = dp[i-1][j][0]
                dp[i][j][1].update(a[1])
            else:
                dp[i][j][0] = dp[i][j-1][0]
                dp[i][j][1].update(b[1])


print(dp[-1][-1][0])
print(dp[-1][-1][1].pop())


